from typing import List, Tuple
from data_preparation import get_merged_dataframes, get_characters_actors_popularity, get_crew_members_production_companies
from demographic_filtering import get_top_10_movies
from tabulate import tabulate


def get_actors_popularity_of_top_10():
    actors_data = get_characters_actors_popularity()
    top_10_data = get_top_10_movies()
    for index in top_10_data.index:
        row = actors_data.loc[index]
        print('Actors played in {0} include: {1}. The popularity of the movie is {2}'
              .format(row.original_title, row.cast, row.popularity))


def get_crew_prod_companies_of_top_10():
    crew_data = get_crew_members_production_companies()
    top_10_data = get_top_10_movies()
    for index in top_10_data.index:
        row = crew_data.loc[index]
        print('The crew that worked on {0} include: {1}. The production companies are: {2}'
              .format(row.original_title, row.crew, row.production_companies))


def execute():

    print(tabulate(get_top_10_movies()[['original_title', 'vote_count', 'vote_average', 'score']].head(10),
                   headers='keys', tablefmt='psql'))

    print('The list of actors and their characters for each of the top-10 movies, plus movie popularity rate:')
    get_actors_popularity_of_top_10()
    print()

    print('The list of crew members who worked on each of top-10 movies and the respective production companies: ')
    get_crew_prod_companies_of_top_10()


execute()




















