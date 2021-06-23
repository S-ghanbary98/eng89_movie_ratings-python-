# Movie Ratings!

while True:
    rating_choice = input("What rating would you like to know more about? \n Options include: \n universal \n pg \n 12 \n 15 \n 18 \n\n")
    if rating_choice == "universal":
        print("\neveryone can watch!")

    elif rating_choice == "pg":
        print("\nGeneral viewing, but some scenes may be unsuitable for young children!")

    elif rating_choice == "12":
        print("\nFilms classified 12A and video works classified 12 contain material that is not generally suitable for children aged under 12. No one younger than 12 may see a 12A film in a cinema unless accompanied by an adult.")

    elif rating_choice == "15":
        print("\nNo one younger than 15 may see a 15 film in a cinema!")

    elif rating_choice == "18":
        print("\nNo one younger than 18 may see an 18 film in a cinema!")

    elif rating_choice == "exit":
        break
    else:
        print("Invalid option, Choose another")


