FROM python:3.11

# Set the working directory inside the container
WORKDIR /app

# Copy application files to the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8080 for AWS EB
EXPOSE 8080

# # Start Gunicorn server for deployment
# CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8080", "application:app"]

# Start Gunicorn server in localhost
CMD ["gunicorn", "-w", "4", "-b", "localhost:8080", "application:app"]