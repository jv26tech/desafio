FROM python:3.10

# Create app directory
WORKDIR /app

# Install app dependencies
COPY requirements.txt /app

RUN pip install -r requirements.txt

# Bundle app source
COPY . /app