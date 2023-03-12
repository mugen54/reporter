# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory to /app
WORKDIR /app


COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt 

# Copy the rest of the application code into the container
COPY . .
RUN chmod 777 /app/reporter/main.py 
RUN chmod 777 /app/reporter/receive.py
# Expose port 8000 for the application to listen on

# Start the RabbitMQ server in the background
CMD ["python", "-u", "reporter/main.py"]

