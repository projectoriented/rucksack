FROM python:3.9-slim

LABEL base_image="python:3.9-slim"
LABEL about.home="https://github.com/projectoriented/rucksack"
LABEL about.tags="bioinformatics, preprocessing, utility"

# poetry version
ENV POETRY_VERSION=1.1.12

# use latest pip
RUN pip install --upgrade pip

# system dependencies
RUN pip install poetry==$POETRY_VERSION

# cache required files
WORKDIR /app
COPY . /app

# intialize project:
RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi
