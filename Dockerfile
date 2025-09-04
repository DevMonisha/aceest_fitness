# Use slim Python 3.11 image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app
COPY . .

# Set PYTHONPATH so that aceest_fitness is always importable
ENV PYTHONPATH=/app

# Expose port
EXPOSE 5000

# Default command to run Flask app
CMD ["python", "-m", "aceest_fitness.app"]
