import json
from django.test import TestCase
from django.test import Client
from webapp.models import Film, Actor

client = Client()
actors_set = set()
dataset = [{"title": "The Internship", "company": "Twentieth Century Fox Film Corporation", "writer": "Vince Vaughn",
            "longitude": -122.3893566, "director": "Shawn Levy",
            "distributor": "Twentieth Century Fox Film Corporation",
            "actors": ["Vince Vaughn", "Owen Wilson", "Rose Byrne"], "location": "Epic Roasthouse", "year": 2013,
            "latitude": 37.7908379, "fact": ""},
           {"title": "The Core", "company": "David Foster Productions", "writer": "Cooper Lane",
            "longitude": -122.4782551, "director": "John Amiel", "distributor": "Paramount Pictures",
            "actors": ["Aaron Eckhart", "Hilary Swank"], "location": "Golden Gate Bridge", "year": 2003,
            "latitude": 37.8199286,
            "fact": "With 23 miles of ladders and 300,000 rivets in each tower, the Golden Gate Bridge was the world's longest span when it opened in 1937."},
           {"title": "Quitters", "company": "Frederick & Ashbury, LLC.", "writer": "Noah Pritzker",
            "longitude": -122.4528316, "director": "Noah Pritzker", "distributor": "",
            "actors": ["Kara Hayward", "Mira Sorvino", "Saffron Burrows"], "location": "Cal-Mart Supermarket",
            "year": 2015, "latitude": 37.7861993, "fact": ""},
           {"title": "Milk", "company": "Focus Features", "writer": "Dustin Lance Black", "longitude": -122.3977199,
            "director": "Gus Van Sant", "latitude": 37.78604379999999, "actors": ["Sean Penn", "Emile Hirsch"],
            "location": "Marine Fireman's Union Headquarters", "year": 2008, "distributor": "Focus Features",
            "fact": ""},
           {"title": "Milk2", "company": "Focus Features", "writer": "Dustin Lance Black", "longitude": -122.3977199,
            "director": "Gus Van Sant", "latitude": 37.78604379999999, "actors": ["Sean Penn", "Emile Hirsch"],
            "location": "Marine Fireman's Union Headquarters", "year": 2008, "distributor": "Focus Features",
            "fact": ""}]


class FilmTestCase(TestCase):
    def setUp(self):
        for item in dataset:
            title = item['title']
            year = item['year']
            location = item['location']
            fact = item['fact']
            company = item['company']
            distributor = item['distributor']
            director = item['director']
            writer = item['writer']
            latitude = item['latitude']
            longitude = item['longitude']
            actors = item['actors']
            for actor in actors:
                actors_set.add(actor)
            film = Film(title=title, year=year, location=location, fact=fact,
                        company=company, distributor=distributor, director=director,
                        writer=writer, latitude=latitude, longitude=longitude)
            film.save()
            for name in actors:
                actor, created = Actor.objects.get_or_create(name=name)
                film.actors.add(actor)

    def test_films_created_correctly(self):
        self.assertEqual(Film.objects.all().count(), len(dataset))
        self.assertEqual(Actor.objects.all().count(), len(actors_set))

    def test_retrieve_all_films(self):
        response = client.get('/film/search')
        content = response.content
        films = json.loads(content)
        self.assertItemsEqual(dataset, films)

    def test_search_film_by_single_field(self):
        fields = ['title', 'company', 'director', 'distributor', 'writer']
        for field in fields:
            for item in dataset:
                if item[field]:
                    # if value is empty, it means we're not filtering on that column
                    answer = filter(lambda x: x[field] == item[field], dataset)
                    response = client.get('/film/search', {field: item[field]})
                    film = json.loads(response.content)
                    self.assertItemsEqual(answer, film)

    def test_search_film_by_year_range(self):
        start_year = 2008
        end_year = 2013
        answer = filter(lambda x: x['year'] >= start_year and x['year'] <= end_year, dataset)
        response = client.get('/film/search', {'start_year': start_year, 'end_year': end_year})
        film = json.loads(response.content)
        self.assertItemsEqual(answer, film)

    def test_autocompletion(self):
        fields = ['title', 'company', 'director', 'distributor', 'writer']
        for field in fields:
            answer = list(set(map(lambda x: x[field], dataset)))
            response = client.get('/film/getSuggestion', {'field': field})
            suggestion = json.loads(response.content)
            self.assertItemsEqual(answer, suggestion['items'])
