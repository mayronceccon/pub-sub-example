import redis
import pandas as pd

cars = [
    {'Brand': 'Honda Civic', 'Price': '22000'},
    {'Brand': 'Toyota Corolla', 'Price': '25000'},
    {'Brand': 'Ford Focus', 'Price': '27000'},
    {'Brand': 'Audi A4', 'Price': '35000'},
    {'Brand': 'Ford Fiesta', 'Price': '15000'},
]

df = pd.DataFrame(cars, columns=['Brand', 'Price'])

server = redis.Redis(host='localhost', port=6379, db=0)
server.publish('topic_create_file', df.to_json(orient='records'))
server.save()
