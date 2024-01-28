################################################################
# -*- coding: utf-8 -*-
################################################################
import sys
import os
import pandas as pd
import sqlite3 as sq

sDatabaseName='C:/VKHCG/99-DW/datawarehouse.db'
conn1 = sq.connect(sDatabaseName)

sTable = 'Dim-BMI'
print('Loading :',sDatabaseName,' Table:',sTable)
sSQL="SELECT * FROM [Dim-BMI];"
PersonFrame0=pd.read_sql_query(sSQL, conn1)
print(PersonFrame0)


print('Loading :',sDatabaseName,' Table:',sTable)
sSQL="SELECT \
       Height,\
       Weight,\
       Indicator,\
       CASE Indicator\
       WHEN 1 THEN 'Pip'\
       WHEN 2 THEN 'Norman'\
       WHEN 3 THEN 'Grant'\
       ELSE 'Sam'\
       END AS Name\
  FROM [Dim-BMI]\
  WHERE Indicator > 2\
  ORDER BY  \
       Height,\
       Weight;"
PersonFrame1=pd.read_sql_query(sSQL, conn1)
print(PersonFrame1)

DimPerson=PersonFrame1
DimPersonIndex=DimPerson.set_index(['Indicator'],inplace=False)
################################################################
sDatabaseName='C:/VKHCG/99-DW/datamart.db'
conn2 = sq.connect(sDatabaseName)
sTable = 'Dim-BMI-Secure'
DimPersonIndex.to_sql(sTable, conn2, if_exists="replace")

sSQL="SELECT * FROM [Dim-BMI-Secure] WHERE Name = 'Sam';"
PersonFrame2=pd.read_sql_query(sSQL, conn2)
print(PersonFrame2)
