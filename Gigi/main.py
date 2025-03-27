from fastapi import FastAPI, HTTPException

app = FastAPI()

Receitas = {
    1: {"nome_receita": "Strogonoff de Frango", "Ingredientes": "Creme de leite, Frango, Champignon", "Tempo_Preparo": 60},
    2: {"nome_receita": "Bolo de Cenoura", "Ingredientes": "Cenoura, Açúcar, Farinha, Cobertura de Chocolate", "Tempo_Preparo": 90},
    3: {"nome_receita": "Lasanha à Bolonhesa", "Ingredientes": "Massa de Lasanha, Molho de Tomate, Carne Moída, Queijo", "Tempo_Preparo": 120},
    4: {"nome_receita": "Panquecas Simples", "Ingredientes": "Farinha, Leite, Ovos, Recheio a gosto", "Tempo_Preparo": 30},
    5: {"nome_receita": "Pudim de Leite", "Ingredientes": "Leite Condensado, Leite, Ovos, Açúcar para Caramelo", "Tempo_Preparo": 180},
    6: {"nome_receita": "Feijoada", "Ingredientes": "Feijão Preto, Carnes Variadas, Farinha, Laranja", "Tempo_Preparo": 240},
    7: {"nome_receita": "Macarrão ao Alho e Óleo", "Ingredientes": "Macarrão, Alho, Azeite, Sal", "Tempo_Preparo": 20},
    8: {"nome_receita": "Pizza Caseira", "Ingredientes": "Massa de Pizza, Molho, Queijo, Coberturas a gosto", "Tempo_Preparo": 120},
    9: {"nome_receita": "Arroz de Forno", "Ingredientes": "Arroz, Queijo, Presunto, Molho de Tomate", "Tempo_Preparo": 40},
    10: {"nome_receita": "Quiche de Queijo", "Ingredientes": "Farinha, Manteiga, Ovos, Queijo", "Tempo_Preparo": 90},
    11: {"nome_receita": "Empadão de Frango", "Ingredientes": "Frango Desfiado, Massa, Creme de Leite", "Tempo_Preparo": 120},
    12: {"nome_receita": "Salada Caesar", "Ingredientes": "Alface, Croutons, Molho Caesar, Frango Grelhado", "Tempo_Preparo": 15},
    13: {"nome_receita": "Sopa de Legumes", "Ingredientes": "Legumes Variados, Caldo de Galinha", "Tempo_Preparo": 40},
    14: {"nome_receita": "Brigadeiro", "Ingredientes": "Leite Condensado, Chocolate em Pó, Manteiga, Granulado", "Tempo_Preparo": 20},
    15: {"nome_receita": "Escondidinho de Carne", "Ingredientes": "Purê de Batata, Carne Moída, Queijo", "Tempo_Preparo": 60},
    16: {"nome_receita": "Torta de Limão", "Ingredientes": "Biscoito, Leite Condensado, Limão", "Tempo_Preparo": 90},
    17: {"nome_receita": "Coxinha", "Ingredientes": "Massa de Batata, Frango Desfiado", "Tempo_Preparo": 120},
    18: {"nome_receita": "Tapioca", "Ingredientes": "Goma de Tapioca, Recheio a gosto", "Tempo_Preparo": 10},
    19: {"nome_receita": "Churros", "Ingredientes": "Massa de Churros, Açúcar, Doce de Leite", "Tempo_Preparo": 60},
    20: {"nome_receita": "Hambúrguer Caseiro", "Ingredientes": "Pão de Hambúrguer, Carne Moída, Queijo, Alface, Tomate", "Tempo_Preparo": 30},
    21: {"nome_receita": "Cachorro-Quente", "Ingredientes": "Pão, Salsicha, Molho de Tomate", "Tempo_Preparo": 15},
    22: {"nome_receita": "Cuscuz", "Ingredientes": "Farinha de Milho, Água, Sal, Manteiga", "Tempo_Preparo": 20},
    23: {"nome_receita": "Peixe Assado", "Ingredientes": "Peixe, Limão, Temperos", "Tempo_Preparo": 60},
    24: {"nome_receita": "Carne de Panela", "Ingredientes": "Carne, Batata, Cenoura, Molho de Tomate", "Tempo_Preparo": 120},
    25: {"nome_receita": "Yakissoba", "Ingredientes": "Macarrão, Legumes, Molho Shoyu, Carne ou Frango", "Tempo_Preparo": 40},
    26: {"nome_receita": "Risoto de Frango", "Ingredientes": "Arroz Arbóreo, Frango, Caldo de Galinha, Queijo", "Tempo_Preparo": 50},
    27: {"nome_receita": "Bolinho de Chuva", "Ingredientes": "Farinha, Ovos, Açúcar, Canela", "Tempo_Preparo": 30},
    28: {"nome_receita": "Moqueca de Peixe", "Ingredientes": "Peixe, Leite de Coco, Pimentão, Dendê", "Tempo_Preparo": 90},
    29: {"nome_receita": "Frango Xadrez", "Ingredientes": "Frango, Pimentão, Amendoim, Molho Shoyu", "Tempo_Preparo": 40},
    30: {"nome_receita": "Curau de Milho", "Ingredientes": "Milho, Leite, Açúcar", "Tempo_Preparo": 60}
}

@app.get("/") #Visuaizar todas as receitas
async def ListReceitas():
    return Receitas

@app.get("/idreceita/{id_receita}") #Buscando receita pelo ID
async def Buscar_IDReceita(id_receita: int): #Define que o tipo da id é int
    if id_receita in Receitas:
        return Receitas[id_receita]
    else:
        raise HTTPException(status_code=404, detail="ID inexistente")

@app.get("/nomereceita/{nome_receita}") #Buscando receita pelo nome
async def Buscar_NOMEReceita(nome_receita: str):
    resposta = [receitas for receitas in Receitas.values() if receitas["nome_receita"].lower() == nome_receita.lower()]
    if not resposta:
        raise HTTPException(status_code=404, detail="Receita não cadastrada")
    return {"Receitas": resposta}
   