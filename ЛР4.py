if __name__ == "__main__":
    """
    becoming traditional book-library example
    """
class Lib:
    def __init__(self, name: str, age: int):
        """
        Конструктор базового класса Book.

        :param name: book name.
        :param age: years number.
        """
        self.name = name
        self.age = age

    def rate(self) -> str:
        """
        Метод 1.

        """
        return "Good"

    def __str__(self) -> str:
        """
        Магический метод 1 str.

        """
        return f"{self.name} ({self.__class__.__name__}), {self.age} лет с момента выпуска"

    def __repr__(self) -> str:
        """
        Магический метод 2 repr.

        """
        return f"Книга('{self.name}', {self.age}) лет с момента выпуска"


class book_one(Lib):
    def __init__(self, name: str, age: int, pages: int):
        """
        Конструктор дочернего класса book_one.

        :param name: Имя.
        :param age: Лет с момента выпуска.
        :param pages: Число страниц.
        """
        super().__init__(name, age)
        self.pages = pages

    def rate(self) -> str:
        """
        Rating

        """
        return "Good"
