from textwrap import dedent

import openai


def create_prompt(name: str, profile: str, language: str) -> str:
    prompts = {
        "int": dedent(
            f"""This is a profile for a consultant named {name}. I want you to generate
                a good intro text for this profile. The profile is in English, so
                please write the intro text in English. The profile is as follows:

                {profile}"""
        ),
        "no": dedent(
            f"""Dette er en profil for en konsulent som heter {name}. Jeg vil at du
                skal generere en profesjonell og god introtekst for denne profilen. Den
                skal fremheve kvalitetene til personen og gjøre det lettere å selge de
                inn til en kunde. Legg vekt på teknologier konsulenten behersker.
                Profilen er på norsk, så vennligst skriv introteksten på norsk.
                Profilen er som følger:

                {profile}"""
        ),
    }

    return prompts[language]


def call_openai(prompt: str, openai_api_key: str) -> str:
    openai.api_key = openai_api_key
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content.strip()
