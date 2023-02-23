programming_dict = {
    "Bug": "An error in a program that prevents the program from running as expected",
    "Function": "A piece of code that can be callad",
    "Loop": "An action doing something over and over again"
}

# retrieving
print(programming_dict["Loop"])

# Adding
programming_dict["int"] = "A whole number"
print(programming_dict)

# Loop through keys in dictionary
for key in programming_dict:
    print(key)  # prints keys only
    print(programming_dict[key])  # prints values

# ------------------------------------------------
# Nesting -> normal dict
capitals = {
    "France": "Paris",
    "Germany": "Barlin"
}

# Nesting list in dict
Travellog = {
    "France": ["Paris", "Lille", "Marseille"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"]
}

# Nesting dict in dict
travel_log = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Marseille"],
        "total_visits": 12
    },
    "Germany": {
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 25
    }
}

# Nesting dict in list
travel_log_list = [
    {
        "Country": "France",
        "cities_visited": ["Paris", "Lille", "Marseille"],
        "total_visits": 12
    },
    {
        "Country": "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 25
    }
]
