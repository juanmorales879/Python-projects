'''
File: filename.py
Author:
Description:  Filter a dataset - reference https://www.youtube.com/watch?v=2AFGPdNn4FM
'''
import pandas as pd

def main():

    movies = pd.read_csv("http://bit.ly/imdbratings")
    print("---- First Ten Lines ----")
    print(movies.head(10))  # print the first few lines

    actors = []
    for row in movies.itertuples():

        actorsList = row[6]
        actors.append (map(actorsList.encode('ascii','ignore'),actorsList))

    movies["actorsList"] = actorsList

    # create a python list of booleans - will be True if a row matches a criteria, false otherwise
    # to tell us which rows match a condition
    # example:  find movies with duration > 200

    booleans = []
    for length in movies.duration:
        if length >= 200:
            booleans.append(True)
        else:
            booleans.append(False)

    # booleans tells us which rows match the condition
    # convert list to pandas series

    is_long = pd.Series(booleans)

    print(is_long.head())

    print(movies[is_long])

    is_long = movies.duration >= 200  #condition replaces the for loop (series comparison, returns a series of T/F)

    print(movies[movies.duration >= 200])
    print("-----Crime Movies----")
    dfCrime = movies[movies.genre == "Crime"]

    print("------Column Names---")

    for col in dfCrime:
        print(col)

    print("------ALL Crime movies---")
    for row in dfCrime.itertuples():
        print(row.Index,row.genre, row.title,row.star_rating)

    print("----Crime Movies with rating =7.5---")

    dfHighlyRatedCrimeMovies = dfCrime[dfCrime.star_rating==7.5]

    for row in dfHighlyRatedCrimeMovies.itertuples():
         print(row.title, row.star_rating)
       #  print(row[0], row[1], row[2], row[3], row[4])  # can also access values from column index values

if __name__ == "__main__":
    main()
