# Install base image
FROM python:3.7-slim-buster

# Add the source code into the container in a directory named app
ADD . /app

# Set working directory to app to run commands
WORKDIR /app

# Install required dependencies.
RUN pip install -r requirements.txt

# Declare env variables
ENV FLASK_APP=app.py
ENV FLASK_ENV=development

# Expose the port that flask will run on
EXPOSE 5000

# Run flask
CMD ["flask", "run", "--host=0.0.0.0"]