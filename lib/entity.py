import json
from copy import deepcopy


def mapper(obj):
    entity = Entity()
    if type(obj) is dict:
        entity.__dict__ = obj
    elif type(obj) is str or type(obj) is bytes:
        entity.__dict__ = json.loads(obj)

    for key, value in entity.__dict__.items():
        if type(value) is dict:
            entity.__dict__[key] = mapper(json.dumps(value))
        elif type(value) is list:
            for i, obj in enumerate(value):
                if type(obj) is dict:
                    value[i] = mapper(json.dumps(obj))

    return entity


class Entity:
    def __init__(self):
        pass

    def to_json(self):
        copy = deepcopy(self.__dict__)
        for key, value in copy.items():
            if type(value) is Entity:
                copy[key] = json.loads(value.to_json())
            elif type(value) is list:
                for i, obj in enumerate(value):
                    if type(obj) is Entity:
                        value[i] = json.loads(obj.to_json())
        return json.dumps(copy)

    def to_dict(self):
        return self.__dict__
