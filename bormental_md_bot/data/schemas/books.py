from sqlalchemy import Column, Integer, TEXT, VARCHAR

from bormental_md_bot.data.base import Base


class BookModel(Base):
    __tablename__ = 'books'

    book_id: Column = Column(Integer, autoincrement=True, primary_key=True)
    title: Column = Column(VARCHAR(128), nullable=False)
    description: Column = Column(TEXT, nullable=True, default='soon')
    reviews: Column = Column(TEXT, nullable=True, default='soon')
    content: Column = Column(TEXT, nullable=True, default='soon')
    link: Column = Column(VARCHAR(128), nullable=False)
    cb_data: Column = Column(VARCHAR(32), nullable=False)
