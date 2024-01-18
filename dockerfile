# Use the official Python image for Windows
FROM dockurr/windows

# Set the working directory in the container
WORKDIR C:/app

# Copy the Python script and requirements file into the container
COPY to-do.py .
COPY requirements.txt .

# Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port on which the application will run
EXPOSE 5000

# Command to run the Python script
CMD ["python", "to-do.py"]
