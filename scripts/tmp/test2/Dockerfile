FROM ubuntu:latest

ADD . /csv_to_postgres_script

RUN chmod +x /csv_to_postgres_script/script.py

ENV PATH $PATH:/csv_to_postgres_script

RUN apt-get update &&\
    apt-get install -y postgresql-10 postgresql-contrib-10 python3-pip &&\
    pip3 install -r requirements.txt

USER postgres

RUN /etc/init.d/postgresql start &&\
    psql --command "ALTER USER postgres WITH PASSWORD 'postgres';" &&\
    createdb test_database &&\
    psql -d test_database -c "CREATE TABLE test(id SERIAL PRIMARY KEY, date DATE, url TEXT, count INTEGER);"
    
RUN echo "host all  all    0.0.0.0/0  md5" >> /etc/postgresql/10/main/pg_hba.conf

RUN echo "listen_addresses='*'" >> /etc/postgresql/10/main/postgresql.conf

EXPOSE 5432

VOLUME  ["/etc/postgresql", "/var/log/postgresql", "/var/lib/postgresql"]

CMD ["/usr/lib/postgresql/10/bin/postgres", "-D", "/var/lib/postgresql/10/main", "-c", "config_file=/etc/postgresql/10/main/postgresql.conf"]
