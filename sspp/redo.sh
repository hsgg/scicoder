#!/bin/sh

rm table.sqlite

#sqlite3 student_data.sqlite < ../../scicoder/student_data.sql
sqlite3 table.sqlite < table.sql

./read.py
