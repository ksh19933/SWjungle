from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbjungle

movie = db.movies.find_one({'title': '매트릭스'})
star = movie['star']


same_star_movies = list(db.movies.find({'star': star}))

for movies in same_star_movies:
  print(movies['title'])

db.movies.update_one({'tile':'매트릭스'}, {'$set':{'star':0}})
print(movie['star'])