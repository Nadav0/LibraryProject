class Book:
    def __init__(self, id, name, author, year_published, type):
        self.id = id
        self.name = name
        self.author = author
        self.year_published = year_published
        self.type = type

    MAX_LOAN_TIME = {
        1: 7,
        2: 14,
        3: 30
    }

    def get_max_loan_time(self):
        return self.MAX_LOAN_TIME[self.type]
