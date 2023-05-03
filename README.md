# CVPartner Intro Writer

`cvpartner-intro-writer` is a Python 3.10+ application that generates personalized introductory text for users by querying their CVs from CVPartner and generating an intro text using OpenAI's API. The application uses `click` for command line operations and the `Litestar` web framework for hosting an API endpoint.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
  - [Command Line Interface (CLI)](#cli)
  - [API Endpoint](#api-endpoint)
- [Development](#development)
  - [Poetry](#poetry)
  - [Pre-commit](#pre-commit)

## Features

- Fetches user CV data from CVPartner
- Generates personalized intro text using OpenAI's API
- Provides CLI commands to fetch user data, list users, and generate intro prompts
- Exposes an API endpoint to generate intro text with user email and language

## Installation

Ensure you have Python 3.10+ installed on your system.

1. Clone this repository:

```bash
git clone https://github.com/yourusername/cvpartner-intro-writer.git
cd cvpartner-intro-writer
```

Install poetry package manager:

```
pip install poetry
```

Install the dependencies:

```
poetry install
```

Create a .env file in the root directory of the project, and add your API keys:

```
CVPARTNER_API_KEY=your_cvpartner_api_key
OPENAI_API_KEY=your_openai_api_key
```

## Usage

### CLI

Fetch user CV data by email:

```poetry run python3 -m app -- run --return-at=cv user@example.com```

List all users:

```poetry run python3 -m app -- list-users```

Generate an intro prompt for a user by email:

```poetry run python3 -m app -- run --return-at=prompt user@example.com```

### API Endpoint

Start the server:

```poetry run server```

Access the API endpoint to generate intro text:

```curl "http://localhost:8000/generate-intro?email=user@example.com&language=en"```

## Development

### Poetry

poetry is used for package management. To add a new dependency, use the following command:

```poetry add package_name```

### Pre-commit

pre-commit is used for linting and code formatting. To set up pre-commit hooks, run:

```pre-commit install```

To run pre-commit manually:

```pre-commit run --all-files```
