# Use the official Python image as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install the project dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port that Flask will be running on
EXPOSE 6000

# Set the environment variables
ENV FLASK_APP=client-server.py

# Run the Flask application using host networking mode
CMD ["python", "-m", "flask", "run", "--host=0.0.0.0", "--port=6000", "--no-reload", "--no-debugger"]
