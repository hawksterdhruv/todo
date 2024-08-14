from tinydb import TinyDB
from tinydb.storages import JSONStorage
from tinydb_serialization import SerializationMiddleware
from tinydb_serialization.serializers import DateTimeSerializer

serialization = SerializationMiddleware(JSONStorage)
serialization.register_serializer(DateTimeSerializer(), 'TinyDate')
db = TinyDB('todos_db.json', storage=serialization)


def get_max_index():
    todo = db.get(doc_id=len(db))

    return todo['id'] if todo else 0
