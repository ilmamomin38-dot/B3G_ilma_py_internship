library={
    "B101":{
        "title":"python Basics",
        "author":"john smith",
        "copies":5
    },
    "B102":{
        "title":"Data Structures",
        "author":"jane doe",
        "copies":3
    },
    "B103":{
        "title":"Algorithms",
        "author":"Aman Gupta",
        "copies":2
    },
}

book_id="B102"

if library[book_id]["copies"]>0:
    library[book_id]["copies"]-=1
    print("Book issued successfully!")
else:
    print("no copies available")

    print("\nupdated library:")
    for book_id,details in library.items():
        print(book_id,":",details)