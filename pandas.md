### importing libraries
    import pandas as pd
    import numpy as np
### Importing Data    
    pd.read_csv(filename) |                                          From a CSV file
    pd.read_table(filename) |                                        From a delimited text file (like TSV)
    pd.read_excel(filename) |                                        From an Excel file
    pd.read_sql(query, connection_object) |                          Read from a SQL table/database
    pd.read_json(json_string) |                                      Read from a JSON formatted string, URL or file.
    pd.read_html(url) |                                              Parses an html URL, string or file and extracts tables to a list of dataframes
    pd.read_clipboard() |                                            Takes the contents of your clipboard and passes it to read_table()
    pd.DataFrame(dict) |                                             From a dict, keys for columns names, values for data as lists
