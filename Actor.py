class Actor:
    def __init__(self, cast):
        self._cast_id: int = cast['cast_id']
        self._character: str = cast['character']
        self._credit_id: str = cast['credit_id']
        self._gender: int = cast['gender']
        self._actor_id: int = cast['id']
        self._name: str = cast['name']

    def __repr__(self):
        return str.format('{0} - {1}', self._character, self._name)

    @property
    def name(self):
        return self._name