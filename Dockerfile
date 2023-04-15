FROM python:3.10.10

RUN python -m venv venv
RUN . venv/bin/activate
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
ADD . /
EXPOSE 5000

CMD ["/bin/bash", "start.sh"]