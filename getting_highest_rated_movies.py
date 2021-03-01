# Analyze movies by weighted rating to determine its popularity

# IMDB Weighted Rating formula: (v/(v+m) * R) + (m/(m+v) * C)
#   where:
# v is the number of votes for the movie;
# m is the minimum votes required to be listed in the chart;
# R is the average rating of the movie; And
# C is the mean vote across the whole report
# We already have v(vote_count) and R (vote_average)

from data_preparation import get_merged_dataframes
from tabulate import tabulate

merged_dataframes = get_merged_dataframes()

# finding C (overall mean vote)
all_votes_mean = merged_dataframes['vote_average'].mean()

# finding minimum votes required to be listed on a chart
minimum_votes = merged_dataframes['vote_count'].quantile(0.9)


# calculating weighted rating
def weighted_rating(x, min_votes=minimum_votes, overall_average=all_votes_mean):
    votes_number = x['vote_count']
    votes_average = x['vote_average']
    return (votes_number/(votes_number + min_votes) * votes_average +
            (min_votes/(min_votes + votes_number) * overall_average))


# defining weighted rating under new 'score' column and returning top 10 movies with the highest rating
def get_top_10_movies():
    qualified_movies = merged_dataframes.copy().loc[merged_dataframes['vote_count'] >= minimum_votes]
    qualified_movies['score'] = qualified_movies.apply(lambda x: weighted_rating(x), axis=1)
    qualified_movies = qualified_movies.sort_values(by='score', ascending=False)
    return qualified_movies[['original_title', 'vote_count', 'vote_average', 'score']].head(10)

