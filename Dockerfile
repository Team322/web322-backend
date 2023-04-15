FROM python:3

RUN python -m venv venv
ADD . /

CMD ["/bin/bash", "start.sh"]