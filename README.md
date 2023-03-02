# Movie Service Unit Test
***
_Это набор тестов для класса `MovieService`, который отвечает за обработку логики объектов фильма. Эти тесты проверяют правильность работы класса `MovieService`, имитируя класс `MovieDAO`, отвечающий за доступ к данным._

---

## Dependencies (Зависимости)
+ Python 3.7+
+ pytest
+ unittest.mock
---

## How to run the tests (Как запустить тесты)

1. Clone the repository to your local machine.
2. Navigate to the `tests` directory.
3. Run the command `python -m pytest`.

---

## How the tests are structured (Как устроены тесты)

### `movie_dao()` fixture

_Эта `fixture` устанавливает фиктивный объект MovieDAO с предопределенными методами и атрибутами, которые будут использоваться в каждом тесте._

### `TestMovieService` class

_Это тестовый класс, который содержит отдельные тесты для класса `MovieService`._

### `movie_mock()` fixture

_Эта `fixture` создает новый объект `MovieService` с фиктивным объектом `MovieDAO`._

### Individual tests (Индивидуальные тесты):
`test_get_one()`: проверяет метод `get_one()` службы `MovieService`. Он проверяет, возвращает ли метод объект фильма с правильными атрибутами.
`test_get_all()`: проверяет метод `get_all()` службы `MovieService`. Он проверяет, возвращает ли метод список объектов фильмов с правильными атрибутами.
`test_create()`: проверяет метод `create()` службы `MovieService`. Он проверяет, возвращает ли метод строку при создании нового фильма.
`test_update()`: проверяет метод `update()` службы `MovieService`. Он проверяет, возвращает ли метод словарь с обновленными атрибутами при обновлении фильма.
`test_partially_update()`: тестирует метод `partial_update()` службы `MovieService`. Он проверяет, возвращает ли метод `None` при попытке обновления с недопустимыми атрибутами.
`test_delete()`: проверяет метод `delete()` службы `MovieService`. Он проверяет, возвращает ли метод `None` при удалении фильма.
---
_Набор тестов для классов `DirectorService` и `GenreService` аналогичны `MovieService`_

![codwars](https://www.codewars.com/users/Ko4ak/badges/large)
