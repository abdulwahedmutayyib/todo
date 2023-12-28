<<<<<<< HEAD
# Use an official Ubuntu runtime as a parent image
FROM ubuntu:latest
=======
# Use an official Python runtime as a parent image
FROM python:3.8-slim
>>>>>>> eab571a5613a554987cb3ee43e3b94b6b3052fe4

# Set the working directory to /app
WORKDIR /app

# Install any necessary dependencies
RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    apt-get install -y espeak libespeak1 && \
    pip3 install win10toast pyttsx3

# Copy the current directory contents into the container at /app
COPY . /app

<<<<<<< HEAD
# Run app.py when the container launches
CMD ["python3", "to-do.py"]

=======
# Install any needed packages specified in requirements.txt
RUN python -m pip install pywin32
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME=World

# Run the script when the container launches
CMD ["python", "to-do.py"]
>>>>>>> eab571a5613a554987cb3ee43e3b94b6b3052fe4

