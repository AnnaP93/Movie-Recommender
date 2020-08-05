class MovieDetails:
    def __init__(self, specific_movie):
        self._budget: str = specific_movie['budget']
        self._genres: str = specific_movie['genres']
        self._homepage: str = specific_movie['homepage']
        self._id: str = specific_movie['id']
        self._keywords: str = specific_movie['keywords']
        self._original_language: str = specific_movie['original_language']
        self._original_title: str = specific_movie['original_title']
        self._overview: str = specific_movie['overview']
        self._popularity: str = specific_movie['popularity']
        self._production_companies: str = specific_movie['production_companies']
        self._production_countries: str = specific_movie['production_countries']
        self._release_date: str = specific_movie['release_date']
        self._revenue: str = specific_movie['revenue']
        self._runtime: str = specific_movie['runtime']
        self._spoken_languages: str = specific_movie['spoken_languages']
        self._status: str = specific_movie['status']
        self._tagline: str = specific_movie['tagline']
        self._title: str = specific_movie['title']
        self._vote_average: str = specific_movie['vote_average']
        self.vote_count: str = specific_movie['vote_count']

    @property
    def budget(self):
        return self._budget

    @property
    def genres(self):
        return self._genres

    @property
    def id(self):
        return self._id

    @property
    def keywords(self):
        return self._keywords

    @property
    def popularity(self):
        return self._popularity

    @property
    def production_companies(self):
        return self._production_companies

    @property
    def production_countries(self):
        return self._production_countries

    @property
    def revenue(self):
        return self._revenue

    @property
    def runtime(self):
        return self._runtime

    @property
    def title(self):
        return self._title

    @property
    def vote_average(self):
        return self._vote_average

    @property
    def vote_count(self):
        return self._vote_count