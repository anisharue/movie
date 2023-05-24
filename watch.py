# importing libraries
import spacy
from wasabi import Printer

nlp = spacy.load("en_core_web_md")
printer = Printer()


# defined a movie function
def movie(description):

    # used a try accept block
    while True:
        try:

            # opened movies.txt  and read from it
            with open("movies.txt", "r")as file:

                # read the lines in the movie.txt snd assigned it to a variable
                movie_description = file.readlines()

                # used the nlp function to apply the language model to the text
                # converted the descriptions to lowercase using the lower function
                description1 = nlp(description.lower())

                # initialized variables
                highest_similarity = -1
                recommended_movie = ""

                # used a for loop to iterate through the movie descriptions read from the file
                for movies in movie_description:

                    # used nlp to apply the language learning model to  the text
                    movie_doc = nlp(movies.lower())

                    # calculate similarity between the input and each movie in the txt file
                    similarity = description1.similarity(movie_doc)

                    # used an if statement and the  greater than logical operator to check
                    # if the similarity is higher than the current highest similarity, and if it is true
                    # the variables are updated
                    if similarity > highest_similarity:
                        highest_similarity = similarity

                        # used the split function to split the movie by the hyphen and select the first part which
                        # is the movie name
                        recommended_movie = movies

                return f"\n{recommended_movie}"
        except FileNotFoundError:
            print("\n movies.txt file not exist")
            exit()
        except (IOError, OSError):
            print("\nError reading file")
            exit()
        except UnicodeDecodeError:
            print("\nError decoding file")
            exit()


description = """Will he save
their world or destroy it? When the Hulk becomes too dangerous for the
Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a
planet where the Hulk can live in peace. Unfortunately, Hulk land on the
planet Sakaar where he is sold into slavery and trained as a gladiator"""
next_movie = movie(description)
printer.text(f"Next movie recommendation: {next_movie}", color="blue")

