import pandas as pd
import matplotlib.pyplot as plt
import openpyxl

# series = pd.Series([10, 20, 30, 40], ['A', 'B', 'C', 'D'])

# print(series['B'])

# print(series.iloc[2])

# series.name = "mySeries"

# print(series)

# # "convert to dict"
# print(dict(series))

# #conkatenera två serier

# s1 = pd.Series([1,2,3,4],['a','b','c','d'])
# s2 = pd.Series([2,4,6,8],['c', 'a', 'b', 'd'])

# print(s1+s2)
# # Tails visar sista och head visar första
# print(s1.head())
# print(s1.tail())

# #----------------------------------
# def mysquare(x):
#     return x**2

# print(s1.apply(mysquare))


# #Sortera

# print(s1.sort_index())
# print(s1.sort_values())


#DATAFRAME!!!!!!!!!!

# data = {
#     'SSN': [123,445,541,872],
#     'Name': ['Anna', 'Bob', 'John', 'Mike'],
#     'Age': [29, 43, 82, 23],
#     'Height': [176, 165, 187, 182],
#     'Gender': ['f', 'm', 'm', 'm']
# }
# #Skapar ett dataframe
# df = pd.DataFrame(data)

# #Sätter SSN som key index ( om man inte gör det så skapas automatiskt ett index 0,1,2 etc)
# df.set_index('SSN', inplace=True)

# print(df)

# def excel():
#     df = pd.read_csv("log.csv", header = None, names=['user', 'timestamp'])
#     df['timestamp'] = pd.to_datetime(df['timestamp'])
    
#     df['year'] = df['timestamp'].dt.year
#     df['month'] = df['timestamp'].dt.month
#     df['day'] = df['timestamp'].dt.day
#     df['time'] = df['timestamp'].dt.time
#     df['count'] = 1

#     file_path = r"C:\Users\Timot\Documents\Data Engineer 23\4.Programmering inom platform development\testfolder\log_info.xlsx"

#     log_info = openpyxl.Workbook()
#     sheet = log_info.active

#     sheet.append(['Användare','Inloggad', 'År', 'Månad','Dag', 'Tid', 'Antal'])

#     for _ , row in df.iterrows():
#         sheet.append(row.tolist())
    
#     log_info.save(file_path)


# def excel1():
#     # Read existing data from Excel file if it exists
#     file_path = r"C:\Users\Timot\Documents\Data Engineer 23\4.Programmering inom platform development\testfolder\log_info.xlsx"
#     try:
#         existing_df = pd.read_excel(file_path)
#     except FileNotFoundError:
#         existing_df = pd.DataFrame(columns=['user', 'timestamp', 'year', 'month', 'day', 'time', 'count'])

#     # Read CSV file and perform transformations
#     df = pd.read_csv("log.csv", header=None, names=['user', 'timestamp'])
#     df['timestamp'] = pd.to_datetime(df['timestamp'])
#     df['year'] = df['timestamp'].dt.year
#     df['month'] = df['timestamp'].dt.month
#     df['day'] = df['timestamp'].dt.day
#     df['time'] = df['timestamp'].dt.time
#     df['count'] = 1

#     # Append new data to existing data
#     combined_df = pd.concat([existing_df, df], ignore_index=True)

#     # Save the updated data to Excel file
#     with pd.ExcelWriter(file_path, engine='openpyxl') as writer:
#         combined_df.to_excel(writer, index=False, sheet_name='Sheet1')

# excel1()

def excel():
    # Read existing data from Excel file if it exists
    file_path = r"C:\Users\Timot\Documents\Data Engineer 23\4.Programmering inom platform development\testfolder\log_info.xlsx"
    try:
        existing_df = pd.read_excel(file_path)
    except FileNotFoundError:
        existing_df = pd.DataFrame(columns=['year', 'month', 'day', 'time', 'count'])

    # Read CSV file and perform transformations
    df = pd.read_csv("log.csv", header=None, names=['timestamp'])
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df['year'] = df['timestamp'].dt.year
    df['month'] = df['timestamp'].dt.month
    df['day'] = df['timestamp'].dt.day
    df['hour'] = df['timestamp'].dt.hour
    count = pd.read_csv("log.csv", header=None, names=['hour'])

    df['count'] = 1

    # Append new data to existing data
    combined_df = pd.concat([existing_df, df], ignore_index=True)

    # Save the updated data to Excel file
    with pd.ExcelWriter(file_path, engine='openpyxl') as writer:
        combined_df.to_excel(writer, index=False, sheet_name='Sheet1')




def excel1():
    # Read existing data from Excel file if it exists
    file_path = r"C:\Users\Timot\Documents\Data Engineer 23\4.Programmering inom platform development\testfolder\log_info.xlsx"
    try:
        existing_df = pd.read_excel(file_path)
    except FileNotFoundError:
        existing_df = pd.DataFrame(columns=['year', 'month', 'day', 'hour', 'count'])

    # Read CSV file and perform transformations
    df = pd.read_csv("log.csv", header=None, names=['timestamp'])
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df['year'] = df['timestamp'].dt.year
    df['month'] = df['timestamp'].dt.month
    df['day'] = df['timestamp'].dt.day
    df['hour'] = df['timestamp'].dt.hour

    # Count occurrences of each unique combination of 'year', 'month', 'day', 'hour'
    count_df = df.groupby(['year', 'month', 'day', 'hour']).size().reset_index(name='count')

    # Append new data to existing data
    combined_df = pd.concat([existing_df, count_df], ignore_index=True)

    # Save the updated data to Excel file
    with pd.ExcelWriter(file_path, engine='openpyxl') as writer:
        combined_df.to_excel(writer, index=False, sheet_name='Sheet1')

excel1()
