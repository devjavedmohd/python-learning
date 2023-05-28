# Nesting
capitals = {
    "France": "Paris",
    "India": "Delhi",
}

# Nesting list in dictionary

travel_log = [
    {
        "France": {
            "dream_cities": ["Paris", "Lille", "Dijon"],
            "want_visit_times": 2
        },
        "India": {
            "where_visited": ["Delhi", "Bangalore", "Kochi", "Chandigarh"],
            "visited": True,
            "total_trips": "multiple"
        }
    }
]
travel_log_2 = [
    {
        "country": "France",
        "dream_cities": ["Paris", "Lille", "Dijon"],
        "want_visit_times": 2
    },
    {
        "country": "India",
        "where_visited": ["Delhi", "Bangalore", "Kochi", "Chandigarh"],
        "visited": True,
        "total_trips": "multiple"
    }
]

# country_visited = input("Enter country name you visited: \n")
# city_visited = input("Enter country name you visited: \n")
# trips_counter = int(input("Enter country name you visited: \n"))


my_travel_logs = [
    {
        "country": "India",
        "trips": "3",
        "cities": ["New Delhi", "Gurgaon", "Bangalore"]
    }
]

print(my_travel_logs)


def add_new_country(country, city, trips):
    new_country = {
        "country": country,
        "trips": trips,
        "cities": city
    }
    my_travel_logs.append(new_country)


add_new_country(country="Russia", trips=2, city=["Moscow", "Saint Petersburg"])
add_new_country(country="USA", trips=0, city=["", ""])
add_new_country(country="UK", trips=1, city=["London", "Bath", "York"])

# add_new_country(country=country_visited, city=city_visited, trips=trips_counter)


# print(my_travel_logs)
