FROM python:3.10.6-slim-bullseye
# Set environment variables
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
COPY . /horoscopebot
WORKDIR /horoscopebot
RUN pip install -r requirements.txt
EXPOSE 8443