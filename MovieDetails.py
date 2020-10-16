from typing import List
import datetime


class MovieDetails:
    def __init__(self, budget, genres, homepage, id, keywords, original_language, original_title, overview, popularity,
                 production_companies, production_countries, release_date, revenue, runtime, spoken_languages, status,
                 tagline, title, vote_average, vote_count):

        self._budget: int = budget
        self._genres: List[str] = genres
        self._homepage: str = homepage
        self._id: str = id
        self._keywords: List[str] = keywords
        self._original_language: str = original_language
        self._original_title: str = original_title
        self._overview: str = overview
        self._popularity: float = popularity
        self._production_companies: List[str] = production_companies
        self._production_countries: List[str] = production_countries
        self._release_date: datetime.date = release_date
        self._revenue: int = revenue
        self._runtime: int = runtime
        self._spoken_languages: List[str] = spoken_languages
        self._status: str = status
        self._tagline: str = tagline
        self._title: str = title
        self._vote_average: float = vote_average
        self._vote_count: int = vote_count

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
    def release_date(self):
        return self._release_date

    @property
    def revenue(self):
        return self._revenue

    @property
    def runtime(self):
        return self._runtime

    @property
    def spoken_languages(self):
        return self._spoken_languages

    @property
    def status(self):
        return self._status

    @property
    def title(self):
        return self._title

    @property
    def vote_average(self):
        return self._vote_average

    @property
    def vote_count(self):
        return self._vote_count

    def __repr__(self):
        return '{0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11}, {12}, {13}, {14}, {15}, {16}, {17}, {18}'\
            .format(self._budget, self._genres, self._homepage, self._id, self._keywords,
                    self._original_language, self._original_title, self._overview, self._popularity, self._production_companies,
                    self._production_countries, self._release_date, self._revenue, self._runtime, self._spoken_languages,
                    self._status, self._title, self._vote_average, self._vote_count)