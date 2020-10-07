FROM python:3.7-alpine
LABEL maintainer="howie_howerton@trendmicro.com"
# Add the project files
ADD . /flask-app
# Change directories to the /flask-app directory
WORKDIR /flask-app
# Install OS dependencies for Flask plugins (mainly Flask-Bcrypt)
RUN apk update && apk add --virtual build-deps gcc python3-dev musl-dev libffi-dev py-cffi
# Run setup script to install a virtualenv, install dependencies and create/seed the DB.
RUN sh init.sh
# The app is conigured to listen on port 5000
EXPOSE 5000
# Entrypoint for the application
ENTRYPOINT ["python"]
CMD ["app.py"]