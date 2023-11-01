from typing import Generator
from sqlalchemy.ext.asyncio import AsyncSession
from core.database import Session

# generetor retorna sem matar o processo, ele coloca como se fosse um break point de onde ele parou, e ele irá rodar a partir disso na próxima vez
async def get_session() -> Generator: # função vai ter como retporno um Generator
    session: AsyncSession = Session()
    try:
        yield session #é um return "sem um return" - ele devolve a sessão mas mantém a função viva!
    finally:
        await session.close() # após utilizar a sessão com o banco, aí sim, finalizamos ela 