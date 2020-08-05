from typing import List
import json
from Actor import Actor
from Crew import Crew

class Credit:
    """
    input: movie_id, title, cast, crew
    Return:
        movie_id
        title
        actors (from 'cast')
        directors (from 'crew')
    """
    def __init__(self, movie_id, title, cast, crew):
        self._movie_id = movie_id
        self._title = title
        self._cast = cast
        self._crew = crew

    # def __init__(self, string_representation):
    #     temp = list(string_representation.split(','))
    #     for i, element in enumerate(temp):
    #         if '[]' in element:
    #             temp[i] = '," []'
    #             # string_representation = str(temp)
    #             string_representation = string_representation.replace('[]', '"[]"')
    #
    #         # if element == '[]':
    #         #     element = element.replace(('[]', ',"'))
    #
    #     self._movie_id: str = temp[0]
    #     self._title: str = temp[1]
    #     temp: List[str] = list(string_representation.split(',"'))
    #     actors: List[Actor] = []
    #     crew: List[Crew] = []
    #     if '""' in temp[1]:
    #         temp[1] = temp[1].replace('""', '"').rstrip('"')
    #         raw_actors = json.loads(temp[1])
    #         for actor in raw_actors:
    #             actors.append(Actor(actor))
    #         temp[2] = temp[2].replace('""', '"').rstrip('"')
    #         raw_crew = json.loads(temp[2])
    #         for crew_member in raw_crew:
    #             crew.append(Crew(crew_member))
    #
    #     else:
    #         temp[1] = temp[1].replace('"', '')
    #         temp[2] = temp[2].replace('""', '"').rstrip('"')
    #         raw_actors = json.loads(temp[2])
    #         for actor in raw_actors:
    #             actors.append(Actor(actor))
    #         temp[3] = temp[3].replace('""', '"').rstrip('"')
    #         raw_crew = json.loads(temp[3])
    #         for crew_member in raw_crew:
    #             crew.append(Crew(crew_member))
    #     self._cast: List[Actor] = actors
    #
    #     self._crew: List[Crew] = crew

    @property
    def movie_id(self):
        return self._movie_id

    @property
    def title(self):
        return self._title

    @property
    def cast(self):
        return self._cast

    @property
    def crew(self):
        return self._crew

    def __repr__(self):
        return '{0} : {1}, {2}, {3}'.format(self._movie_id, self._title, self._cast, self._crew)








