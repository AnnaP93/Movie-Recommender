class ProductionCompanies:
    def __init__(self, production_companies_data):
        self._id: int = production_companies_data['id']
        self._name: str = production_companies_data['name']

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    def __repr__(self):
        return str.format('{0}', self._name)