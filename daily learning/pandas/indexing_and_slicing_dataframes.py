import pandas as pd

excel_file_path = r"C:\Users\mohan.7482\Desktop\daily learning\pandas\final_excel_sheet_Settlement Order.xlsx"

excel_data = pd.read_excel(excel_file_path)

df = pd.DataFrame(excel_data)

print(df,"entire dataframe")

print(df.head(),"print first five rows")

print(df.head(7),"we may specify how many rows we want from first")


print(df.tail(),"print last five rows")

print(df.tail(7),"we may specify how many rows we want from last")


print(df.describe(),"print statistical measures for each numeric column in the dataframe")

print(df.columns,"number of columns in the dataframe")

print(df.shape,"print the shape of the dataframe")


