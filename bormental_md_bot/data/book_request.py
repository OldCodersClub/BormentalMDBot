from typing import List, Tuple

from sqlalchemy import ChunkedIteratorResult, select, text
from sqlalchemy.orm import sessionmaker

from bormental_md_bot.data.schemas.books import BookModel


class BookRequest:
    def __init__(self, session: sessionmaker, cb_data: str) -> None:
        self.session: sessionmaker = session
        self.cb_data: str = cb_data

    async def db_get_books_list(self) -> List[Tuple[str, int]]:
        """Получить список книг."""
        async with self.session.begin():
            query: ChunkedIteratorResult = await self.session.execute(  # type: ignore
                select(BookModel.title, BookModel.book_id).where(BookModel.cb_data == self.cb_data)
            )
            books_list: List[Tuple[str, int]] = [(title, book_id) for title, book_id in query]
            return books_list

    async def db_get_book_link(self) -> str:
        """Получить ссылку на книгу."""
        async with self.session.begin():
            query: ChunkedIteratorResult = await self.session.execute(  # type: ignore
                select(BookModel.link).where(BookModel.book_id == int(self.cb_data))
            )
            link: str = query.scalar()
        return link

    async def db_book_interaction(self, field: str, book_id: str) -> str:
        """Взаимодействие с книгой."""
        async with self.session.begin():
            query: ChunkedIteratorResult = await self.session.execute(  # type: ignore
                text(f"SELECT {field} FROM books WHERE book_id = '{book_id}'")
            )
            action: str = query.scalar()
        return action

    async def db_get_prev(self, book_id: str) -> str:
        async with self.session.begin():
            query: ChunkedIteratorResult = await self.session.execute(  # type: ignore
                text(f"SELECT cb_data FROM books WHERE book_id = '{book_id}'")
            )
            cb_data: str = query.scalar()
        return cb_data

    # deprecated
    async def db_check_books(self) -> List[str]:
        """Проверить бд и создать актуальный список книг."""
        async with self.session.begin():
            query = await self.session.execute(  # type: ignore
                select(BookModel.title)
            )
            all_books_list: List[str] = [title[0] for title in query]
        return all_books_list
