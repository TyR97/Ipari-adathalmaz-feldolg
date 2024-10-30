import pandas as pd

import DataFrameProcessing as DFP
import sqlite3

conn = sqlite3.connect('test.db')

meres_df = DFP.df_init('Hűtőpanelek.csv')
#adag_df = DFP.df_init('Adagok.csv')
#adag_df = pd.read_csv('Adagok.csv', sep=',', engine='python')
new_df = DFP.df_processor(meres_df)

conn.execute('''CREATE TABLE IF NOT EXISTS meres (
        MeresID INTEGER PRIMARY KEY AUTOINCREMENT,
        Panel INTEGER,
        Ido TEXT,
        Homerseklet REAL);''')

DFP.df_cleaner(new_df)

#new_df.to_sql('meres', conn, if_exists='append', index=False)
#adag_df.to_sql('adagok', conn, if_exists='append', index=False)
conn.close()
#print(new_df)




