import json
from copy import deepcopy


class Entity(dict):
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

    @classmethod
    def from_object(cls, obj):
        entity = cls()
        if type(obj) is dict:
            entity.update(obj)
        elif type(obj) is str or type(obj) is bytes:
            entity.update(json.loads(obj))

        for key, value in entity.items():
            if type(value) is dict:
                entity[key] = cls.from_object(json.dumps(value))
            elif type(value) is list:
                for i, obj in enumerate(value):
                    if type(obj) is dict:
                        value[i] = cls.from_object(json.dumps(obj))

        return entity
