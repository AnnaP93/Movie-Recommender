class ProductionCountries:
    def __init__(self, production_countries_data):
        self._iso_3166_1: int = production_countries_data['iso_3166_1']
        self._name: str = production_countries_data['name']

    @property
    def iso_3166_1(self):
        return self._iso_3166_1

    @property
    def name(self):
        return self._name

    def __repr__(self):
        return str.format('{0}', self._name)