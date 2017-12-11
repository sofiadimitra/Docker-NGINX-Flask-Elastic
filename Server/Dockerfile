FROM python:3.6-alpine

ADD ./Server /app
WORKDIR /app
RUN pip install -r requirements.txt

EXPOSE 5000
CMD ["python", "api.py"]