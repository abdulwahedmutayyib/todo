# Use a compatible Windows image
FROM mcr.microsoft.com/windows/servercore:ltsc2022

# Set working directory
WORKDIR C:/app

# Copy code and requirements file
COPY . .

# Install dependencies from requirements.txt
RUN python -m pip install --upgrade pip  # Ensure latest pip
RUN pip install -r requirements.txt

# Specify default command
CMD ["python", "to-do.py"]
