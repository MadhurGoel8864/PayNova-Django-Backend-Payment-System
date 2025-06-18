# Base image with Python
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy project files
COPY . .

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Collect static files if using Django static files (optional)
# RUN python manage.py collectstatic --noinput

# Set environment variables (example)
ENV PYTHONUNBUFFERED=1

# Run migrations and then start the server
CMD ["sh", "-c", "python manage.py migrate && gunicorn payment_prj.wsgi:application --bind 0.0.0.0:$PORT"]
