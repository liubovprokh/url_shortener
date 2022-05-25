FROM python:3.9

RUN apt-get update \
    && apt-get install gcc -y \
    && apt-get clean

RUN mkdir /code
WORKDIR /code
ADD ./.env ./.env

ADD ./requirements.txt ./requirements.txt
RUN pip install -r ./requirements.txt \
    && rm -rf /root/.cache/pip
ADD ./shortener_app ./shortener_app

CMD ["uvicorn", "shortener_app.main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]
