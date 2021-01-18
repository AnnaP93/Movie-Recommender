# 1. Get all movie_ids and titles
# 2. Get actors from cast
# 3. Get directors from crew
# 4. Merge credits with movies files
from typing import List, Tuple


from Credit import Credit
from Crew import Crew
from Keywords import Keywords
from ProductionCompanies import ProductionCompanies
from ProductionCountries import ProductionCountries
from SpokenLanguages import SpokenLanguages
from read_input import read_input
from Actor import Actor
from MovieDetails import MovieDetails
from Genres import Genres
import json
from datetime import date


def get_movie_credits() -> List[Credit]:
    reading_credits_data = read_input('tmdb_5000_credits.csv')
    del reading_credits_data[-1]
    all_credits: List[Credit] = []
    for raw_credit in reading_credits_data[1:]:
        movie_id: str
        title: str
        raw_credit = __sanitize_credit(raw_credit)

        cast_start_index = raw_credit.index('[')
        id_and_title = raw_credit[0:cast_start_index]
        id_index: int = id_and_title.index(',')
        movie_id: str = id_and_title[0:id_index]
        title: str = id_and_title[id_index:cast_start_index]
        if '"' in title:
            title: str = title.strip(',"')
        cast_end_index: int = raw_credit.index(']')
        cast_data: str = raw_credit[cast_start_index:cast_end_index+1]
        crew_start_index = raw_credit.index('[', cast_start_index+1, None)
        crew_end_index = raw_credit.index(']', cast_end_index+1, None)
        crew_data = raw_credit[crew_start_index:crew_end_index+1]
        cast: List[Actor] = __fill_actors(cast_data)
        crew: List[Crew] = __fill_crew(crew_data)

        credit = Credit(movie_id, title, cast, crew)
        all_credits.append(credit)

    return all_credits


def get_5000_movies_data() -> List[MovieDetails]:
    reading_5000_movie_data = read_input('tmdb_5000_movies.csv')
    all_movie_details: List[MovieDetails] = []
    for single_movie_details in reading_5000_movie_data[1:10]:
        single_movie_details = __sanitize_movies_data(single_movie_details)
        budget: int
        genres: List[Genres]
        homepage: str
        id: int
        keywords: List[Keywords]
        original_title: str
        overview: str
        popularity: float
        production_companies: List[ProductionCompanies]
        production_countries: List[ProductionCountries]
        # release_date: date
        release_date: str
        revenue: int
        runtime: int
        spoken_languages: List[SpokenLanguages]
        status: str
        tagline: str
        title: str
        vote_average: float
        vote_count: int

        budget_index = single_movie_details.index(',')
        budget = int(single_movie_details[0:budget_index])
        genres_index = single_movie_details.index(']')
        raw_genres = single_movie_details[budget_index+1:genres_index+1]
        genres: List[Genres] = __fill_genres(raw_genres)
        homepage_start_index = single_movie_details.index(',', genres_index, None)
        homepage_end_index = single_movie_details.index(',', homepage_start_index+1, None)
        homepage = single_movie_details[homepage_start_index:homepage_end_index].strip(',')
        id_end_index = single_movie_details.index(',', homepage_end_index+1, None)
        id = int(single_movie_details[homepage_end_index+1:id_end_index])
        keywords_end_index = single_movie_details.index(']', id_end_index, None)
        raw_keywords = single_movie_details[id_end_index+1:keywords_end_index+1].strip('"')
        keywords = __fill_keywords(raw_keywords)
        original_language_start_index = single_movie_details.index(',', keywords_end_index, None)
        original_language_end_index = single_movie_details.index(',', original_language_start_index+1, None)
        original_language = single_movie_details[original_language_start_index+1:original_language_end_index]
        original_title_end_index = single_movie_details.index(',', original_language_end_index+1, None)
        original_title = single_movie_details[original_language_end_index+1:original_title_end_index]
        overview_start_index = single_movie_details.index('"', original_title_end_index, None)
        overview_end_index = single_movie_details.index('"', overview_start_index+1, None)
        overview = single_movie_details[overview_start_index+1:overview_end_index]
        popularity_start_index = single_movie_details.index(',', overview_end_index, None)
        popularity_end_idex = single_movie_details.index(',', popularity_start_index+1, None)
        popularity = single_movie_details[overview_end_index+2:popularity_end_idex]
        production_companies_start_index = single_movie_details.index('[', popularity_end_idex, None)
        production_companies_end_index = single_movie_details.index(']', popularity_start_index, None)
        raw_production_companies = single_movie_details[production_companies_start_index:production_companies_end_index+1]
        production_companies = __fill_production_companies(raw_production_companies)
        production_countries_start_index = single_movie_details.index('[', production_companies_end_index, None)
        production_countries_end_index = single_movie_details.index(']', production_countries_start_index, None)
        raw_production_countries = single_movie_details[production_countries_start_index:production_countries_end_index+1]
        production_countries = __fill_production_countries(raw_production_countries)
        release_date_start_index = single_movie_details.index(',', production_countries_end_index, None)
        release_date_end_index = single_movie_details.index(',', release_date_start_index+1, None)
        release_date = single_movie_details[release_date_start_index+1:release_date_end_index]
        revenue_end_index = single_movie_details.index(',', release_date_end_index+1)
        revenue = single_movie_details[release_date_end_index+1:revenue_end_index]
        runtime_end_index = single_movie_details.index(',', revenue_end_index+1, None)
        runtime = single_movie_details[revenue_end_index+1: runtime_end_index]
        spoken_languages_start_index = single_movie_details.index('[', runtime_end_index, None)
        spoken_languages_end_index = single_movie_details.index(']', runtime_end_index, None)
        raw_spoken_languages = single_movie_details[spoken_languages_start_index:spoken_languages_end_index+1]
        spoken_languages = _fill_spoken_languages(raw_spoken_languages)
        status_start_index = single_movie_details.index(',', spoken_languages_end_index, None)
        status_end_index = single_movie_details.index(',', status_start_index+1, None)
        status = single_movie_details[status_start_index+1:status_end_index]
        tagline_end_index = single_movie_details.index(',', status_end_index+1, None)
        tagline = single_movie_details[status_end_index+1:tagline_end_index]
        title_end_index = single_movie_details.index(',', tagline_end_index+1, None)
        title = single_movie_details[tagline_end_index+1:title_end_index]
        vote_average_end_index = single_movie_details.index(',', title_end_index+1, None)
        vote_average = float(single_movie_details[title_end_index+1:vote_average_end_index])
        vote_count = single_movie_details[vote_average_end_index+1:]

        movie_characteristics = MovieDetails(budget, genres, homepage, id, keywords, original_language,
                                             original_title, overview, popularity, production_companies,
                                             production_countries, release_date, revenue, runtime, spoken_languages,
                                             status, tagline, title, vote_average, vote_count)
        all_movie_details.append(movie_characteristics)

    return all_movie_details


def __sanitize_movies_data(raw_movie: str) -> str:
    raw_movie = raw_movie.replace('"At the end of the world, the adventure begins."',
                                  'At the end of the world the adventure begins.')
    raw_movie = raw_movie.replace('"Lost in our world, found in another."', 'Lost in our world found in another.')
    return raw_movie

def __fill_genres(genres_data: str) -> List[Genres]:
    all_genres: List[Genres] = []
    genres_data = genres_data.replace('""', '"').strip('"')
    genres_data = json.loads(genres_data)
    for genre in genres_data:
        all_genres.append(Genres(genre))
    return all_genres


def __fill_keywords(keywords_data: str) -> List[Keywords]:
    all_keywords: List[Keywords] = []
    keywords_data = keywords_data.replace('""', '"')
    keywords_data = json.loads(keywords_data)
    for keyword in keywords_data:
        all_keywords.append(Keywords(keyword))
    return all_keywords


def __fill_production_companies(production_companies_data):
    all_production_companies: List[ProductionCompanies] = []
    production_companies_data = production_companies_data.replace('""', '"')
    production_companies_data = json.loads(production_companies_data)
    for production_company in production_companies_data:
        all_production_companies.append(ProductionCompanies(production_company))

    return all_production_companies


def __fill_production_countries(production_countries_data):

    all_production_countries: List[ProductionCountries] = []
    production_countries_data = production_countries_data.replace('""', '"')
    production_countries_data = json.loads(production_countries_data)
    for production_country in production_countries_data:
        all_production_countries.append(ProductionCountries(production_country))

    return all_production_countries


def _fill_spoken_languages(languages_data):
    all_spoken_languages: List[SpokenLanguages] = []
    languages_data = languages_data.replace('""', '"')
    languages_data = json.loads(languages_data)
    for each_language in languages_data:
        all_spoken_languages.append(SpokenLanguages(each_language))

    return all_spoken_languages


def __sanitize_credit(raw_credit: str) -> str:
    raw_credit = raw_credit.replace('[]', '"[]"')

    # Edge case when name abbreviation is incorrect
    raw_credit = raw_credit.replace('J.J,', 'J.J.')

    # Edge case when [] included in cast json code
    raw_credit = raw_credit.replace('[Singing voice]', 'Singing voice')
    raw_credit = raw_credit.replace('[Cameo]', 'Cameo')
    raw_credit = raw_credit.replace('[cameo]', 'cameo')
    raw_credit = raw_credit.replace('[REC]²', 'REC 2')
    raw_credit = raw_credit.replace('[REC]', 'REC')

    return raw_credit


def __fill_actors(raw_actors: str) -> List[Actor]:
    actors: List[Actor] = []
    if '""' in raw_actors:
        raw_actors = raw_actors.replace('""', '"').rstrip('"')
        raw_actors = json.loads(raw_actors)
        for actor in raw_actors:
            actors.append(Actor(actor))

    return actors


def __fill_crew(raw_crew: str) -> List[Crew]:
    crew: List[Crew] = []
    if '""' in raw_crew:
        raw_crew = raw_crew.replace('""', '"').rstrip('"')
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


def execute():

    # all_credits = get_movie_credits()
    # for unique_credit in all_credits:
    #     print(unique_credit)

    print(get_5000_movies_data())

    # print(get_all_titles())


execute()