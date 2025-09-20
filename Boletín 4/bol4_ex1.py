artigo = "chaveiros"
vendas = 756

if vendas <= 100:
    consumo = "baixo"
elif vendas > 100 and vendas <= 500:
    consumo = "medio"
elif vendas > 500 and vendas <= 1000:
    consumo = "alto"
else:
    consumo = "primeira necesidade"

print(f"O consumo de {artigo} é {consumo}.")