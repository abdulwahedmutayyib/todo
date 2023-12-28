# Use an official Ubuntu runtime as a parent image
FROM ubuntu:latest

# Set the working directory to /app
WORKDIR /app

# Install required dependencies
RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    apt-get install -y espeak libespeak1 && \
    pip3 install --upgrade setuptools && \
    pip3 install win10toast pyttsx3 pypiwin32==223

# Copy the local code into the container at /app
COPY . /app

# Run the Python script
CMD ["python3", "to-do.py"]
