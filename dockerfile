# Use an official Ubuntu runtime as a parent image
FROM ubuntu:latest

# Set the working directory to /app
WORKDIR /app

# Install any necessary dependencies
RUN apt-get update -y
    apt-get install -y python3
    apt-get install -y python3-pip
    apt-get install -y espeak libespeak1 
    pip3 install win10toast pyttsx3

# Copy the current directory contents into the container at /app
COPY . /app

# Run app.py when the container launches
CMD ["python3", "to-do.py"]
