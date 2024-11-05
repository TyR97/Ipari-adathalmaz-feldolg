import pandas as pd

"""
 Reads CSV into a Pandas DataFrame.

  Parameters
  ----------
  csv_path : string
      Path to csv file
      
  Returns
  -------
  Pandas DataFrame
  """

def df_init(csv_path):
    with open(csv_path, 'r') as f:
        line = f.readline()
        if ';' in line:
            try:
                df = pd.read_csv(csv_path, sep=';', engine='python')
                print('CSV loaded successfully.')
            except Exception as e:
                print('CSV could not be loaded.')
            return df
        elif ',' in line:
            try:
                df = pd.read_csv(csv_path, sep=',', engine='python')
            except Exception as e:
                print('CSV could not be loaded.')
            return df
        else:
            raise ValueError('Unknown separator in file')



"""
 Iterates trough the DataFrame columns, creates a new Pandas DataFrame with the following columns:
    MeresID
    Panel
    Ido
    Homerseklet

  Parameters
  ----------
  old_df : DataFrame
      The DataFrame to be copied

  Returns
  -------
  Pandas DataFrame
  """
def df_processor(old_df):

    new_df = pd.DataFrame(columns=['Panel', 'Ido', 'Homerseklet'])

    for idx in range(len(old_df)):
        time_col = f'Panel hőfok {idx} [°C] Time'
        temp_col = f'Panel hőfok {idx} [°C] ValueY'

        if temp_col in old_df.columns and time_col in old_df.columns:
            temp_df = pd.DataFrame({
                #'MeresID': old_df.index + 1,
                'Panel': idx,
                'Ido': old_df[time_col],
                'Homerseklet': old_df[temp_col]
            })
            new_df = pd.concat([new_df, temp_df])

    new_df['Panel'] = new_df['Panel'].astype(int)
    new_df['Ido'] = new_df['Ido'].astype(str)
    new_df['Homerseklet'] = new_df['Homerseklet'].str.replace(',','.').astype(float)
    return new_df
"""
  Changes the . to - in the Ido column.
  Makes sure that every timestamp has a leadingzero
  Parameters
  ----------
  old_df : DataFrame
      The DataFrame to modify

  Returns
  -------
  """
def df_cleaner(old_df):
    old_df['Ido'] = old_df['Ido'].str.replace('.','-')
    old_df['Ido'] = pd.to_datetime(old_df['Ido'])

"""
  Makes sure that that date is in the YYYY-MM-DD format.
  Parameters
  ----------
  old_df : DataFrame
      The DataFrame to modify

  Returns
  -------
  """
def date_to_right_format(date):
    return pd.to_datetime(date, dayfirst=True).dt.strftime('%Y-%m-%d')

