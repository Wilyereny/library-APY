import uvicorn
import psycopg2
import logging
from getMongoDB import getDatabase
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel



#------------------------------/\ FastAPI /\-------------------------------------#
platts = FastAPI()
#http://127.0.0.1:8000

#------------------------------/\ Schemes /\-------------------------------------#
class book(BaseModel):
    _id:Optional[str]
    Title:str
    Autor:str
    Genero:str
    Synopsys:str
    Year: int
    Pages: int
    ISBN: int
    Editorial:str

    
def bookEntity(book) -> dict:
    return {
            "_id":Optional[str(book["_id"])],
            "Title":book["Title"],
            "Autor":book["Autor"],
            "Genero":book["Genero"],
            "Synopsys":book["Synopsys"],
            "Year":book["Year"],
            "Pages": book["Pages"],
            "ISBN": book["ISBN"],
            "Editorial":book["Editorial"]
    }
    
def booksEntity(entity) -> list:
    return [bookEntity(book) for book in entity]


#------------------------------/\  Routes /\-------------------------------------#
@platts.get("/books")
def find_all_books():   
    try:
        # Open a cursor to perform database operations
        dbname = getDatabase("Platts")
        plattsCollection = dbname["Platts"]
        plattsData = plattsCollection.find()
        #return booksEntity(plattsData)
                
    except (Exception, psycopg2.Error) as error:
        logging.error(error)

    finally:
        # closing database connection.
        logging.info("Connection is closed")

    #return booksEntity(plattsData)
    return "Hola Mundo"

@platts.get("/books/{id}")
def find_book(id):
    try:
        # Open a cursor to perform database operations
        dbname = getDatabase("Platts")
        plattsCollection = dbname["Platts"]
        plattsData = plattsCollection.find_one(id)
        return booksEntity(plattsData)
                
    except (Exception, psycopg2.Error) as error:
        logging.error(error)

    finally:
        # closing database connection.
        logging.info("Connection is closed")

    return bookEntity(plattsData)


    
