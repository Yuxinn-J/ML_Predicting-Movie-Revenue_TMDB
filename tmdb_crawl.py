import csv
import requests
import json

with open("yearByYear_data.csv", "w") as outfile:
    f = csv.writer(outfile)
    f.writerow(
          ['id', 'imdb_id', 'adult', 'belongs_to_collection', 'budget', 'genres', 'original_language', 'original_title',
          'popularity', 'production_companies', 'production_countries', 'release_date', 'revenue',
          'runtime', 'spoken_languages', 'status', 'title', 'video', 'vote_average', 'vote_count'])
    with open('yearByYearID_data.csv') as file:
        data=csv.reader(file)
        rows=[row for row in data]
        for row in rows:
            if row[0]=='year':
                continue
            url = 'https://api.themoviedb.org/3/movie/' + row[0] + '?api_key=eca64d0f17cb0b1db8ea87f94de242ed&language=en-US'
            response = requests.get(str(url))
            json_res = response.json()

            #f = csv.writer(outfile)

            try:
                # for row in json_res['genres']:
                #     del row['id']
                # del json_res['belongs_to_collection']['id']
                # del json_res['belongs_to_collection']['poster_path']
                # del json_res['belongs_to_collection']['backdrop_path']
                # for row in json_res['production_companies']:
                #     del row['id']
                #     del row['logo_path']
                # for row in json_res['production_countries']:
                #     del row['iso_3166_1']
                f.writerow([json_res['id'], json_res['imdb_id'], json_res['adult'], json_res['belongs_to_collection'],
                            json_res['budget'], json_res['genres'], json_res['original_language'], json_res['original_title'],
                            json_res['popularity'], json_res['production_companies'],
                            json_res['production_countries'], json_res['release_date'], json_res['revenue'],
                            json_res['runtime'], json_res['spoken_languages'], json_res['status'], json_res['title'],
                            json_res['video'], json_res['vote_average'], json_res['vote_count']])
            except:
                pass
