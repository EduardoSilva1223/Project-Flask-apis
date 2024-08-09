FROM python:3.12.5-alpine3.20
EXPOSE 5000

WORKDIR /app

COPY requirements.txt /app

RUN pip install --no-cache-dir -r requirements.txt

COPY Main.py .


CMD [ "python", "Main.py" ]