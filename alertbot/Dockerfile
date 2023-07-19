FROM python:3.9-slim

WORKDIR /app

# Upgrade pip
RUN pip install --no-cache-dir --upgrade pip

# Copy the current directory to the container
COPY . .
COPY /requirements.txt .
# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "send_alert.py"]

