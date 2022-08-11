## Importing libraries
    import pandas as pd
    import numpy as np
## Importing Data  
    Use these commands to import data from a variety of different sources and formats.


    pd.read_csv(filename) |                                   From a CSV file
    pd.read_table(filename) |                                 From a delimited text file (like TSV)
    pd.read_excel(filename) |                                 From an Excel file
    pd.read_sql(query, connection_object) |                   Read from a SQL table/database
    pd.read_json(json_string) |                               Read from a JSON formatted string, URL or file.
    pd.read_html(url) |                                       Parses an html URL, string or file and extracts tables to a list of dataframes
    pd.read_clipboard() |                                     Takes the contents of your clipboard and passes it to read_table()
    pd.DataFrame(dict) |                                      From a dict, keys for columns names, values for data as lists
## Exporting Data
    Use these commands to export a DataFrame to CSV, .xlsx, SQL, or JSON.

    df.to_csv(filename) |                                  Write to a CSV file
    df.to_excel(filename) |                                Write to an Excel file
    df.to_sql(table_name, connection_object) |             Write to a SQL table
    df.to_json(filename) |                                 Write to a file in JSON format
    
## Create Test Objects
    These commands can be useful for creating test segments.

    pd.DataFrame(np.random.rand(20,5)) |                               5 columns and 20 rows of random floats
    pd.Series(my_list) |                                               Create a series from an iterable my_list
    df.index = pd.date_range('1900/1/30', periods=df.shape[0]) |       Add a date index
    
