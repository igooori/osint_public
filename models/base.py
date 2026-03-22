from sqlalchemy.ext.asyncio import create_async_engine,async_sessionmaker
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import  String,BigInteger,Column,Integer

engine = create_async_engine("sqlite+aiosqlite:///osint_bot.db")
class Base(DeclarativeBase): pass
class SearchLog(Base):
    __tablename__ = 'search_logs'
    id = Column(Integer,primary_key=True)
    user_id = Column(BigInteger)
    query = Column(String)
async_session_maker = async_sessionmaker(engine,expire_on_commit=False)

async def save_search(user_id:int,query:str):
    async with async_session_maker() as session:
        async with session.begin():
            new = SearchLog(user_id=user_id,query=query)
            session.add(new)
    print(f"✅ Лог сохранен в БД: {query}")