import redis
import pandas as pd

server = redis.Redis(host='localhost', port=6379, db=0)
pubsub = server.pubsub()

pubsub.subscribe('topic_create_file')

for b in pubsub.listen():
    data = b['data']
    if data != 1:
        df = pd.read_json(data)
        df.to_excel('./files/file_python.xls')
        print(f"File python XLS\n")
