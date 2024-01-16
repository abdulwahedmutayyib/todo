# Use an official Ubuntu runtime as a parent image
FROM ubuntu:latest

# Install system dependencies
RUN apt-get update && \
    apt-get install -y python3 python3-pip espeak libespeak1 && \
    pip3 install win10toast pyttsx3
RUN wget https://github.com/mhammond/pywin32/releases/download/b224/pywin32-224-cp38-cp38-win_amd64.whl
RUN pip3 install pywin32-224-cp38-cp38-win_amd64.whl


# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Make port 80 available to the world outside this container
# EXPOSE 80

# Run app.py when the container launches
CMD ["python3", "to-do.py"]
