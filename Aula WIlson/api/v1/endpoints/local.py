from typing import List
from fastapi import APIRouter, status, Depends, HTTPException, Response

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from Models.local_model import LocalModel
from shecmas.local_shecmas import LocalSchema

from core.deps import get_session

router = APIRouter()

@router.post("",status_code=status.HTTP_201_CREATED, response_model=LocalSchema)
async def post_local(local: LocalSchema, db: AsyncSession = Depends(get_session)):
    novo_local = LocalModel(
        nome=local.nome,
        relation=local.relation,
        foto=local.foto                      
    )
    db.add(novo_local)
    await db.commit()
    
    return novo_local


@router.get("/", response_model=List[LocalSchema])
async def get_profissoes(db: AsyncSession = Depends(get_session)):
    async with db  as session:
        query = select(LocalModel)
        result = await session.execute(query)
        locais: List[LocalModel] = result.scalars().all()
        
        return locais
    
@router.get("/{local_id}", response_model=LocalSchema)
async def get_local(local_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(LocalModel).filter(LocalModel.id == local_id)
        result = await session.execute(query)
        local = result.scalar_one_or_none()
        
        if local:
            return local
        else:
            raise HTTPException(detail="Profissão não encontrada", status_code=status.HTTP_404_NOT_FOUND)
@router.put("/{local_id}", response_model=LocalSchema, status_code=status.HTTP_202_ACCEPTED)
async def put_local(local_id: int, local: LocalSchema, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(LocalModel).filter(LocalModel.id == local_id)
        result = await session.execute(query)
        local_up = result.scalar_one_or_none()
        
        if local_up:
            local_up.nome = local.nome
            local_up.relation = local.relation
            local_up.foto = local.foto
            
            await session.commit()
            return local_up
        else:
            raise HTTPException(detail="Profissão não encontrada", status_code=status.HTTP_404_NOT_FOUND)

@router.delete("/{local_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_local(local_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(LocalModel).filter(LocalModel.id == local_id)
        result = await session.execute(query)
        local_del = result.scalar_one_or_none()
        
        if local_del:
            await session.delete(local_del)
            await session.commit()
            return Response(status_code=status.HTTP_204_NO_CONTENT)
        else:
            raise HTTPException(detail="Profissão não encontrada", status_code=status.HTTP_404_NOT_FOUND)

