import redis
import pandas as pd

server = redis.Redis(host='localhost', port=6379, db=0)
pubsub = server.pubsub()

pubsub.subscribe('topic_create_file')

for b in pubsub.listen():
    data = b['data']
    if data != 1:
        df = pd.read_json(data)
        df.to_csv('./files/file_python.csv', encoding='utf-8', index=False)
        print(f"File python CSV\n")
