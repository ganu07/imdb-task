"""
A File to declare base metadata of SQLAlchemy to avoid circular dependency
"""

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

