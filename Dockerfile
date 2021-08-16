FROM python:3.9.2-slim
WORKDIR /src/travelist/
ENV PYTHONPATH=/src/travelist/

COPY requirements.txt .

RUN pip install --upgrade pip setuptools wheel && pip install -r requirements.txt

COPY ./travelist/ /src/travelist/
