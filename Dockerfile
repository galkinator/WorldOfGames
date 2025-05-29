FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy source code and Scores.txt
COPY . .
COPY scores.txt /Scores.txt

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the Flask default port (change if needed)
EXPOSE 5001

ENV FLASK_APP=MainScores.py

ENV FLASK_RUN_HOST=0.0.0.0

# Run the Flask app
CMD ["python", "MainScores.py"]
