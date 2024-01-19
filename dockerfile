# Use the official Python image for Windows
FROM mcr.microsoft.com/windows/nanoserver:1809

# Set the working directory inside the container
WORKDIR C:\app

# Copy the local code to the container
COPY . .

# Install required dependencies
RUN pip install pywin32 pyttsx3 pypiwin32 win10toast

# CMD to run the Python script
CMD ["python", "to-do.py"]
