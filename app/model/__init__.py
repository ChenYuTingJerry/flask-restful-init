class AbstractModel:

    def save(self):
        raise NotImplemented('save() need to be implemented')

    def delete(self):
        raise NotImplemented('delete() need to be implemented')

    def to_entity(self):
        raise NotImplemented('to_entity() need to be implemented')
