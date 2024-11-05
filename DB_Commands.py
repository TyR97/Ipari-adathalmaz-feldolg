import sqlite3
"""
  Creates the db database session and structor
  Parameters
  ----------
  db_name : String
      Name of the Database

  Returns
  conn : database session
  -------
  """
def db_init(db_name):
    conn = sqlite3.connect(db_name)

    conn.execute('''
        CREATE TABLE IF NOT EXISTS meres (
        MeresID INTEGER PRIMARY KEY AUTOINCREMENT,
        Panel INTEGER,
        Ido TEXT,
        Homerseklet REAL);''')

    conn.execute('''
        CREATE TABLE IF NOT EXISTS adagok (
        AdagID INTEGER PRIMARY KEY AUTOINCREMENT,
        KezdetIdo TEXT,
        VegeIdo TEXT);''')

    conn.execute('''
        CREATE TABLE IF NOT EXISTS meres_adag(
    	MeresID	INT,
    	AdagID	INT,
    	PRIMARY KEY(MeresID, AdagID),
    	FOREIGN KEY("AdagID") REFERENCES "adagok"("AdagID"),
    	FOREIGN KEY("MeresID") REFERENCES "meres"("MeresID")
    );''')

    return conn

"""
  Exports the DataFrames to the database.
  Parameters
  ----------
  conn : 
  df_meres: DataFrame
    Dataframe containing the meres data
  df_adagok: DataFrame
    Dataframe containing the adagok data

  Returns
  -------
  """

def db_export(conn, df_meres, df_adagok):
    df_meres.to_sql('meres', conn, if_exists='append', index=False)
    df_adagok.to_sql('adagok', conn, if_exists='append', index=False)


"""
  Populates the Junction table and closes the database session
  Parameters
  ----------
  conn : database session

  Returns
  -------
  """
def populate_junction_table(conn):
    cursor = conn.cursor()
    try:
        # Execute the query
        conn.execute('''
            INSERT INTO meres_adag (MeresID, AdagID)
            SELECT meres.MeresID, adagok.AdagID
            FROM meres
            JOIN adagok
            ON meres.Ido BETWEEN adagok.KezdetIdo AND adagok.VegeIdo;''')
        conn.commit()
        print("Junction table populated successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Close the connection
        conn.close()



