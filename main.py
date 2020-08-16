# 1. Get all movie_ids and titles
# 2. Get actors from cast
# 3. Get directors from crew
# 4. Merge credits with movies files
from typing import List, Tuple

from Credit import Credit
from Crew import Crew
from Keywords import Keywords
from read_input import read_input
from Actor import Actor
from MovieDetails import MovieDetails
from Genres import Genres
import json


def get_movie_credits() -> List[Credit]:
    reading_credits_data = read_input('tmdb_5000_credits.csv')
    all_credits: List[Credit] = []
    for raw_credit in reading_credits_data[1:4804]:
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


def get_5000_movies_data():
    reading_5000_movie_data = read_input('tmdb_5000_movies.csv')
    all_movie_details: List[MovieDetails] = []
    for single_movie_details in reading_5000_movie_data[1:10]:
        budget: int
        genres: List[str]
        homepage: str
        id: int
        keywords: List[str]
        original_title: str
        overview: str
        popularity: float
        production_companies: List[str]
        production_countries: List[str]
        revenue: int
        runtime: int
        tagline: str
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
        keywords_end_index = single_movie_details.index(']', id_end_index)
        raw_keywords = single_movie_details[id_end_index+1:keywords_end_index+1].strip('"')
        keywords: List[Genres] = __fill_keywords(raw_keywords)




        movie_characteristics = MovieDetails(budget, genres, homepage, id, keywords, original_title)
        all_movie_details.append(movie_characteristics)

    return all_movie_details


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


# def __sanitize_title(temp: str, raw_credit: str) -> str:
#     if '"' in temp[1]:
#         adjusted_separation = list(raw_credit.split(',"'))
#         adjusted_separation[1] = adjusted_separation[1].replace('"', '')
#     return adjusted_separation


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


def get_actors() -> List[Tuple[str, List[str]]]:
    """
    This method returns the list of unique actors' names in each movie.
    :return:
    str(title) from Credit & list(str(name)) from Credit

    List[str, List[str]]
    The actors played in Avatar are: Sam Worthington, Zoe Saldana, etc.
    The actors played in Pirates of the Caribbean are: Johnny Depp, Sam Worthington
    """
    credits_data = get_movie_credits()
    cast = []
    actors = []
    # test: List[str, List[str]] = []
    # t_actors: List[str] = ["Sam", "Zoe"]
    # test.append(("Avatar", t_actors))
    for credit in credits_data:
        only_cast: List[Actor] = credit.cast
        # cast.append(only_cast)
        for actor_characteristic in only_cast:
            only_actors = actor_characteristic.name
            actors.append(only_actors)
        print(str.format("The actors played in {0} are {1}", credit.title, actors))
        actors = []

    return actors


def execute():

    # all_credits = get_movie_credits()
    # for unique_credit in all_credits:
    #     print(unique_credit)

    #print(get_5000_movies_data())

    # print(get_all_titles())

    print(get_actors())


execute()



# Tuple - NON Iterable
# Anna, Popovych - single record
# Viktor, Deineka - single record
# person1 = { "Anna", "Popovych" }
# person2 = { "Viktor", "Deineka" }


# LIST - Iterable
# (Anna, Popovych), (Viktor, Deineka), (Anna, Smith), (Anna Mykhailovska), (Anna Popovych) - many records
# persons = List[Tuple[str, str]]
# persons.Append({"Anna", "Popovych"})
# persons.Append({"Viktor", "Deineka"})
# persons.Append({"Anna", "Smith"})
# persons.Append({"Anna", "Mykhailovska"})
# persons.Append({"Anna", "Popovych"})

# Dictionary - Iterable
# (Anna, Popovych), (Viktor, Deineka) - Collection of unique keys with their values
# persons = Dictionary[str, str]
# persons["Anna"] = "Popovych"
# persons["Viktor"] = "Deineka"
# persons["Anna"] = "Smith" - ERROR



















