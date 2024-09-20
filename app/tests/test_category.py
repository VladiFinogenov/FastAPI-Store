import pytest
from sqlalchemy.orm.sync import update

from app.tests.factory import CategoryFactory
from routers.category import update_category


class Test:


    def setup(self):
        data = {
            "name": "test category",
            "parent_id": None
        }
        self.category = data


    @pytest.mark.asyncio
    async def test_create_category(self, client):

        response = await client.post(url="/category/create", json=self.category)

        assert response.status_code == 201
        assert response.json()["transaction"] == "Successful"


    @pytest.mark.asyncio
    async def test_get_all_categories(self, client):
        response = await client.get("/category/all_categories")

        assert response.status_code == 200
        assert isinstance(response.json(), list)
        assert response.json()[0]['name'] == self.category["name"]

    @pytest.mark.asyncio
    async def test_update_categories(self, client):
        update_data = self.category['name'] = ''
        response = await client.put("/category/update_category", json=self.category)

        assert response.status_code == 200
        assert isinstance(response.json(), list)
        assert response.json()[0]['name'] == self.category["name"]




