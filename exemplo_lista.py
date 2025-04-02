# produto: str = "Computador"
# produto2: str = "Mouse"
# produto3: str = "Teclado"

# lista_produtos: list[str] = [produto, produto2, produto3]

# print(lista_produtos)

# lista_produtos.append("Monitor")

# print(lista_produtos)

# lista_produtos.remove("Mouse")

# lista_produtos.copy()

# lista_produtos.count("Computador")

# lista_produtos.index("Computador")

# lista_produtos.insert(0, "Monitor")

# lista_produtos.count("Computador")

import json

dicionario_produtos: dict[str, str] = {
    "produto": "Computador",
    "quantidade": 1,
    "preco": 1000.00
}

dicionario_produtos2: dict[str, str] = {
    "produto": "Mouse",
    "quantidade": 2,
    "preco": 50.00
}

dicionario_produtos3: dict[str, str] = {
    "produto": "Teclado",
    "quantidade": 3,
    "preco": 100.00
}

lista_produtos: list[dict[str, str]] = [dicionario_produtos, dicionario_produtos2, dicionario_produtos3]

print(lista_produtos)


carrinho_compras: str = json.dumps(lista_produtos)

print(carrinho_compras)






print(dicionario_produtos)

dicionario_produtos["quantidade"] = 2