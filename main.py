from typing import List, Tuple
from data_preparation import get_movie_credits, get_merged_dataframes


def get_characters_actors_popularity():

    all_data = get_merged_dataframes()
    for index, each_row in all_data.iterrows():
        print('The actors played in {0} include: {1}. The movie popularity is {2}.'
              .format(each_row['original_title'], each_row['cast'], each_row['popularity']))


def get_crew_members_production_companies():
    all_data = get_merged_dataframes()
    for index, each_row in all_data.iterrows():
        print('The crew members worked on {0} include: {1}. The production companies are: {2}'
              .format(each_row['original_title'], each_row['crew'], each_row['production_companies']))


def execute():

    get_characters_actors_popularity()
    # get_crew_members_production_companies()


execute()




















