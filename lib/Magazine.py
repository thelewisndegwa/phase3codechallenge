class Magazine:
    instances = []

    def __init__(self, name, category):
        self._name = name
        self._category = category
        self._contributors = []
        self._articles = []
        Magazine.instances.append(self)

    def name(self):
        return self._name

    def category(self):
        return self._category
    
    def contributors(self):
        return self._contributors
    
    def articles(self):
        return self._articles

    @classmethod
    def all(cls):
        return cls.instances
    
    def add_contributor(self, author):
        self._contributors.append(author)

    @classmethod
    def find_by_name(cls, name):
        for magazine in cls.instances:
            if magazine.name() == name:
                return magazine
        return None

    @classmethod
    def article_titles(cls):
        titles = []
        for magazine in cls.instances:
            for article in magazine.articles():
                titles.append(article.title())
        return titles

    def contributing_authors(self):
        author_counts = {}
        for article in self._articles:
            author = article.author()
            if author in author_counts:
                author_counts[author] += 1
            else:
                author_counts[author] = 1
        return [author for author, count in author_counts.items() if count > 2]
    pass