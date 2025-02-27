FROM python:3.11

# Set the working directory inside the container
WORKDIR /app

# Copy application files to the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8000 for AWS EB
EXPOSE 8000

# # Start Gunicorn server for deployment
# CMD ["gunicorn", "-w", "4", "--threads", "2", "-b", "0.0.0.0:8000", "app:app"]

# Start Gunicorn server in localhost
CMD ["gunicorn", "-w", "4", "--threads", "2", "-b", "localhost:5007", "app:app"]

