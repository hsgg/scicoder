#!/usr/bin/env python

import sys
import numpy as np
from astropy.io import fits
import sqlalchemy
from SQLiteConnection import engine, Session
from ModelClasses import Sspp
import time


filename = 'ssppOut-dr9.fits'


table = fits.open(filename, memmap=True)[1].data

table = table.view(np.recarray)  # make it fast:

def numpytype2sqltype(nptype):
    if 'S' in nptype:
        return 'TEXT'
    elif 'i' in nptype:
        return 'INTEGER'
    elif 'f' in nptype:
        return 'DOUBLE'


sql_definition = 'CREATE TABLE "sspp" ('
sql_definition += '"id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE'
for i in range(len(table.dtype)):
    colname = table.dtype.names[i]
    nptype = str(table.dtype[i])
    coltype = numpytype2sqltype(nptype)
    sql_definition += ', "{0}" {1}'.format(colname, coltype)
sql_definition += ');'

print(sql_definition)



# read in data
session = Session()
session.begin()
start = time.time()
i = 0
for row in table:
    sspp = Sspp()

    for colname, nptype in table.dtype.descr:
        #print(colname, nptype, row[colname])
        if 'i' in nptype:
            #print(type(row[colname]))
            setattr(sspp, colname, int(row[colname]))
        else:
            setattr(sspp, colname, row[colname])

    session.add(sspp)

    i += 1
    if i % 1000 == 0:
        end = time.time()
        print(i, (end - start) / 1000 * (1800000 - i) / 60, "min")
        start = end
        session.commit()
        session.begin()


session.commit()
engine.dispose() # cleanly disconnect from the database
