class Genres:
    def __init__(self, genres_data):
        self._id: int = genres_data['id']
        self._name: str = genres_data['name']

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    def __repr__(self):
        return str.format('{0}', self._name)