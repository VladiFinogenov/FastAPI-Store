import factory
from factory.alchemy import SQLAlchemyModelFactory
from app.models import Product, Category


class CategoryFactory(SQLAlchemyModelFactory):
    class Meta:
        model = Category
        sqlalchemy_session = None  # Сессия будет передаваться во время создания

    name = factory.Faker('word')
    slug = factory.Faker('slug')
    is_active = True
    parent_id = None

    @classmethod
    def create(cls, **kwargs):
        session = kwargs.pop('session', None)
        if session is None:
            raise RuntimeError("No session provided.")

        return super().create(session=session, **kwargs)

    @classmethod
    def create_multiple(cls, count, session=None, **kwargs):
        """Метод для создания нескольких экземпляров с указанной сессией."""

        return [cls.create(session=session, **kwargs) for _ in range(count)]

class ProductFactory(SQLAlchemyModelFactory):
    class Meta:
        model = Product
        sqlalchemy_session = None

    name = factory.Faker('word')
    slug = factory.Faker('slug')
    description = factory.Faker('text')
    price = factory.Faker('random_int', min=1, max=100)
    image_url = factory.Faker('image_url')
    stock = factory.Faker('random_int', min=1, max=100)
    rating = factory.Faker('random_float', min=0, max=5, ndigits=1)
    category = factory.SubFactory(CategoryFactory)

    @classmethod
    def create(cls, **kwargs):
        session = kwargs.pop('session', None)
        if session is None:
            raise RuntimeError("No session provided.")

        return super().create(session=session, **kwargs)

    @classmethod
    def create_multiple(cls, count, session=None, **kwargs):
        """Метод для создания нескольких экземпляров с указанной сессией."""

        return [cls.create(session=session, **kwargs) for _ in range(count)]