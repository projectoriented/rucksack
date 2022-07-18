FROM python:3.10-slim

LABEL base_image="python:3.10-slim"
LABEL about.home="https://github.com/projectoriented/rucksack"
LABEL about.tags="bioinformatics, preprocessing, utility"

# poetry version
ENV POETRY_VERSION=1.1.13

# use latest pip
RUN pip install --upgrade pip

# install poetry
RUN pip install poetry==$POETRY_VERSION

# set working directory
WORKDIR /app

# copy files to container workdir for build context
COPY . .

# intialize project
RUN poetry config virtualenvs.create false
RUN poetry install --no-interaction --no-ansi
