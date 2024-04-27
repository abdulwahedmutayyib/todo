FROM python:3.9-slim-buster

# Set working directory
WORKDIR /app

# Copy code and requirements file
COPY . .

# Install dependencies from requirements.txt
RUN pip install --upgrade pip  # Ensure latest pip
RUN pip install -r requirements.txt

# Specify default command
CMD ["python", "to-do.py"]
