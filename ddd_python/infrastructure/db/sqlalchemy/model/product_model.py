from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Float
from ddd_python.infrastructure.db.sqlalchemy.config import Base

class ProductModel(Base):
    __tablename__ = "products"

    product_id: Mapped[str] = mapped_column(String, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    price: Mapped[float] = mapped_column(Float, nullable=False)
