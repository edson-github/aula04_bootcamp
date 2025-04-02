# crie uma dicionario para armazenar informacoes de um livro
# incluindo titulo, autor, ano de publicacao e genero. Imprima cada informacao em uma linha

from typing import Dict, List

livro: Dict[str, any] = {
    "titulo": "O Senhor dos Anéis",
    "autor": "J.R.R. Tolkien",
    "ano": "1954",
    "genero": "Fantasia"
}

print(livro["titulo"])
print(livro["autor"])
print(livro["ano"])
print(livro["genero"])








