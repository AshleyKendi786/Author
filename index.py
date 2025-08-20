

class Author:
    def __init__(self, name):
        if not isinstance(name, str):
            raise Exception("Name must be a string")
        if len(name) == 0:
            raise Exception("Name cannot be empty")
        self._name = name
        self._articles = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        raise Exception("Author name is immutable")

    def articles(self):
        return self._articles

    def magazines(self):
        
        return list({article.magazine for article in self._articles})


class Magazine:
    def __init__(self, name, category):
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise Exception("Name must be 2–16 characters")
        if not isinstance(category, str) or len(category) < 1:
            raise Exception("Category must be a non-empty string")
        self._name = name
        self._category = category
        self._articles = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not (2 <= len(value) <= 16):
            raise Exception("Name must be 2–16 characters")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str) or len(value) < 1:
            raise Exception("Category must be a non-empty string")
        self._category = value

    def articles(self):
        return self._articles

    def contributors(self):
        return list({article.author for article in self._articles})

    def article_titles(self):
        return [article.title for article in self._articles]

    def contributing_authors(self):
        # authors who wrote more than 2 articles
        authors = {}
        for article in self._articles:
            authors[article.author] = authors.get(article.author, 0) + 1
        return [author for author, count in authors.items() if count > 2]


class Article:
    def __init__(self, author, magazine, title):
        if not isinstance(author, Author):
            raise Exception("Author must be of type Author")
        if not isinstance(magazine, Magazine):
            raise Exception("Magazine must be of type Magazine")
        if not isinstance(title, str):
            raise Exception("Title must be a string")
        if not (5 <= len(title) <= 50):
            raise Exception("Title must be 5–50 characters")

        self._author = author
        self._magazine = magazine
        self._title = title

        #relationships
        author._articles.append(self)
        magazine._articles.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        raise Exception("Title is immutable")

    @property
    def author(self):
        return self._author

    @property
    def magazine(self):
        return self._magazine

if __name__ == "__main__":
    # Authors
    a1 = Author("Ashley")
    a2 = Author("Sylvia")

    # Magazines
    m1 = Magazine("TechWorld", "Fashion")
    m2 = Magazine("HealthPlus", "Beauty")

    # Articles
    Article(a1, m1, "AI Revolution in 2025")
    Article(a1, m1, "Python Tips and Tricks")
    Article(a2, m2, "Healthy Living Guide")
    Article(a2, m1, "Dance Studios in Campus")
    Article(a2, m1, "Fashion Trends 2023")


    print("\n--- Demo ---")
    print("Kendi's Articles:", [art.title for art in a1.articles()])
    print("Kendi's Magazines:", [mag.name for mag in a1.magazines()])
    print("Contributors to TechWorld:", [auth.name for auth in m1.contributors()])
    print("Articles in TechWorld:", m1.article_titles())
    print("Contributing Authors (2+ articles in TechWorld):",
          [auth.name for auth in m1.contributing_authors()])
