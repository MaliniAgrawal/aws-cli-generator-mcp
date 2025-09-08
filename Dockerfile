# Dockerfile

# Use official Python image
FROM python:3.10-slim

# Set environment vars
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Copy requirement files
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy project code
COPY src/ ./src/

# Set environment for Flask
ENV PYTHONPATH=/app/src
ENV FLASK_APP=aws_mcp_cli.mcp_server
ENV FLASK_ENV=production

# Expose port for Flask
EXPOSE 5000

# Run the app
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
