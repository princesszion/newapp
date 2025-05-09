# Use official Python slim image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install python-decouple gunicorn psycopg2-binary
RUN pip install -r requirements.txt

# Copy project files
COPY . .

# Copy .env file
COPY .env .env

# Collect static files and apply DB migrations
RUN python manage.py collectstatic --noinput || true
# RUN python manage.py migrate

# Expose port
EXPOSE 8000

# Start with Gunicorn
CMD ["gunicorn", "myproject.wsgi:application", "--bind", "0.0.0.0:80"]
