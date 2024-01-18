# Use the official Windows Server Core image
FROM mcr.microsoft.com/windows/servercore:ltsc2022

# Set the working directory in the container
WORKDIR C:\app

# Download and install Python
RUN Invoke-WebRequest -Uri https://www.python.org/ftp/python/3.9.7/python-3.9.7.exe -OutFile python.exe ; \
    Start-Process -Wait -FilePath .\python.exe -ArgumentList '/quiet InstallAllUsers=1 PrependPath=1'

# Verify Python installation
RUN python --version

# Copy your Python script into the container
COPY to-do.py .

# Set the command to run your Python script
CMD ["python", "to-do.py"]
