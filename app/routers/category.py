from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.responses import JSONResponse

from app.backend.db_depends import get_db
from typing import Annotated
from sqlalchemy import select, update
from app.models import Category
from sqlalchemy import insert
from app.schemas.schemas import CreateCategory

from app.utils.slug import create_slug

router = APIRouter(prefix='/category', tags=['category'])


@router.get('/all_categories')
async def get_all_categories(db: Annotated[AsyncSession, Depends(get_db)]):
    categories = await db.scalars(select(Category).where(Category.is_active == True))

    return categories.all()


@router.post('/create')
async def create_category(
        db: Annotated[AsyncSession, Depends(get_db)],
        create_category: CreateCategory
):
    # Проверка на наличие родительской категории
    if create_category.parent_id:
        parent_category = await db.get(Category, create_category.parent_id)
        if not parent_category:
            raise HTTPException(status_code=404, detail="Parent category not found")

    # Создание новой категории
    new_category = Category(
        name=create_category.name,
        slug=create_slug(create_category.name),
        parent_id=create_category.parent_id
    )

    db.add(new_category)
    await db.commit()
    await db.refresh(new_category)  # Обновляем объект, чтобы получить созданный ID

    return JSONResponse(
        content={'transaction': 'Successful'},
        status_code=status.HTTP_201_CREATED
    )


@router.put('/update_category')
async def update_category(db: Annotated[AsyncSession, Depends(get_db)], category_id: int, update_category: CreateCategory):
    category = await db.scalar(select(Category).where(Category.id == category_id))
    if not category:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='There is no category found'
        )

    await db.execute(update(Category).where(Category.id == category_id).values(
            name=update_category.name,
            slug=create_slug(update_category.name),
            parent_id=update_category.parent_id)
    )

    await db.commit()

    return {
        'status_code': status.HTTP_200_OK,
        'transaction': 'Category update is successful'
    }


@router.delete('/delete/{category_id}')
async def delete_category(db: Annotated[AsyncSession, Depends(get_db)], category_id: int):
    category = await db.scalar(select(Category).where(Category.id == category_id))
    if not category:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='There is no category found'
        )
    await db.delete(category)
    # await db.execute(update(Category).where(Category.id == category_id).values(is_active=False))
    await db.commit()

    return {
        'status_code': status.HTTP_200_OK,
        'transaction': 'Category delete is successful'
    }