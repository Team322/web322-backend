FROM python:3.10.10

RUN python -m venv venv
RUN source venv/bin/activate
RUN pip install -r requirements.txt
ADD . /
EXPOSE 5000

CMD ["/bin/bash", "start.sh"]