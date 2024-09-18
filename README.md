# Проект интернет магазина на FastAPI


## Основной стек приложения

fastapi==0.112.1
jinja2==3.1.4
SQLAlchemy==2.0.35
PostgreSQL
alembic==1.13.2


## Запуск приложения

`
uvicorn app.main:app --port 8000 --reload
`
# Работа с базой данных

Документация по подключению БД через SQLAlchemy

https://docs.sqlalchemy.org/en/20/core/engines.html#backend-specific-urls

## Создание пользователя для PostgreSQL на linux

### Шаг 1: Установка PostgreSQL (если еще не установлено)
`Данная инструкция не предусмотрена текущей документацией`

## Шаг 2: Вход в систему PostgreSQL

1. **Переключитесь на пользователя `postgres`:**
   PostgreSQL устанавливает специального пользователя с именем `postgres`, который имеет право управлять БД.

```bash
sudo -i -u postgres
````

2. **Запустите консоль psql:**

```bash
psql
````
## Шаг 3: Создание пользователя

Для создания нового пользователя выполните следующую команду в консоли `psql`:

`
CREATE USER имя_пользователя WITH PASSWORD 'ваш_пароль';
`
#### Пример:
```sql
CREATE USER ecommerce WITH PASSWORD 'secure_password';
```
#### Ожидаемый результат:

`CREATE ROLE`

### Шаг 4: Создание БД и передача прав созданному пользователю

Для создания БД выполните следующую команду в консоли `psql`:

`
CREATE DATABASE имя_БД OWNER имя_пользователя ENCODING 'UTF8';
`
#### Пример:
```sql
CREATE DATABASE ecommerce OWNER ecommerce ENCODING 'UTF8';
```
#### Ожидаемый результат:

`CREATE DATABASE`

### Заключение

`Вы успешно создали нового пользователя и базу данных в PostgreSQL на Linux`

`Для выхода из консоли PostgreSQL используйте команду:`

```bash
\q
````

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
