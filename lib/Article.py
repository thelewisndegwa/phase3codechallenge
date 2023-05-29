class Article:
    instances = []

    def __init__(self, author, magazine, title):
        self._author = author
        self._magazine = magazine
        self._title = title
        Article.instances.append(self)
        author.add_article(self)
        magazine.articles().append(self)

    def title(self):
        return self._title
    
    def author(self):
        return self._author

    def magazine(self):
        return self._magazine

    @classmethod
    def all(cls):
        return cls.instances
    pass