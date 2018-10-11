#!/bin/bash

createdb test_database
psql -d test_database -c "CREATE TABLE test(id SERIAL PRIMARY KEY, date DATE, url TEXT, count INTEGER);"