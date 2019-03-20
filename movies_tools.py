
# Part 1.  import statements needed
import csv
from flask import Flask

# Commit to remote server - GitHub
# work in virtual enviornment

#Part 2.   open cleaned data set, movies_cleaned.csv

#Part 3.   In your movies_tools.py file, define a class Movie that accepts as constructor
#input one row of the movies_clean.csv file (in whatever format you think is appropriate for you).


# how is html interacting with python here? within this route?

# in the route you will define the path
# you will then define a (unique) function with a return value
# the return value will have the html tag, the defaut is a p tag,
# ex. "<h1> hello </h1>"

#Part 4.   cleate routes with functions


#creating class strategie
    #fuction should iterate through first five rows and return a variable
    #that represents these rows

    #the route /movies/ratings/
        #should take variable and return each of them
        # with correcrt format to console - Movie Title | IMBD rating
        # use "{} | {}".format(vartittle, var_rating)

if __name__ == "__main__": # Still only want the application to RUN if we are running this file specifically, and not using functions inside it as tools for something else
    app.run() # This is what causes an app to work at URLs that start with http://localhost:5000/ (AKA http://127.0.0.1:5000/, they mean the exact same thing) -- on your own computer -- when you run the program with "runserver" at the end, as directed. See HW 1!
