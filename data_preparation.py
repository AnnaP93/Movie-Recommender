from typing import List, Tuple
from Credit import Credit
from Crew import Crew
from Keywords import Keywords
from ProductionCompanies import ProductionCompanies
from ProductionCountries import ProductionCountries
from SpokenLanguages import SpokenLanguages
from read_input import read_input, read_input_df
from Actor import Actor
from Genres import Genres
import json


def get_movie_credits():
    reading_credits_data = read_input_df('tmdb_5000_credits.csv')

    for headline, single_credit in reading_credits_data.items():
        if headline == 'cast':
            reading_credits_data['cast'] = reading_credits_data['cast'].apply(lambda x: __fill_actors(x))

        if headline == 'crew':
            reading_credits_data['crew'] = reading_credits_data['crew'].apply(lambda x: __fill_crew(x))

    return reading_credits_data


def get_5000_movies_data():

    reading_5000_movie_data = read_input_df('tmdb_5000_movies.csv')

    for headline, single_movie_details in reading_5000_movie_data.items():
        if headline == 'genres':
            reading_5000_movie_data['genres'] = reading_5000_movie_data['genres'].apply(lambda x: __fill_genres(x))

        if headline == 'keywords':
            reading_5000_movie_data['keywords'] = reading_5000_movie_data['keywords'].apply(lambda x: __fill_keywords(x))

        if headline == 'production_companies':
            reading_5000_movie_data['production_companies'] = \
                reading_5000_movie_data['production_companies'].apply(lambda x: __fill_production_companies(x))

        if headline == 'production_countries':
            reading_5000_movie_data['production_countries'] = \
                reading_5000_movie_data['production_countries'].apply(lambda x: __fill_production_countries(x))

        if headline == 'spoken_languages':
            reading_5000_movie_data['spoken_languages'] = \
                reading_5000_movie_data['spoken_languages'].apply(lambda x: _fill_spoken_languages(x))

    return reading_5000_movie_data


def __fill_genres(genres_data: str) -> List[Genres]:
    all_genres: List[Genres] = []
    if genres_data == '[]':
        return 'NaN'
    genres_data = json.loads(genres_data)
    for genre in genres_data:
        all_genres.append(Genres(genre))
    return all_genres


def __fill_keywords(keywords_data: str) -> List[Keywords]:
    all_keywords: List[Keywords] = []
    if keywords_data == '[]':
        return 'NaN'
    else:
        keywords_data = json.loads(keywords_data)
    for keyword in keywords_data:
        all_keywords.append(Keywords(keyword))
    return all_keywords


def __fill_production_companies(production_companies_data):
    all_production_companies: List[ProductionCompanies] = []
    if production_companies_data == '[]':
        return 'NaN'
    production_companies_data = json.loads(production_companies_data)
    for production_company in production_companies_data:
        all_production_companies.append(ProductionCompanies(production_company))

    return all_production_companies


def __fill_production_countries(production_countries_data):

    all_production_countries: List[ProductionCountries] = []
    if production_countries_data == '[]':
        return 'NaN'
    production_countries_data = json.loads(production_countries_data)
    for production_country in production_countries_data:
        all_production_countries.append(ProductionCountries(production_country))

    return all_production_countries


def _fill_spoken_languages(languages_data):
    all_spoken_languages: List[SpokenLanguages] = []
    if languages_data == '[]':
        return 'NaN'
    languages_data = json.loads(languages_data)
    for each_language in languages_data:
        all_spoken_languages.append(SpokenLanguages(each_language))

    return all_spoken_languages


def __fill_actors(raw_actors: str) -> List[Actor]:
    actors: List[Actor] = []
    raw_actors = json.loads(raw_actors)
    for actor in raw_actors:
        actors.append(Actor(actor))

    return actors


def __fill_crew(raw_crew: str) -> List[Crew]:
    crew: List[Crew] = []
    raw_crew = json.loads(raw_crew)
    for crew_member in raw_crew:
        crew.append(Crew(crew_member))

    return crew


def get_all_titles() -> List[str]:
    credits_data: List[Credit] = get_movie_credits()
    list_of_titles = []
    for single_movie in credits_data:
        list_of_titles.append(single_movie.title)
    return list_of_titles


def get_merged_dataframes():
    left = get_5000_movies_data().set_index(['id'])
    right = get_movie_credits().set_index(['movie_id'])
    joined_dfs = left.join(right, lsuffix='TMDB 5000 Movies', rsuffix='TMDB 5000 Credits')
    return joined_dfs


def execute():

    print(get_merged_dataframes())

# execute()
