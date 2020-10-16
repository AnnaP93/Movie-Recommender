class SpokenLanguages:
    def __init__(self, spoken_languages_data):
        self._iso_639_1: str = spoken_languages_data['iso_639_1']
        self._name: str = spoken_languages_data['name']

    @property
    def iso_639_1(self):
        return self._iso_639_1

    @property
    def name(self):
        return self._name

    def __repr__(self):
        return str.format('{0}', self._name)