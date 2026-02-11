FROM python:3.11-slim
WORKDIR /app
COPY frontend.py .
COPY requirements.txt .
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python" , "frontend.py"]