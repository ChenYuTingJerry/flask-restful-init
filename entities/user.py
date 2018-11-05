from lib.entity import Entity


class UserEntity(Entity):
    def __init__(self):
        self.name = 'john doe'
        self.gender = 'male'
        self.age = 16
