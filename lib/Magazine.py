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
