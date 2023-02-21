FROM python

WORKDIR /code

COPY requirements.txt .


RUN pip install -r requirements.tx


COPY src/ .

CMD ["pytho","app.py"]
