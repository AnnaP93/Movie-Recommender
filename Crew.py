class Crew:
    def __init__(self, crew):
        self._credit_id: str = crew['credit_id']
        self._department: str = crew['department']
        self._gender: int = crew['gender']
        self._id: int = crew['id']
        self._job: str = crew['job']
        self._name: str = crew['name']

    def __repr__(self):
        return str.format('{0} - {1}', self._job, self._name)

    @property
    def name(self):
        return self._name

    @property
    def job(self):
        return self._job