FROM python:3.8

COPY ./requirements.txt /webapp/requirements.txt

WORKDIR /webapp

RUN pip install -r requirements.txt

# COPY roberta-sequence-classification-9.onnx /webapp

COPY webapp/* /webapp


ENTRYPOINT ["python"]

CMD ["app.py"]