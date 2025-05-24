FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy source code and Scores.txt
COPY . .
COPY Scores.txt /Scores.txt

# Install dependencies
RUN pip install --no-cache-dir flask

# Expose the Flask default port (change if needed)
EXPOSE 5000

# Run the Flask app
CMD ["python", "MainScores.py"]
