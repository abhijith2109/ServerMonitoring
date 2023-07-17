FROM python:3.11.0b4-bullseye

WORKDIR /app

COPY . .

# Copy the requirements.txt file to the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

RUN pip install requirements.txt

CMD ["python", "client-server.py"]