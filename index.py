# magazine_demo.py

class Article:
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title


class Author:
    _all_authors = []

    def __init__(self, name):
        self.name = name  # ✅ Use setter for validation
        self._articles = []
        Author._all_authors.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        if len(value.strip()) == 0:
            raise ValueError("Name must be longer than 0 characters")
        if hasattr(self, "_name"):  # prevents reassignment
            raise AttributeError("Name cannot be changed after instantiation")
        self._name = value

    @property
    def articles(self):
        return self._articles

    @property
    def magazines(self):
        return list(set(article.magazine for article in self._articles))

    def add_article(self, magazine, title):
        article = Article(self, magazine, title)
        self._articles.append(article)
        magazine._articles.append(article)
        return article

    @property
    def topic_areas(self):
        if not self._articles:
            return None
        return list(set(article.magazine.category for article in self._articles))

    @classmethod
    def all(cls):
        return cls._all_authors


class Magazine:
    _all_magazines = []

    def __init__(self, name, category):
        self.name = name
        self.category = category
        self._articles = []
        Magazine._all_magazines.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        if len(value) < 2 or len(value) > 16:
            raise ValueError("Name must be between 2 and 16 characters")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str):
            raise ValueError("Category must be a string")
        if len(value.strip()) == 0:
            raise ValueError("Category must be longer than 0 characters")
        self._category = value

    @property
    def articles(self):
        return self._articles

    @property
    def contributors(self):
        return list(set(article.author for article in self._articles))

    @property
    def article_titles(self):
        if not self._articles:
            return None
        return [article.title for article in self._articles]

    @property
    def contributing_authors(self):
        author_counts = {}
        for article in self._articles:
            author = article.author
            author_counts[author] = author_counts.get(author, 0) + 1

        contributing_authors = [author for author, count in author_counts.items() if count >= 2]
        return contributing_authors if contributing_authors else None

    @classmethod
    def top_publisher(cls):
        magazines_with_articles = [mag for mag in cls._all_magazines if mag.articles]
        if not magazines_with_articles:
            return None
        return max(magazines_with_articles, key=lambda mag: len(mag.articles))

    @classmethod
    def all(cls):
        return cls._all_magazines


# ---------------- DEMO / TEST ----------------

if __name__ == "__main__":
    # Create Authors
    a1 = Author("Ashley")
    a2 = Author("Kim")
    a3 = Author("Sylvia")

    # Create Magazines
    m1 = Magazine("Vogue", "Fashion")
    m2 = Magazine("TechLife", "Technology")
    m3 = Magazine("DanceBeat", "Entertainment")

    # Add Articles
    a1.add_article(m1, "Runway Revolution")
    a1.add_article(m1, "Streetwear Rising")
    a1.add_article(m2, "AI in Fashion")

    a2.add_article(m2, "The Future of Robotics")
    a2.add_article(m2, "Tech & Humanity")
    a2.add_article(m3, "Dancehall Explosion")

    a3.add_article(m1, "African Designers to Watch")
    a3.add_article(m3, "Campus Dance Trends")

    # --- TEST OUTPUTS ---
    print("All Authors:", [author.name for author in Author.all()])
    print("All Magazines:", [mag.name for mag in Magazine.all()])

    print("\nArticles by Ashley:", [article.title for article in a1.articles])
    print("Magazines Ashley has written for:", [mag.name for mag in a1.magazines])

    print("\nArticles in Vogue:", [article.title for article in m1.articles])
    print("Contributors to Vogue:", [author.name for author in m1.contributors])

    print("\nTopic areas Ashley covers:", a1.topic_areas)
    print("Titles in TechLife:", m2.article_titles)
    print("Contributing authors in TechLife (2+ articles):",
          [a.name for a in m2.contributing_authors or []])

    top = Magazine.top_publisher()
    print("\nTop Publisher:", top.name if top else None)
