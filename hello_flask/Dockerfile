FROM python:3.8-slim
WORKDIR /app
COPY . /app
RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    libmariadb-dev \
    pkg-config
RUN  pip3 install flask mysqlclient
EXPOSE 5009
CMD ["python", "app.py"]
