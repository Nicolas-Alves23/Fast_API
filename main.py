from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

class Banco(BaseModel):
    nome: str 
    cor:str 
    ano_da_descoberta: int

app = FastAPI()


# Base de dados 
flores = {
   1: { "nome": "Rosa", "cor": "Vermelha", "ano da descoberta": 1800 },
   2: { "nome": "Orquídea", "cor": "Branca", "ano da descoberta": 1822 },
   3: { "nome": "Tulipa", "cor": "Amarela", "ano da descoberta": 1600 },
   4: { "nome": "Margarida", "cor": "Branca", "ano da descoberta": 1700 },
   5: { "nome": "Girassol", "cor": "Amarela", "ano da descoberta": 1602 },
   6: { "nome": "Lírio", "cor": "Branco", "ano da descoberta": 1701 },
   7: { "nome": "Violeta", "cor": "Roxa", "ano da descoberta": 1840 },
   8: { "nome": "Camélia", "cor": "Rosa", "ano da descoberta": 1809 },
   9: { "nome": "Jasmim", "cor": "Branco", "ano da descoberta": 1500 },
   10: { "nome": "Crisântemo", "cor": "Amarela", "ano da descoberta": 1400 },
   11: { "nome": "Lavanda", "cor": "Roxa", "ano da descoberta": 1800 },
   12: { "nome": "Dália", "cor": "Vermelha", "ano da descoberta": 1750 },
   13: { "nome": "Lótus", "cor": "Branca", "ano da descoberta": 3000 },
   14: { "nome": "Tulipa Negra", "cor": "Preta", "ano da descoberta": 1850 },
   15: { "nome": "Íris", "cor": "Azul", "ano da descoberta": 1595 },
   17: { "nome": "Gardênia", "cor": "Branca", "ano da descoberta": 1755 },
   18: { "nome": "Azaleia", "cor": "Rosa", "ano da descoberta": 1855 },
   19: { "nome": "Begônia", "cor": "Rosa", "ano da descoberta": 1683 },
   20: { "nome": "Magnólia", "cor": "Branca", "ano da descoberta": 1681 },
   21: { "nome": "Amarílis", "cor": "Vermelha", "ano da descoberta": 1770 },
   22: { "nome": "Anêmona", "cor": "Branca", "ano da descoberta": 1600 },
   23: { "nome": "Hibisco", "cor": "Vermelho", "ano da descoberta": 1750 },
   24: { "nome": "Narciso", "cor": "Amarelo", "ano da descoberta": 1776 },
   25: { "nome": "Miosótis", "cor": "Azul", "ano da descoberta": 1800 },
   26: { "nome": "Camomila", "cor": "Branca", "ano da descoberta": 1600 },
   27: { "nome": "Peônia", "cor": "Rosa", "ano da descoberta": 1805 },
   28: { "nome": "Gerânio", "cor": "Vermelho", "ano da descoberta": 1750 },
   29: { "nome": "Cinerária", "cor": "Azul", "ano da descoberta": 1900 },
   30: { "nome": "Bromélia", "cor": "Vermelha", "ano da descoberta": 1870 },
   31: { "nome": "Dente-de-leão", "cor": "Amarelo", "ano da descoberta": 1700 },
   32: { "nome": "Lúpulo", "cor": "Verde", "ano da descoberta": 1500 }
}

# Lista de todos os itens dentro da API (Flores) /\⬆️
@app.get("/")
async def listar_flores():
    return flores

# Procurar com ID
@app.get("/flores/{id}")
async def listar_flor_por_id(id: int):
    
    if id not in flores:
        raise HTTPException(status_code=404, detail="Flor não encontrada")
    return flores[id]

# Query params ⬇️
@app.get("/jardim/")
async def buscar_flor_por_nome_e_cor(nome: str, cor: str):
    # Filtra as flores com base no nome e na cor
    resultados = [flor for flor in flores.values() if flor["nome"].lower() == nome.lower() or flor["cor"].lower() == cor.lower()]
    
    # Se não encontrar nenhuma flor que atenda aos critérios, retorna um erro
    if not resultados:
        raise HTTPException(status_code=404, detail="Flor não encontrada com o nome e cor especificados.")
    
    return {"flores": resultados}


# Request Body ⬇️ 
@app.post("/flores/")
async def adicionar_flor(flor: Banco):
    # Gerando um novo ID
    new_id = max(flores.keys()) + 1
    # Definindo como o texto vai ficar
    flores[new_id] = flor.dict()
    # Salvando os dados 🎲
    return {"id": new_id, "nome": flor.nome, "cor": flor.cor, "ano da descoberta": flor.ano_da_descoberta}

# Método PUT
@app.put("/flores/{id}")
async def atualizar_flor(id:int, flor:Banco):
    # Caso id não esteja dentro ❌
    if id not in flores:
        raise HTTPException(status_code=404, detail="Flor não encontrada")

    # Subindo as novas informações do usuário 🖥️
    flores[id] = flor.dict()

    return {"id":id, **flor.dict()}


