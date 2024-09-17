# Проект интернет магазина на FastAPI


## Основной стек приложения

fastapi==0.112.1
jinja2==3.1.4
SQLAlchemy==2.0.35
alembic==1.13.2


## Запуск приложения

`
uvicorn app.main:app --port 8000 --reload
`

## Создание миграций

* alembic init app/migrations

* изменить настройки подключения в файле alembic.ini sqlalchemy.url на настройки указанные в db
Пример: sqlalchemy.url = sqlite:///ecommerce.db

* Изменить настройки env.py target_metadata = None на: 

`from app.backend.db import Base
from app.models.category import Category
from app.models.products import Product

target_metadata = Base.metadata`

* Выполнить первую миграцию командой

```bash
alembic revision --autogenerate -m "Initial migration"
```

* Выполнить команду: "alembic upgrade head" - применение самой последней созданной миграции

### основные команды в Alembic:

** alembic upgrade +2 две версии включая текущую для апгрейда
** alembic downgrade -1 на предыдущую для даунгрейда
** alembic current получить информацию о текущей версии
** alembic history --verbose история миграций, более подробнее можно почитать в документации.
** alembic downgrade base даунгрейд в самое начало миграций
** alembic upgrade head применение самой последней созданной миграции
