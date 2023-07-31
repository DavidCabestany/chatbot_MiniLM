# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Set the working directory in the container
WORKDIR /app

# Add current directory files to the container
ADD . /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 5005 available to the world outside this container
EXPOSE 5005

# Run app.py when the container launches
CMD ["python", "app.py"]
