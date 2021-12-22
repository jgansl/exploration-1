#!/usr/bin/python3
# -*- coding: utf-8 -*-
#! https://kb.objectrocket.com/postgresql/python-and-postgresql-docker-container-part-2-1063
# import the connect library from psycopg2
from psycopg2 import connect

table_name = "some_table"

# declare connection instance
conn = connect(
    dbname = "some_db",
    user = "objectrocket",
    host = "172.28.1.4",
    password = "1234"
)

# declare a cursor object from the connection
cursor = conn.cursor()

# execute an SQL statement using the psycopg2 cursor object
cursor.execute(f"SELECT * FROM {table_name};")

# enumerate() over the PostgreSQL records
for i, record in enumerate(cursor):
    print ("\n", type(record))
    print ( record )

# close the cursor object to avoid memory leaks
cursor.close()

# close the connection as well
conn.close()class AdaptableYellowRat(QCAlgorithm):

    def Initialize(self):
        self.SetStartDate(2020,1, 1)
        self.SetEndDate(2021,1,1)
        self.SetCash(100000)
        self.AddEquity("TSLA", Resolution.Minute)
        self.rsi = self.RSI("TSLA", 14)
        self.SetWarmUp(14)

    def OnData(self, data):
        if self.IsWarmingUp:
            return
        if not self.Portfolio["TSLA"].Invested:
            if self.rsi.Current.Value < 60:
                self.MarketOrder("TSLA", 100)
        else:
            if self.rsi.Current.Value > 85:
                self.Liquidate()

    def OnEndOfDay(self):
        self.Plot("Indicators","RSI", self.rsi.Current.Value)

