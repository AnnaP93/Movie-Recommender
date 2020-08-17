from typing import List, Tuple
from Actor import Actor
from data_preparation import get_movie_credits


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
    actors = []
    # test: List[str, List[str]] = []
    # t_actors: List[str] = ["Sam", "Zoe"]
    # test.append(("Avatar", t_actors))
    for credit in credits_data:
        only_cast: List[Actor] = credit.cast
        for actor_characteristic in only_cast:
            only_actors = actor_characteristic.name
            actors.append(only_actors)
        print(str.format("The actors played in {0} are {1}", credit.title, actors))
        actors = []

    return actors


def execute():

    print(get_actors())


execute()




















