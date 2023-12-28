# Use an official Python runtime as a parent image
FROM python:3.8-windowsservercore

# Set the working directory in the container
WORKDIR C:\app

# Copy the current directory contents into the container at /app
COPY . .

# Install Python dependencies
RUN pip install pywin10toast pyttsx3

# Run the script when the container launches
CMD ["python", "your_script_name.py"]
