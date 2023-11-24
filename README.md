# Organo-A-Retrieval-Based-Chatbot

## Overview
While my initial project deals with rule based chatbot, in this project I developed retrieval based chatbot. As the retrieval based chatbot needs more data to process, hereby scraped the data using beautiful soup from the wikipedia anout the Human Organs.

## Technical Aspect

Machine Learning :
1) Created the sentence list with the scraped data.
2) Once the user feeds the Input, appends that to the existing sentence list.
3) Hereby I have used Tf-Idf Vecorizer for the vector representation of list.
4) With the generated vectors, found the similarities based on cosine similarity approach.
5) Fetch the top 1 similar response and return it back to the UI

Website:
Build a website using a Flask. Deployed the website in Heroku with all the necessary packages mentioned in the required files.

Demo:
https://organos-retrieval.herokuapp.com/ 

![image](https://user-images.githubusercontent.com/105039765/179507598-bb9f4df8-7b3d-400d-97ec-f2b5aeb8f352.png)




