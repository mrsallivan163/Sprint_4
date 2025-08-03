# qa_python
1. test_books_collector_init_empty_dict_genre - проверка, что books_genre — это пустой словарь
2. test_books_collector_init_empty_list_genre - проверка, что favorites — это пустой список
3. test_books_collector_init_list_expected_genre - проверка, genre — список с ожидаемыми жанрами
4. test_books_collector_init_list_expected_genre_age_rating - проверка, что genre_age_rating — список возрастных ограничений
5. test_add_new_book_add_two_books - проверка добавления двух новых книг в словарь
6. test_add_new_book_cannot_add_duplicate - проверка что одну и ту же книгу можно добавить только один раз
7. test_add_new_book_invalid_name_length_not_added - проверка, что название книги может содержать максимум 40 символов и не может быть пустым
8. test_set_book_genre_valid_sets_genre - проверка установки жанра добавленной книге
9. test_set_book_genre_nonexistent_book_no_effect - проверка, что устанавливается жанр книги, если книга есть в books_genre
10. test_set_book_genre_invalid_genre_not_set - проверка, что нельзя установаить жанр книге, которого нет в списке genre
11. test_get_book_genre_returns_genre - проверка получения жанра книги по ее названию
12. test_get_book_genre_nonexistent_book_returns_none - проверка, что нельзя получить жанр по наименованию книги, которой не существует в словаре
13. test_get_books_with_specific_genre_return_list_books_name_by_genre - проверка получения списка книг по определенному жанру
14. test_get_books_genre_return_dict_books_genre  - проверка получения текущего словаря books_genre
15. test_get_books_for_children_returns_only_child_safe_books - проверка получения книг, которые подходят детям, у жанра книги не должно быть возрастного рейтинга
16. test_add_book_in_favorites_add_books - проверка добавления книги в "Избранное"
17. test_add_book_in_favorites_nonexistent_book_not_added -  проверка, что добавить несуществующую книгу в "Избранное" нельзя
18. test_add_book_in_favorites_cannot_add_twice - проверка, что добавить дважды одну и ту же книгу в "Избранное" нельзя
19. test_delete_book_from_favorites_delete_books - проверка удаления книги из списка "Избранное"
20. test_get_list_of_favorites_books_get_list_favourites_books - проверка получения списка избранных книг
21. test_get_list_of_favorites_books_returns_empty_list_when_no_favorites - проверка возвращения пустого списка, если нет книг добавленных в "Избранное"
