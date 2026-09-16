import math

movies = [
    {"title": "The Dune Chronicles", "year": 2021, "genres": {"sci-fi", "drama"},
     "rating": 8.6, "duration_min": 155, "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"]}, # noqa: E501
    {"title": "Kitchen Stories", "year": 2019, "genres": {"comedy", "drama"},
     "rating": 7.1, "duration_min": 98, "actors": ["A. Novak", "M. Ferguson"]},
    {"title": "silent hours", "year": 2016, "genres": {"thriller", "drama"},
     "rating": 6.4, "duration_min": 112, "actors": ["J. Bloom", "K. Lee"]},
    {"title": "Comet Racers", "year": 2023, "genres": {"sci-fi", "action"},
     "rating": 5.9, "duration_min": 101, "actors": ["O. Isaac", "P. Diaz"]},
    {"title": "The Last Bakery", "year": 2014, "genres": {"comedy"},
     "rating": 7.8, "duration_min": 89, "actors": ["A. Novak", "T. Chalamet"]},
    {"title": "midnight in oslo", "year": 2020, "genres": {"thriller", "mystery"},
     "rating": 8.9, "duration_min": 124, "actors": ["K. Lee", "R. Ferguson"]},
    {"title": "Garden of Static", "year": 2022, "genres": {"drama"},
     "rating": 4.8, "duration_min": 137, "actors": ["P. Diaz", "J. Bloom"]},
    {"title": "The Quiet Algorithm", "year": 2024, "genres": {"sci-fi", "drama"},
     "rating": 9.2, "duration_min": 118, "actors": ["M. Ferguson", "O. Isaac"]},
    {"title": "Two Left Shoes", "year": 2011, "genres": {"comedy"},
     "rating": 6.0, "duration_min": 95, "actors": ["A. Novak", "K. Lee"]},
    {"title": "Red Harbor", "year": 2018, "genres": {"action", "thriller"},
     "rating": 7.3, "duration_min": 129, "actors": ["P. Diaz", "T. Chalamet"]},
]

def average_rating(movies):
    rating_sum = sum([i.get("rating", 0) for i in movies])
    return round(rating_sum / len(movies), 1)

def catalog_age_stats(movies, current_year=2026): # TODO: получается current_year не обязательна, по подсказке в заданию надо использовать для расчета возраста фильма, но поидее можно сортировкой обойтись
    movies_sorted = sorted(movies, key=lambda x: x.get("year"))
    average_year = math.ceil((movies_sorted[0].get("year") + movies_sorted[-1].get("year")) / 2)
    average_age_film = list(filter(lambda x: x.get("year") == average_year, movies_sorted))
    
    return (movies_sorted[0], movies_sorted[-1], average_age_film[0])

def duration_in_hours(minutes):
    hours = minutes // 60
    minutes = minutes % 60
    hours_str = f"{hours}ч " if hours != 0 else ""
    return f"{hours_str}{minutes}м"

def rating_tier(rating):
    if rating >= 9:
        return "шедевр"
    elif rating >= 7:
        return "хорошо"
    else:
        return "средне" if rating > 5 else "слабо"

def decade_label(year):
    match year:
        case n if n > 2020:
            return "новые"
        case n if 2015 <= n <= 2020:
            return "недавние"
        case _:
            return "старые"

def print_not_comedies(movies):
    for movie in movies:
        if "comedy" in movie.get("genres"):
            continue
        print(movie) 

def print_first_masterpiece(movies):
    i = 0
    while i < len(movies):
        if movies[i].get("rating") > 9.0:
            print(f"Первый найденный шедевр: {movies[i]}")
            break
        i+=1
    else:
        print("Шедевров не найдено")

def count_long_movies(movies, threshold=120):
    count = 0
    for movie in movies:
        if movie.get("duration_min") > threshold:
            count += 1
    return count

def main():
    print("Started main")

    print(f"Result of average_rating call {average_rating(movies)}")
    print(f"Result of catalog_age_stats call {catalog_age_stats(movies)}")
    print(f"Result of duration_in_hours call {duration_in_hours(movies[0].get("duration_min"))}")
    print(f"Result of rating_tier call {rating_tier(movies[0].get("rating"))}")
    print(f"Result of decade_label call {decade_label(movies[0].get("year"))}")
    
    print_not_comedies(movies)
    print_first_masterpiece(movies)
    print(f"Result of count_long_movies call {count_long_movies(movies)}")
    

if __name__ == "__main__":
    main()

