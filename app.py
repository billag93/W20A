import dbcreds
import mariadb

def makePosts():
    conn = mariadb.connect(user = dbcreds.user, password = dbcreds.password, host = dbcreds.host, port = dbcreds.port, database = dbcreds.database)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO blog_post (username, content, id) VALUES(?, ?, NULL)", [username, newPost])
    conn.commit()
    cursor.close()
    conn.close()

def seeAllPosts():
    conn = mariadb.connect(user = dbcreds.user, password = dbcreds.password, host = dbcreds.host, port = dbcreds.port, database = dbcreds.database)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM blog_post")
    rows = cursor.fetchall()
    print(rows)
    cursor.close()
    conn.close()

while True: 
    username = input("Enter your username here: ")
    print("You have the following options. Enter 1 to make a post, and enter 2 to see all posts")
    Option = input("Enter your option here: ")

    if (Option == "1"):
        newPost = input("Enter your blogpost here: ")
        makePosts()

    elif (Option == "2"):
        seeAllPosts()