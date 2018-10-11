FROM postgres:10

ADD . /csv_to_postgres_script

RUN chmod +x /csv_to_postgres_script/script.py

COPY create_db.sh /docker-entrypoint-initdb.d

ENV PATH $PATH:/csv_to_postgres_script

RUN apt-get update &&\
    apt-get install -y python3-pip &&\
    pip3 install -r /csv_to_postgres_script/requirements.txt

#USER postgres

#RUN /etc/init.d/postgresql start &&\
#    psql --command "ALTER USER postgres WITH PASSWORD 'postgres';" &&\
#    createdb test_database &&\
#    psql -d test_database -c "CREATE TABLE test(id SERIAL PRIMARY KEY, date DATE, url TEXT, count INTEGER);"