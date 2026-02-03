from sqlalchemy import Column, Integer, String, Float, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

from .config import DATABASE_URL

Base = declarative_base()


class InventoryItem(Base):
    __tablename__ = 'inventory_items'

    id = Column(Integer, primary_key=True)
    sku = Column(String(50), unique=True, nullable=False)
    name = Column(String(200), nullable=False)
    description = Column(String(500))
    quantity = Column(Integer, default=0)
    unit_price = Column(Float, default=0.0)
    warehouse_location = Column(String(100))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'sku': self.sku,
            'name': self.name,
            'description': self.description,
            'quantity': self.quantity,
            'unit_price': self.unit_price,
            'warehouse_location': self.warehouse_location,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    role = Column(String(20), default='viewer')
    created_at = Column(DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'role': self.role,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }


# Database setup - lazy initialization for testing
engine = None
Session = None


def get_engine():
    global engine
    if engine is None:
        import os
        db_url = os.environ.get('DATABASE_URL', DATABASE_URL)
        engine = create_engine(db_url)
    return engine


def get_session():
    global Session
    if Session is None:
        Session = sessionmaker(bind=get_engine())
    return Session()


def init_db():
    Base.metadata.create_all(get_engine())
