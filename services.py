from sqlalchemy.ext.asyncio import AsyncSession

from settings import async_session
import sqlalchemy as sa

from models import Users


async def save_user_objects(username: str, objects: dict):
    session: AsyncSession = async_session()
    await session.execute(sa.insert(Users).values([{
        "username": username,
        "objects": objects
    }]))
    await session.commit()
    await session.close()

async def get_user_objects(username: str):
    session: AsyncSession = async_session()
    user = await session.scalar(sa.select(Users).where(Users.username == username))
    await session.commit()
    await session.close()
    return user.objects