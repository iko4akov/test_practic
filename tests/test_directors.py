import pytest

from unittest.mock import MagicMock

from dao.model.director import Director
from dao.director import DirectorDAO
from service.director import DirectorService

@pytest.fixture()
def director_dao():
    director_dao = DirectorDAO(None)

    director_01 = Director(id=1, name="first")
    director_02 = Director(id=2, name="second")
    director_03 = Director(id=3, name="third")

    director_dao.get_one = MagicMock(return_value=director_01)
    director_dao.get_all = MagicMock(return_value=[director_01, director_02, director_03])
    director_dao.create = MagicMock(return_value=director_03)
    director_dao.update = MagicMock(return_value={
                                                    "id": 12,
                                                    "name": "twelfth"
                                                })
    director_dao.delete = MagicMock()


    return director_dao

class TestDirectorService:
    @pytest.fixture(autouse=True)
    def director_mock(self, director_dao):
        self.director_service = DirectorService(dao=director_dao)


    def test_get_one(self):
        director = self.director_service.get_one(1)

        assert director is not None
        assert type(director) is type(Director())
        assert director.name == 'first'
        assert director.id == 1

    def test_get_all(self):
        directors = self.director_service.get_all()

        assert directors is not None
        assert type(directors) is list
        assert directors[0].id == 1
        assert directors[2].id == 3
        assert directors[1].name == 'second'

    def test_create(self):
        dir_data = {
            "id": 12,
            "name": "twelfth"
        }

        director = self.director_service.create(dir_data)

        assert director is not None
        assert director.id > 1
        assert director.id == 3
        assert type(director) is type(Director())

    def test_update(self):
        dir_data = {
            "id": 12,
            "name": "twelfth"
        }
        director = self.director_service.update(dir_data)

        assert director is not None
        assert type(director) is dict
        assert director.get("name") != "test"
        assert "name" in director
        assert director["id"] > 1
        assert director["id"] == 12
        assert type(director) is type(dir_data)


    def test_partially_update(self):
        dir_data = {
            "id": 12,
            "name": "twelfth"
        }
        director = self.director_service.partially_update(dir_data)

        assert director is None

    def test_delete(self):
        dir = self.director_service.delete(1)

        assert dir is None
