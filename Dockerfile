FROM python:3.10-slim

WORKDIR /app

COPY . .

# Remove or uncomment if you add requirements.txt
# RUN pip install -r requirements.txt

CMD ["python", "main.py"]
