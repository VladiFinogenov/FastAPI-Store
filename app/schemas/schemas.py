from pydantic import BaseModel as V2BaseModel

class CreateProduct(V2BaseModel):
    name: str
    description: str
    price: int
    image_url: str
    stock: int
    category: int

class CreateCategory(V2BaseModel):
    name: str
    parent_id: int | None

class CreateUser(V2BaseModel):
    first_name: str
    last_name: str
    username: str
    email: str
    password: str