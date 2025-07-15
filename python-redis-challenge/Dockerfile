FROM python:3.8-slim
WORKDIR /app
COPY count.py .
RUN pip install flask redis
EXPOSE 5002
CMD ["python", "count.py"]
