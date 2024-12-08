# Use the official Python image as the base image
FROM python:3.10.6-slim

# Set environment variables for Python
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /app

# Install system dependencies for PostgreSQL and other necessary tools
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       gcc \
       libpq-dev \
       python3-dev \
       build-essential \
       pkg-config \
       && rm -rf /var/lib/apt/lists/*

# Copy the requirements file into the container
COPY requirements.txt /app/

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copy the Django application code into the container
COPY . /app/

# Expose the port the Django app runs on
EXPOSE 8000

# Set the default command to run the Django app
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
