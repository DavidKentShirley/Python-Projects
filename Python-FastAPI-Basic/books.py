from fastapi import FastAPI

app = FastAPI()

BOOKS = [
    {'title': 'Title One', 'author': 'Author One', 'category': 'science'},
    {'title': 'Title Two', 'author': 'Author Two', 'category': 'science'},
    {'title': 'Title Three', 'author': 'Author Three', 'category': 'history'},
    {'title': 'Title Four', 'author': 'Author Four', 'category': 'math'},
    {'title': 'Title Five', 'author': 'Author Five', 'category': 'math'},
    {'title': 'Title Six', 'author': 'Author Two', 'category': 'math'}
]

# Basic demo of creating an api endpoint // making a usable link www.xxxxx.com/api-endpoint retuns {'message': 'Hello David!'}
@app.get("/api-endpoint")
async def first_api():
    return {'message': 'Hello David!'}

# Pathing with return of the BOOKS dict
@app.get("/books")
async def read_all_books():
    return BOOKS

# Path paramaters to return a specific book based on title
@app.get("/books/{book_title}")
async def read_book(book_title: str):
    for book in BOOKS: 
        if book.get('title').casefold() == book_title.casefold():
            return book


# Query Paramaters
@app.get("/books/")
async def read_category_by_query(category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return

# Query and path Paramaters
@app.get("books/{book_author}/")
async def read_author_category_by_query(book_author: str, category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('author').casefold() == book_author.casefold() and book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return