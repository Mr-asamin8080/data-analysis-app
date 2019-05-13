FROM python:3.7

ENV PYTHONUNBUFFERED 1
ENV LANG C.UTF-8
ENV TZ Asia/Tokyo
ENV WORK_DIR=/home/src

RUN mkdir $WORK_DIR
WORKDIR $WORK_DIR
COPY ./src/app.py $WORK_DIR

RUN pip install elasticsearch
RUN pip install flask

CMD ["python", "app.py"]
