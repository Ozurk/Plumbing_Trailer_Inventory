import pandas as pd
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# TODO create a user-friendly way to add and subtract supplies using the terminal
# todo create a user-friendly way to navigate through the spreadsheet using the terminal
dataframe = pd.read_excel("workbooks//trailer.inventory.xlsx")


class Team_Member:
    def __init__(self, first_name, last_name):
        first_name = input("please enter your first name")
        last_name = input("please enter your last name")


class Working_Dataframe:
    df_copy = dataframe.copy()
    def __init__(self):
        pass
    def view(self, ):


print(Working_Dataframe.df_copy.info)
