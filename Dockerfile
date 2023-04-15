FROM python:3

RUN python -m venv venv
ADD . /
EXPOSE 5000

CMD ["/bin/bash", "start.sh"]