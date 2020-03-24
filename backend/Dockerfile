from python:3

workdir /usr/src/app
COPY requirements.txt ./
run pip3 install -r requirements.txt

CMD [ "python3", "-u", "-m", "backend" ]