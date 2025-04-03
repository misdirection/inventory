import os
from typing import List, Optional
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from domain.entities.category import Category
from application.interfaces.category_repository import CategoryRepository

DATABASE_URL = os.environ.get(
    "DATABASE_URL", "postgresql+psycopg2://postgres@localhost:5432/inventory"
)

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()


class CategoryModel(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)


def map_model_to_category(model: CategoryModel) -> Category:
    return Category(
        id=model.id, name=model.name, description=model.description, attributes=[]
    )


def map_category_to_model(category: Category) -> CategoryModel:
    return CategoryModel(name=category.name, description=category.description)


class PostgresCategoryRepository(CategoryRepository):
    def __init__(self):
        Base.metadata.create_all(engine)

    def get_all_categories(self) -> List[Category]:
        session = SessionLocal()
        try:
            models = session.query(CategoryModel).all()
            return [map_model_to_category(m) for m in models]
        finally:
            session.close()

    def get_category_by_id(self, category_id: int) -> Optional[Category]:
        session = SessionLocal()
        try:
            model = (
                session.query(CategoryModel)
                .filter(CategoryModel.id == category_id)
                .first()
            )
            return map_model_to_category(model) if model else None
        finally:
            session.close()

    def create_category(self, category: Category) -> Category:
        session = SessionLocal()
        try:
            model = map_category_to_model(category)
            session.add(model)
            session.commit()
            session.refresh(model)
            return map_model_to_category(model)
        finally:
            session.close()
