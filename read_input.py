import os
import pandas as pd


def read_input_df(file_name):
    reading_current_directory = os.getcwd()
    data_folder = reading_current_directory + '/input/'
    absolute_file_name = data_folder + file_name
    df_credits = pd.read_csv(absolute_file_name)
    return df_credits


def read_input(file_name: str) -> [str]:
    reading_current_directory = os.getcwd()
    data_folder = reading_current_directory + '/input/'
    absolute_file_name = data_folder + file_name
    file = open(absolute_file_name)
    read_file = file.read()
    return convert_to_list(read_file)


def convert_to_list(entry_data):
    li = list(entry_data.split('\n'))
    return li

