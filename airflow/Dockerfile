FROM apache/airflow:2.6.2

ARG CURRENT_USER=$USER

USER root

RUN apt-get -y update && apt-get -y upgrade
RUN apt-get install -y python3.9-distutils python3.9-dev build-essential

USER ${CURRENT_USER}