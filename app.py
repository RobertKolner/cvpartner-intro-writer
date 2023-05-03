import json

import click
import uvicorn
from litestar import Litestar, get

import config
from config import logger

from cvpartner import client as cvpartner_client
from profile.openai import call_openai, create_prompt
from profile.prepare import prepare_profile


def generate_intro(email: str, language: str, return_at: str = None) -> dict[str, str]:
    # Step 1: Obtain API keys
    logger.info("Generating intro text for {}", email)
    cvpartner_api_key = config.env.cvpartner_api_key
    openai_api_key = config.env.openai_api_key

    # Step 2: Find user_id
    logger.info("Finding user_id for {}", email)
    user_id, cv_id = cvpartner_client.find_user_id(email, cvpartner_api_key)
    if return_at == "user_id":
        return {"user_id": user_id, "cv_id": cv_id}

    # Step 3: Make an API request to CVPartner
    logger.info("Querying CVPartner for user_id {}", user_id)
    cv = cvpartner_client.query_cv(user_id, cv_id, cvpartner_api_key)
    if return_at == "cv":
        return {"cv": cv.json(indent=4)}

    # Step 4: Extract relevant information
    logger.info("Preparing profile for user_id {}", user_id)
    profile = prepare_profile(cv, language)
    if return_at == "profile":
        return {"profile": profile}

    # Step 5: Use the OpenAI API to generate the intro text
    logger.info("Generating prompt for user_id {}", user_id)
    cv_prompt = create_prompt(cv.name, profile, language)
    if return_at == "prompt":
        return {"profile": profile, "prompt": cv_prompt}

    logger.info("Calling OpenAI API for user_id {}", user_id)
    intro_text = call_openai(cv_prompt, openai_api_key)

    # Step 6: Return the generated text
    return {"profile": profile, "prompt": cv_prompt, "intro_text": intro_text}


@get("/generate-intro")
def generate_intro_handler(email: str, language: str) -> dict[str, str]:
    return generate_intro(email, language)


app = Litestar(route_handlers=[generate_intro_handler])


if __name__ == "__main__":

    @click.command()
    def server():
        uvicorn.run(app)

    @click.command()
    @click.argument("email")
    @click.option("--language", default="no")
    @click.option(
        "--return-at",
        type=click.Choice(["intro_text", "user_id", "cv", "profile", "prompt"]),
        default="intro_text",
    )
    def run(email: str, language: str, return_at: str):
        print(generate_intro(email, language, return_at=return_at)[return_at])

    @click.command()
    def list_users():
        cvpartner_api_key = config.env.cvpartner_api_key
        user_data = cvpartner_client.search_users(cvpartner_api_key)
        print(json.dumps(user_data.json(), indent=4))

    @click.group()
    def group():
        pass

    group.add_command(list_users)
    group.add_command(run)
    group.add_command(server)
    group()
