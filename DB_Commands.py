import sqlite3

#TODO: Add functionalities:
# to convert DF to SQLite db
# and other DB related funcs
def db_init(db_name):
    conn = sqlite3.connect(db_name)

    conn.execute('''CREATE TABLE IF NOT EXISTS meres (
            MeresID INTEGER PRIMARY KEY AUTOINCREMENT,
            Panel INTEGER,
            Ido TEXT,
            Homerseklet REAL);''')

    conn.execute('''CREATE TABLE IF NOT EXISTS adagok (
        AdagID INTEGER PRIMARY KEY AUTOINCREMENT,
        KezdetIdo TEXT,
        VegeIdo TEXT);''')

    conn.execute('''CREATE TABLE IF NOT EXISTS meres_adag(
    	MeresID	INT,
    	AdagID	INT,
    	FOREIGN KEY("AdagID") REFERENCES "adagok"("AdagID"),
    	FOREIGN KEY("MeresID") REFERENCES "meres"("MeresID")
    );''')

    return conn

def db_alter_table(table_name, conn):
    conn.execute('''UPDATE {table_name}
        SET KezdetIdo = ,
    ''')


def db_export(conn, df_meres, df_adagok):
    df_meres.to_sql('meres', conn, if_exists='replace', index=False)
    df_adagok.to_sql('adagok', conn, if_exists='replace', index=False)
    conn.close()


