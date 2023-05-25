print("Movies are here!")

CurrentMovies = {
    "Snow White": "11:00am",
    "Elf": "12:00pm",
    "Apple Documentary": "12:00pm",
    "The Office": "1:00pm",
    "Roblox": "5:00pm",
    "Lord of the Rings": "3:00pm",
    "Harry Potter": "1:00pm"
}

print("We are showing the following movies:")
movieList = []
for i in CurrentMovies:
    movieList.append(i)

print(movieList)

selectedMovie = input("What movie time do you want to know? ")
if CurrentMovies.get(selectedMovie) is None:
    print("You are an idiot. That's not a movie! Yuh fired.")
else:
    print(selectedMovie + " is being shown at " + CurrentMovies.get(selectedMovie))

