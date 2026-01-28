FROM python:3.11-slim

WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all application files
COPY . .

# Expose port
EXPOSE 10000

# Set environment variables
ENV PORT=10000

# Run the application
CMD ["python", "main.py"]
