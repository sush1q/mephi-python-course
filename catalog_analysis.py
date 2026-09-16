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

def catalog_age_stats(movies, current_year=2026):
    ages = [current_year - movie.get("year") for movie in movies]

    oldest_movie_age = max(ages)
    newest_movie_age = min(ages)
    average_movie_age = math.ceil(sum(ages) / len(ages))

    return (oldest_movie_age, newest_movie_age, average_movie_age)

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
        print(movie.get("title")) 

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

def normalize_title(title):
    upd_title = []
    for word in title.split():
        upd_title.append(word[0].upper() + word[1:])
    return " ".join(upd_title)

def make_slug(title):
    return title.lower().replace(" ", "-")

def format_report_line(movie):
    return f'"{normalize_title(movie.get("title"))}" ({movie.get("year")}) - {movie.get("rating")}/10, {duration_in_hours(movie.get("duration_min"))}, жанры: {", ".join(sorted(movie.get("genres")))}'

def titles_sorted_by_rating(movies):
    sorted_movies = sorted(movies, key=lambda x: x.get("rating"), reverse=True)
    return list(map(lambda x: x.get("title"), sorted_movies))
    
def top_n_by_rating(movies, n=3):
    ret = []
    sorted_movies = sorted(movies, key=lambda x: x.get("rating"), reverse=True)
    for movie in sorted_movies:
        ret.append((movie.get("title"), movie.get("rating")))
        if (len(ret) >= n):
            return ret
    return ret

def count_by_genre(movies):
    ret = {}
    for movie in movies:
        for genre in movie.get("genres"):
            ret[genre] = ret.get(genre, 0) + 1
    return ret

def actor_filmography(movies):
    ret = {}
    for movie in movies:
        for actor in movie.get("actors"):
            if actor not in ret:
                ret[actor] = []
            ret[actor].append(movie.get("title"))
    return ret

def get_above_average_movies(movies):
    avg = average_rating(movies)
    return {movie.get("title"): movie.get("rating") for movie in movies if movie.get("rating") > avg}

def all_genres(movies):
    unique_genres = set()
    for movie in movies:
        unique_genres.update(movie.get("genres"))
    return unique_genres

def common_actors(movie1, movie2):
    return set(movie1.get("actors")) & set(movie2.get("actors"))

def genres_only_in_one(movies_a, movies_b):
    genres_a = map(lambda x: x.get("genres"), movies_a)
    genres_b = map(lambda x: x.get("genres"), movies_b)
    
    a = set([j for i in genres_a for j in i])
    b = set([j for i in genres_b for j in i])
    return a - b

def iter_high_rated(movies, min_rating=8.0):
    for movie in movies:
        if movie.get("rating") < min_rating:
            continue
        yield movie

def demo_iterator(movies):
    for movie in iter_high_rated(movies):
        print(format_report_line(movie))

def build_report(movies):
    top_3 = [format_report_line(movie) for movie in sorted(movies, key=lambda x: x.get("rating"), reverse=True)[:3]]
    genres_count = dict(sorted(count_by_genre(movies).items(), key=lambda x: x[1], reverse=True))
    
    report = f"""ОТЧЕТ ПО КАТАЛОГУ
Средний рейтинг: {average_rating(movies)}
Средний возраст фильмов: {catalog_age_stats(movies)[2]} лет

Топ-3 фильма:
{"\n".join("  " + line for line in top_3)}

Фильмов по жанрам:
{"\n".join(f"  {genre} — {count}" for genre, count in genres_count.items())}

Все жанры каталога: {", ".join(sorted(all_genres(movies)))}"""
    return report

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
    
    print(f"Result of normalize_title call {normalize_title(movies[2].get("title"))}")
    print(f"Result of make_slug call {make_slug(movies[2].get("title"))}")
    print(f"Result of format_report_line call {format_report_line(movies[0])}")
    
    print(f"Result of titles_sorted_by_rating call {titles_sorted_by_rating(movies)}")
    print(f"Result of top_n_by_rating call {top_n_by_rating(movies)}")
    
    print(f"Result of count_by_genre call {count_by_genre(movies)}")
    print(f"Result of actor_filmography call {actor_filmography(movies)}")
    print(f"Result of get_above_average_movies call {get_above_average_movies(movies)}")
    
    print(f"Result of all_genres call {all_genres(movies)}")
    print(f"Result of common_actors call {common_actors(movies[0], movies[3])}")
    print(f"Result of genres_only_in_one call {genres_only_in_one(movies[5:6], movies[:5])}")

    demo_iterator(movies)
    
    print(f"Sum of films with score more than 7: {sum(movie.get("duration_min") for movie in movies if movie.get("rating") > 7)}")

    print("=============")

    print(build_report(movies))

if __name__ == "__main__":
    main()

