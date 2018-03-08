FROM python:
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements/local.txt /code/
RUN pip install -r requirements.txt
ADD . /code
