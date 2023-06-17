FROM python:3.10.6-slim-bullseye
# Set environment variables

# ### Locale support fr_FR and timezone CET ###
RUN apt-get update
RUN apt-get install -y locales locales-all
ENV LC_ALL fr_FR.UTF-8
ENV LANG fr_FR.UTF-8
ENV LANGUAGE fr_FR.UTF-8
### Locale Support END ###
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
COPY ./horoscopebot /horoscopebot
WORKDIR /horoscopebot
RUN python3 -m pip install -r requirements.txt
EXPOSE 8443