import pytest

from unittest.mock import MagicMock

from dao.model.genre import Genre
from dao.genre import GenreDAO
from service.genre import GenreService

@pytest.fixture()
def genre_dao():
    genre_dao = GenreDAO(None)

    genre_01 = Genre(id=1, name="first")
    genre_02 = Genre(id=2, name="second")
    genre_03 = Genre(id=3, name="third")

    genre_dao.get_one = MagicMock(return_value=genre_01)
    genre_dao.get_all = MagicMock(return_value=[genre_01, genre_02, genre_03])
    genre_dao.create = MagicMock(return_value=genre_03)
    genre_dao.update = MagicMock(return_value={
                                                    "id": 12,
                                                    "name": "twelfth"
                                                })
    genre_dao.delete = MagicMock()

    return genre_dao

class TestGenreService:
    @pytest.fixture(autouse=True)
    def genre_mock(self, genre_dao):
        self.genre_service = GenreService(dao=genre_dao)


    def test_get_one(self):
        genre = self.genre_service.get_one(1)

        assert genre is not None
        assert type(genre) is type(Genre())
        assert genre.name == 'first'
        assert genre.id == 1

    def test_get_all(self):
        genres = self.genre_service.get_all()

        assert genres is not None
        assert type(genres) is list
        assert genres[0].id == 1
        assert genres[2].id == 3
        assert genres[1].name == 'second'

    def test_create(self):
        genre_data = {
            "id": 12,
            "name": "twelfth"
        }

        genre = self.genre_service.create(genre_data)

        assert genre is not None
        assert genre.id > 1
        assert genre.id == 3
        assert type(genre) is type(Genre())

    def test_update(self):
        genre_data = {
            "id": 12,
            "name": "twelfth"
        }
        genre = self.genre_service.update(genre_data)

        assert genre is not None
        assert type(genre) is dict
        assert genre.get("name") != "test"
        assert "name" in genre
        assert genre["id"] > 1
        assert genre["id"] == 12
        assert type(genre) is type(genre_data)


    def test_partially_update(self):
        genre_data = {
            "id": 12,
            "name": "twelfth"
        }
        genre = self.genre_service.partially_update(genre_data)

        assert genre is None

    def test_delete(self):
        genre = self.genre_service.delete(1)

        assert genre is None