# Movie Recommender
### The is a simple movie recommender program which tells you which movie to watch next if you have watched Planet Hulk and whichever movie has the highest similarity score will be recommended as the next movie to watch.

## Table of Contents
### Installation
### Usage
### How it works
### Credits

## Installation
### Assuming that you aleady have python installed on your pc if you dont please install it first before you continu.

### To use the application ,follow the steps below:

### 1. Go  to the command prompt

### 2. You need to install spacy using 
$ pip install spacey 

### 3. You need to install the pre-trained language for english
$ python -m spacy download en_core_web_md

### 4. Remember to make sure that all your files are in the same root directory

### 3. You can now run the code by using:
$ python watch.py


## Usage

### 1. After running the application, it will show you which movie to watch next if you have watched Planet hulk



## How it works
The movie() function in the watch_movie.py code uses the spacy to process the movie descriptions and the user's input description. It then calculates the similarity between the input description and each movie description using the similarity() method.

The movie with the highest similarity score is selected as the recommended movie, and the letter of the movie(e.g Movie A) and its decription are returned 

The movies.txt file contains a list of movies, each with a short description separated by a hyphen (-). The movie() function reads this file and processes each description using the language model.

If the movies.txt file does not exist, or if there is an error reading or decoding the file, the movie() function will print an error message and exit.



## Credits
### This project was created by Anisha Mandega.Feel free to contribute to this project by creating a pull request or reporting an issue
This project is licensed under the MIT License. See the LICENSE file for more details.
