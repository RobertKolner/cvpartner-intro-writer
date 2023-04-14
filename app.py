import json

import click
import uvicorn
from litestar import Litestar, get

import config

from cvpartner import client as cvpartner_client
from profile.openai import call_openai, create_prompt
from profile.prepare import prepare_profile


@get("/generate-intro")
def generate_intro(email: str, language: str) -> dict[str, str]:
    # Step 1: Obtain API keys
    cvpartner_api_key = config.env.cvpartner_api_key
    openai_api_key = config.env.openai_api_key

    # Step 2: Find user_id
    user_id, cv_id = cvpartner_client.find_user_id(email, cvpartner_api_key)

    # Step 3: Make an API request to CVPartner
    cv = cvpartner_client.query_cv(user_id, cv_id, cvpartner_api_key)

    # Step 4: Extract relevant information
    profile = prepare_profile(cv, language)

    # Step 5: Use the OpenAI API to generate the intro text
    cv_prompt = create_prompt(cv.name, profile, language)
    intro_text = call_openai(cv_prompt, openai_api_key)

    # Step 6: Return the generated text
    return {"profile": profile, "prompt": cv_prompt, "intro_text": intro_text}


app = Litestar(route_handlers=[generate_intro])


if __name__ == "__main__":

    @click.command()
    def server():
        uvicorn.run(app)

    @click.command()
    @click.argument("email")
    def fetch(email: str):
        cvpartner_api_key = config.env.cvpartner_api_key
        user_id, cv_id = cvpartner_client.find_user_id(email, cvpartner_api_key)
        cv = cvpartner_client.query_cv(user_id, cv_id, cvpartner_api_key)
        print(json.dumps(cv.dict(), indent=4))

    @click.command()
    def list_users():
        cvpartner_api_key = config.env.cvpartner_api_key
        user_data = cvpartner_client.search_users(cvpartner_api_key)
        print(json.dumps(user_data, indent=4))

    @click.command()
    @click.argument("email")
    def prompt(email: str):
        language = "no"
        cvpartner_api_key = config.env.cvpartner_api_key

        # Step 2: Find user_id
        user_id, cv_id = cvpartner_client.find_user_id(email, cvpartner_api_key)

        # Step 3: Make an API request to CVPartner
        cv = cvpartner_client.query_cv(user_id, cv_id, cvpartner_api_key)

        # Step 4: Extract relevant information
        profile = prepare_profile(cv, language)

        # Step 5: Use the OpenAI API to generate the intro text
        print(create_prompt(cv.name, profile, language))

    @click.group()
    def group():
        pass

    group.add_command(fetch)
    group.add_command(list_users)
    group.add_command(prompt)
    group.add_command(server)
    group()
