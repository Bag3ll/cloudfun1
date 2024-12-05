# Possible film ratings are "universal", "pg", "12", "12a", "15", "18"
film_rating = "12a"

# Use an if statement to check for "universal" rating
if film_rating == "universal":
    print("All age groups can watch this film.")
# Check if film rating is "pg"
elif film_rating == "pg":
    print("General viewing, but some scenes may be unsuitable for young children.")
# Check if film rating is "12" or "12a"
elif film_rating == "12" or film_rating == "12a":
    print("Films classified 12A and video works classified 12 contain material that is not generally suitable for children aged under 12.\n "
          "No one younger than 12 may see a 12A film in a cinema unless accompanied by an adult.")
# Check if film rating is "15"
elif film_rating == "15":
    print("No one younger than 15 may see a 15 film in a cinema.")
# Check if film rating is "18"
elif film_rating == "18":
    print("No one younger than 18 may see an 18 film in a cinema.")
# Else statement for invalid ratings
else:
    print("This is not a correct rating. Please use universal, pg, 12, 12a, 15, or 18.")

