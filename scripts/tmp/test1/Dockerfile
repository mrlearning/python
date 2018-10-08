FROM ubuntu:latest
ADD . /csv_to_postgres_script
WORKDIR /csv_to_postgres_script
RUN chmod +x script.py
RUN echo export PATH=$PATH:/csv_to_postgres_script >> ~/.bashrc
RUN apt-get update && apt-get -y install python3-pip && pip3 install -r requirements.txt