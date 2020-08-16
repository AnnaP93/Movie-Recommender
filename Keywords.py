class Keywords:
    def __init__(self, keywords_data):
        self._id: int = keywords_data['id']
        self._name: str = keywords_data['name']

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    def __repr__(self):
        return str.format('{0}', self._name)