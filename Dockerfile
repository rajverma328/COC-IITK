# Use the official Python image as a base
FROM python:3.10-alpine

# Set environment variables to avoid .pyc files and buffer issues
ENV APP /scheduler
RUN mkdir ${APP}

# Set the working directory
WORKDIR ${APP}

# Copy the requirements.txt to the working directory
COPY ./BACK_END/requirements.txt ./

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the container
RUN mkdir BACK_END
RUN mkdir FRONT_END
RUN mkdir ASSETS
COPY ./BACK_END/ ./BACK_END/
COPY ./ASSETS/ ./ASSETS/
COPY ./FRONT_END/ ./FRONT_END/

# Expose the port the Flask app will run on
ENV PORT=5000
EXPOSE 5000

# Run the application with Gunicorn in production mode
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "BACK_END.app_server:app"]

