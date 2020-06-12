# app_dev/services/basilica_service.py

import basilica

import os

from dotenv import load_dotenv

load_dotenv() # parse the .env file for environment variables

BASILICA_API_KEY = os.getenv("BASILICA_API_KEY")


connection = basilica.Connection(BASILICA_API_KEY)
print(type(connection)) 

if __name__ == "__main__":

    print(type(connection))
    sentences = ("Hello world!", "How are you?")
    embeddings = connection.embed_sentences(sentences)
    
    print(list(embeddings)) # [[0.8556405305862427, ...], ...]