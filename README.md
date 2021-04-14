# Project Webtechnologie

> A simple social media site (this was made as a school project and is not recommended to use for other purposes)

## Getting started without docker

1. Create a python environment: `python -m venv .venv`
2. Activate the environment: `./.venv/Scripts/Activate.ps1` or `source .venv/bin/activate`
3. Install a the requirements: `pip install -r requirements.txt`
4. Create the database: `flask db init` & `flask db migrate -m ""` & `flask db upgrade`
5. Start the program: `python app.py`
6. Open the site: `localhost:5000`

## Getting started with docker

1. Create the image: `docker build --pull --rm -f "DockerFile" -t projectwebtechnologie:latest "."`
2. Create the container: `docker run --rm -p 5000:5000 projectwebtechnologie:latest`
3. Open the site: `localhost:5000`
