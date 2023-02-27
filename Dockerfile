# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory to /app
WORKDIR /app

#RUN apt-get update && \
#   apt-get install -y rabbitmq-server && \
#   apt-get clean && \
#  rm -rf /var/lib/apt/lists/*
# Copy the requirements file into the container
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Expose port 8000 for the application to listen on
EXPOSE 8000

# Start the RabbitMQ server in the background
#CMD rabbitmq-server -detached  && \
#    python /app/reporter/main.py
#sleep 10 && \

#CMD ["pip install pandas","pip install jinja2","pip install matplotlib","pip install pika"]
