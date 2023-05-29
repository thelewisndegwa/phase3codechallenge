from lib.Article import Article

class Author:
    def __init__(self, name):
        self._name = name
        self._articles = []

    def name(self):
        return self._name
    
    def articles(self):
        return self._articles

    def magazines(self):
        unique_magazines = set()
        for article in self._articles:
            unique_magazines.add(article.magazine())
        return list(unique_magazines)

    def add_article(self, magazine, title):
        article = Article(self, magazine, title)
        self._articles.append(article)
    
    def topic_areas(self):
        unique_categories = set()
        for article in self._articles:
            unique_categories.add(article.magazine().category())
        return list(unique_categories)