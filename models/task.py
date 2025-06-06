class Task:
    def __init__(self, id, title, description, completd=False) -> None:
        self.id = id
        self.title = title
        self.description = description
        self.completd = completd

    
    def to_dict(self):
        return{
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'completd': self.completd
        }