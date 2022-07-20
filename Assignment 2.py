# Assignment 2
# Declare a varible called; movie_title,pass empty string date type("")
# Number of movies # african movie count 0
# using while loop ask user to enter movie title,
# if movie title is george of the jungle or pretty woman or mission imposible
#increment movie count to 1 # print you like george of the jungle
# else if the movie title is ijele or zulu increment (AMC)to 1 and
#print you like (AM) else print you are not a movie lover

movie_title = ""
number_of_movies = 0
is_complete = True
african_movie_count = 0
movie_title1 = "george of the jungle"
movie_title2 = "pretty woman"
movie_title3 = "pission impossible"
movie_title4 = "ijele"
movie_title5 = "zulu"

while is_complete:
    movie_title = input("Enter movie title.")
    if (movie_title == movie_title1) or (movie_title == movie_title2) or (movie_title == movie_title3):
        print("you like american movies")
        number_of_movie = number_of_movies + 1
        
    elif(movie_title == movie_title4) or (movie_title == movie_title5):
            print("you like african movie")
            african_movie_count = african_movie_count + 1
    else:
        print("you are not a movie lover")
        is_complete = False
            
        
