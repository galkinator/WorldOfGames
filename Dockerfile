FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy source code and Scores.txt
COPY . .
COPY Scores.txt /Scores.txt

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8777

# Run the Flask app
CMD ["python", "MainScores.py"]
