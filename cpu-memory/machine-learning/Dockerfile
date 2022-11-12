FROM jupyter/scipy-notebook

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
RUN pip3 install joblib

COPY csv/train.csv ./csv/train.csv
COPY csv/test.csv ./csv/test.csv

COPY app.py ./app.py
COPY inference.py ./inference.py

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
