# Pull base image
FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
# Command performs mkdir and cd implicitly
WORKDIR /code

# Install dependencies
RUN pip install --upgrade pip
COPY /config/requirements/requirements220121.txt /code/
RUN pip install -r /code/requirements220121.txt

# Copy entire django project directory to /code/
COPY . /code/