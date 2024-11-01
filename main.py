import DataFrameProcessing as DFP
import DB_Commands as DBC


conn = DBC.db_init('test3.db')

meres_df = DFP.df_init('Hűtőpanelek.csv')
new_df = DFP.df_processor(meres_df)
adag_df = DFP.df_init('Adagok.csv')

adag_df['Kezdet_DATUM'] =  DFP.date_to_right_format(adag_df['Kezdet_DATUM'])
adag_df['Vege_DATUM'] = DFP.date_to_right_format(adag_df['Vege_DATUM'])


DFP.df_cleaner(new_df)

#print(adag_df)

DBC.db_export(conn, new_df, adag_df)
#print(adag_df['Vege_DATUM'])
#print(new_df)




