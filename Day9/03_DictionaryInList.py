travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]
# 🚨 Do NOT change the code above

# to be added to the travel_log. 👇


def add_new_country(country, num_visits, cities):
    travel_log.append({"country": country, "visits": num_visits, "cities": cities})


def add_new_country_contructor(country, num_visits, cities):
    new_country = {}
    new_country["country"] = country
    new_country["visits"] = num_visits
    new_country["cities"] = cities
    travel_log.append(new_country)


# 🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
