FROM python:3.10.13

RUN pip install --upgrade pip

RUN pip install --upgrade setuptools wheel

WORKDIR /app

ADD . /app/

COPY requirements.txt .

RUN pip install -r requirements.txt

RUN python dependencies.py

EXPOSE 8080

CMD ["gunicorn", "-w", "8", "-b", "0.0.0.0:8080", "run:app"]