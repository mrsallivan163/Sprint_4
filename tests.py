from main import BooksCollector
import pytest


class TestBooksCollector:

    # Тесты init 
    def test_books_collector_init_empty_dict_genre(self):
        collector = BooksCollector()
        assert collector.books_genre == {}

    def test_books_collector_init_empty_list_genre(self):
        collector = BooksCollector()
        assert collector.favorites == []

    def test_books_collector_init_list_expected_genre(self):
        collector = BooksCollector()
        expected_genre = ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']
        assert collector.genre == expected_genre
    
    def test_books_collector_init_list_expected_genre_age_rating(self):
        collector = BooksCollector()
        expected_age_rating = ['Ужасы', 'Детективы']
        assert collector.genre_age_rating == expected_age_rating
    
    # Тесты метода add_new_book
    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    def test_add_new_book_cannot_add_duplicate(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Гордость и предубеждение и зомби')
        assert len(collector.get_books_genre()) == 1

    @pytest.mark.parametrize(
        'book_name',
        ['', 'a' * 41] 
    )
    def test_add_new_book_invalid_name_length_not_added(self, book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        assert len(collector.get_books_genre()) == 0

    # Тесты метода set_book_genre 
    def test_set_book_genre_valid_sets_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')
        assert collector.get_book_genre('Гордость и предубеждение и зомби') == 'Фантастика'

    def test_set_book_genre_nonexistent_book_no_effect(self):
        collector = BooksCollector()
        collector.set_book_genre('Несуществующая книга', 'Фантастика')
        assert 'Несуществующая книга' not in collector.get_books_genre()

    @pytest.mark.parametrize(
        'invalid_genre',
        ['Неизвестный жанр', '', 'Триллер']
    )
    def test_set_book_genre_invalid_genre_not_set(self, invalid_genre):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', invalid_genre)
        assert collector.get_book_genre('Гордость и предубеждение и зомби') == ''

    # Тесты метода get_book_genre 
    def test_get_book_genre_returns_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')
        assert collector.get_book_genre('Гордость и предубеждение и зомби') == 'Фантастика'

    def test_get_book_genre_nonexistent_book_returns_none(self):
        collector = BooksCollector()
        assert collector.get_book_genre('Несуществующая книга') is None

    # Тесты метода get_books_with_specific_genre 
    @pytest.mark.parametrize(
        'books_data, target_genre, expected',
        [
            ([('Гордость и предубеждение и зомби', 'Фантастика'), ('Что делать, если ваш кот хочет вас убить', 'Фантастика')], 'Фантастика', ['Гордость и предубеждение и зомби', 'Что делать, если ваш кот хочет вас убить']),
            ([('Что делать, если ваш кот хочет вас убить', 'Ужасы')], 'Фантастика', []),
            ([('Что делать, если ваш кот хочет вас убить', 'Фантастика')], 'Драма', []), 
            ([], 'Фантастика', []), 
        ]
    )
    def test_get_books_with_specific_genre_return_list_books_name_by_genre(self, books_data, target_genre, expected):
        collector = BooksCollector()
        for name, genre in books_data:
            collector.add_new_book(name)
            collector.set_book_genre(name, genre)
        assert sorted(collector.get_books_with_specific_genre(target_genre)) == sorted(expected)

    # Тесты метода get_books_genre
    def test_get_books_genre_return_dict_books_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Ужасы')
        assert collector.get_books_genre() == {'Гордость и предубеждение и зомби':'Фантастика', 'Что делать, если ваш кот хочет вас убить':'Ужасы'}

    # Тесты метода get_books_for_children
    def test_get_books_for_children_returns_only_child_safe_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Ужасы')
        assert collector.get_books_for_children() == ['Гордость и предубеждение и зомби']

    @pytest.mark.parametrize(
        'books_data, expected_children_books',
        [
            ([('Гордость и предубеждение и зомби', 'Фантастика'), ('Приключение Паддингтона 2', 'Мультфильмы')], ['Гордость и предубеждение и зомби', 'Приключение Паддингтона 2']),
            ([('Что делать, если ваш кот хочет вас убить', 'Ужасы'), ('Агент Шмидт', 'Детективы')], []),
            ([('Гордость и предубеждение и зомби', 'Фантастика'), ('Что делать, если ваш кот хочет вас убить', 'Ужасы')], ['Гордость и предубеждение и зомби']),
            ([('Без жанра', '')], []),
            ([], [])
        ]
    )
    def test_get_books_for_children_returns_only_child_safe_books(self, books_data, expected_children_books):
        collector = BooksCollector()
        for name, genre in books_data:
            collector.add_new_book(name)
            collector.set_book_genre(name, genre)
        result = collector.get_books_for_children()
        assert sorted(result) == sorted(expected_children_books)

    # Тесты add_book_in_favorites
    def test_add_book_in_favorites_add_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        assert 'Гордость и предубеждение и зомби' in collector.get_list_of_favorites_books()

    def test_add_book_in_favorites_nonexistent_book_not_added(self):
        collector = BooksCollector()
        collector.add_book_in_favorites('Несуществующая книга')
        assert len(collector.get_list_of_favorites_books()) == 0

    def test_add_book_in_favorites_cannot_add_twice(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        assert len(collector.get_list_of_favorites_books()) == 1

    # Тесты delete_book_from_favorites
    def test_delete_book_from_favorites_delete_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.delete_book_from_favorites('Гордость и предубеждение и зомби')
        assert 'Гордость и предубеждение и зомби' not in collector.get_list_of_favorites_books()

    # Тесты get_list_of_favorites_books
    def test_get_list_of_favorites_books_get_list_favourites_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        assert collector.get_list_of_favorites_books() == ['Гордость и предубеждение и зомби']
    
    def test_get_list_of_favorites_books_returns_empty_list_when_no_favorites(self):
        collector = BooksCollector()
        assert collector.get_list_of_favorites_books() == []
        