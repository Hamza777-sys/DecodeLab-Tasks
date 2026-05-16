# =========================================================
# ADVANCED AI MOVIE RECOMMENDATION SYSTEM
# Project 3 - DecodeLabs Artificial Intelligence
# =========================================================

print("=================================================")
print("        ADVANCED AI RECOMMENDATION SYSTEM")
print("=================================================")

# Movie Database
movies = {
    "Interstellar": {
        "tags": ["Sci-Fi", "Space", "Adventure"],
        "year": 2014,
        "director": "Christopher Nolan",
        "cast": ["Matthew McConaughey", "Anne Hathaway"],
        "rating": 8.7,
        "description": "A team travels through space to save humanity."
    },

    "Inception": {
        "tags": ["Sci-Fi", "Mind", "Action"],
        "year": 2010,
        "director": "Christopher Nolan",
        "cast": ["Leonardo DiCaprio", "Joseph Gordon-Levitt"],
        "rating": 8.8,
        "description": "A thief enters dreams to steal secrets."
    },

    "Titanic": {
        "tags": ["Romance", "Drama"],
        "year": 1997,
        "director": "James Cameron",
        "cast": ["Leonardo DiCaprio", "Kate Winslet"],
        "rating": 7.9,
        "description": "A love story aboard the Titanic ship."
    },

    "John Wick": {
        "tags": ["Action", "Crime"],
        "year": 2014,
        "director": "Chad Stahelski",
        "cast": ["Keanu Reeves", "Ian McShane"],
        "rating": 7.4,
        "description": "A retired assassin seeks revenge."
    },

    "The Mask": {
        "tags": ["Comedy", "Fantasy"],
        "year": 1994,
        "director": "Chuck Russell",
        "cast": ["Jim Carrey", "Cameron Diaz"],
        "rating": 6.9,
        "description": "A magical mask transforms a bank clerk."
    },

    "Conjuring": {
        "tags": ["Horror", "Thriller"],
        "year": 2013,
        "director": "James Wan",
        "cast": ["Vera Farmiga", "Patrick Wilson"],
        "rating": 7.5,
        "description": "Paranormal investigators help a haunted family."
    },

    "Avengers": {
        "tags": ["Action", "Sci-Fi"],
        "year": 2012,
        "director": "Joss Whedon",
        "cast": ["Robert Downey Jr.", "Chris Evans"],
        "rating": 8.0,
        "description": "Superheroes unite to save the world."
    },

    "La La Land": {
        "tags": ["Romance", "Music"],
        "year": 2016,
        "director": "Damien Chazelle",
        "cast": ["Ryan Gosling", "Emma Stone"],
        "rating": 8.0,
        "description": "A musician and actress chase their dreams."
    },

    "Matrix": {
        "tags": ["Sci-Fi", "Action"],
        "year": 1999,
        "director": "Wachowski Sisters",
        "cast": ["Keanu Reeves", "Laurence Fishburne"],
        "rating": 8.7,
        "description": "A hacker discovers reality is a simulation."
    },

    "Home Alone": {
        "tags": ["Comedy", "Family"],
        "year": 1990,
        "director": "Chris Columbus",
        "cast": ["Macaulay Culkin", "Joe Pesci"],
        "rating": 7.7,
        "description": "A boy defends his home from burglars."
    },

    "Batman": {
        "tags": ["Action", "Adventure"],
        "year": 2022,
        "director": "Matt Reeves",
        "cast": ["Robert Pattinson", "Zoë Kravitz"],
        "rating": 7.8,
        "description": "Batman fights crime in Gotham City."
    },

    "Avatar": {
        "tags": ["Sci-Fi", "Adventure"],
        "year": 2009,
        "director": "James Cameron",
        "cast": ["Sam Worthington", "Zoe Saldana"],
        "rating": 7.9,
        "description": "Humans explore the alien world Pandora."
    },

    "Annabelle": {
        "tags": ["Horror", "Thriller"],
        "year": 2014,
        "director": "John R. Leonetti",
        "cast": ["Annabelle Wallis", "Ward Horton"],
        "rating": 5.4,
        "description": "A haunted doll spreads terror."
    },

    "Rush Hour": {
        "tags": ["Comedy", "Action"],
        "year": 1998,
        "director": "Brett Ratner",
        "cast": ["Jackie Chan", "Chris Tucker"],
        "rating": 7.0,
        "description": "Two detectives solve a kidnapping case."
    },

    "Me Before You": {
        "tags": ["Romance", "Drama"],
        "year": 2016,
        "director": "Thea Sharrock",
        "cast": ["Emilia Clarke", "Sam Claflin"],
        "rating": 7.4,
        "description": "A young woman cares for a disabled man."
    }
}

# Collect all available tags
all_tags = set()

for info in movies.values():
    for tag in info["tags"]:
        all_tags.add(tag)

# Display available interests
print("\nAvailable Interests:\n")

for tag in sorted(all_tags):
    print("-", tag)

# User Input
user_input = input(
    "\nEnter your interests separated by commas:\n"
)

# Convert user input into list
user_preferences = [
    item.strip().title()
    for item in user_input.split(",")
]

print("\nYour Interests:", user_preferences)

recommendations = []

# Recommendation Logic
for movie, info in movies.items():

    score = 0

    for interest in user_preferences:

        if interest in info["tags"]:
            score += 1

    # Add movie if at least one match exists
    if score > 0:
        recommendations.append((movie, score, info))

# Sort recommendations by score
recommendations.sort(
    key=lambda x: (x[1], x[2]["rating"]),
    reverse=True
)

# Display Results
print("\n=================================================")
print("                MOVIE RECOMMENDATIONS")
print("=================================================")

if recommendations:

    for movie, score, info in recommendations:

        print(f"\n🎬 Movie Name      : {movie}")
        print(f"🎯 Match Score     : {score}")
        print(f"📅 Release Year    : {info['year']}")
        print(f"🎬 Director        : {info['director']}")
        print(f"⭐ IMDb Rating     : {info['rating']}")
        print(f"🏷️ Categories      : {', '.join(info['tags'])}")
        print(f"👨 Main Cast       : {info['cast'][0]}, {info['cast'][1]}")
        print(f"📝 Description     : {info['description']}")
        print("-" * 50)

else:
    print("\n❌ No recommendations found.")
    print("Try different interests.")

print("\n=================================================")
print("      THANK YOU FOR USING THE AI SYSTEM")
print("=================================================")