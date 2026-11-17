movie_type= ["action", "comedy", "drama", "horror"]
movie_title= []

while True:
    question = input("do you know any movies? [yes/no]")

    if question.lower() == "yes":
        print("what is the genre? select from the list:")
        for x in movie_type:
            print(x)

        a_type = input("Genre:")

        title = input ("what is the title of the movie?")
        movie_title.append(title)
        continue
    else:
        print("Thank you.")
        break