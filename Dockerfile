FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install certificates and dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    ca-certificates \
    && update-ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements
COPY requirements.txt .

# Upgrade pip and install dependencies
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copy app files
COPY . .

# Set PYTHONPATH so that aceest_fitness is always importable
ENV PYTHONPATH=/app

# Expose port
EXPOSE 5000

# Command to run the app
CMD ["python", "-m", "aceest_fitness.app"]
