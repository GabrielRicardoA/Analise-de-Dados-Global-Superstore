import matplotlib.pyplot as plt
#Analise das Kpis
# %%
# Faturamento por mes

def grafico_faturamento_por_mes(faturamento):

    plt.figure(figsize=(8,4))
    plt.plot(faturamento["mes_do_pedido"],faturamento["Vendas"],color="blue",marker="o")
    plt.title("Faturamento por Mes")
    plt.xlabel("Meses")
    plt.xticks(rotation=45)
    plt.ylabel("Faturamento")
    plt.tight_layout()
    plt.grid(axis="y",alpha=0.4)
    plt.savefig("images/faturamento_por_mes.png")
    plt.show()



# %%
#Lucro por mes

def grafico_lucro_por_mes(lucro_por_mes):
    plt.figure(figsize=(8,4))
    plt.plot(lucro_por_mes["mes_do_pedido"],lucro_por_mes["Lucro"],color="green",marker="o")
    plt.title("Lucro por mes")
    plt.xlabel("Meses")
    plt.xticks(rotation=45)
    plt.ylabel("Lucro")
    plt.tight_layout()
    plt.grid(axis="y",alpha=0.4)
    plt.savefig("images/lucro_por_mes.png")
    plt.show()

# %%
#Segmentos que mais faturam
def grafico_segmentos__que_mais_faturam(segmentos__que_mais_faturam):

    plt.figure(figsize=(8,4))
    plt.bar(segmentos__que_mais_faturam["Segmento"],segmentos__que_mais_faturam["Vendas"],color="blue")
    plt.title("Segmentos que mais faturam")
    plt.xlabel("Segmentos")
    plt.ylabel("Vendas")
    plt.tight_layout()
    plt.grid(axis="y",alpha=1)
    plt.savefig("images/segmento_mais_faturam.png")
    plt.show()

# %%
#Segmentos que mais Lucram

def grafico_segmentos__que_mais_lucram(segmentos__que_mais_lucram):
    plt.figure(figsize=(8,4))
    plt.bar(segmentos__que_mais_lucram["Segmento"],segmentos__que_mais_lucram["Lucro"],color="green")
    plt.title("Segmentos que mais Lucram")
    plt.xlabel("Segmentos")
    plt.ylabel("Lucro")
    plt.tight_layout()
    plt.grid(axis="y",alpha=1)
    plt.savefig("images/segmento_mais_lucram.png")
    plt.show()

# %%
#categorias que mais faturam

def grafico_categorias__que_mais_faturam(categorias__que_mais_faturam):

    plt.figure(figsize=(8,4))
    plt.bar(categorias__que_mais_faturam["Categoria"],categorias__que_mais_faturam["Vendas"],color="blue")
    plt.title("Categorias que mais faturam")
    plt.xlabel("Categoria")
    plt.ylabel("Vendas")
    plt.tight_layout()
    plt.grid(axis="y",alpha=1)
    plt.savefig("images/categorias__que_mais_faturam.png")
    plt.show()
# %%
#categorias que mais lucram

def grafico_categorias__que_mais_lucram(categorias__que_mais_lucram):
    plt.figure(figsize=(8,4))
    plt.bar(categorias__que_mais_lucram["Categoria"],categorias__que_mais_lucram["Lucro"],color="green")
    plt.title("Categorias que mais lucram")
    plt.xlabel("Categoria")
    plt.ylabel("Lucro")
    plt.tight_layout()
    plt.grid(axis="y",alpha=1)
    plt.savefig("images/categorias__que_mais_lucram.png")
    plt.show()

# %%
#subcategorias que mais faturam 

def grafico_subcategorias_que_mais_faturam(subcategorias_que_mais_faturam):

    plt.figure(figsize=(8,4))
    plt.barh(subcategorias_que_mais_faturam["Subcategoria"],subcategorias_que_mais_faturam["Vendas"],color="blue")
    plt.title("Categorias que mais faturam")
    plt.xlabel("Subcategoria")
    plt.ylabel("Vendas")
    plt.tight_layout()  
    plt.grid(axis="x",alpha=1)
    plt.savefig("images/subcategorias_que_mais_faturam.png")
    plt.show()

# %%
#subcategorias que mais lucram
def grafico_subcategorias_que_mais_lucram(subcategorias_que_mais_lucram):
    plt.figure(figsize=(8,4))
    plt.barh(subcategorias_que_mais_lucram["Subcategoria"],subcategorias_que_mais_lucram["Lucro"],color="green")
    plt.title("subcategorias que mais lucram")
    plt.xlabel("Subcategoria")
    plt.ylabel("Lucro")
    plt.tight_layout()
    plt.grid(axis="x",alpha=1)
    plt.savefig("images/subcategorias_que_mais_lucram.png")
    plt.show()

# %%
#relacao entre desconto e lucro
def grafico_relacao_desconto_lucro(relacao_desconto_lucro):

    plt.figure(figsize=(8,4))
    plt.scatter(relacao_desconto_lucro["Desconto"],relacao_desconto_lucro["Lucro"])
    plt.title("relacao entre desconto e lucro")
    plt.xlabel("Desconto")
    plt.ylabel("Lucro")
    plt.tight_layout()
    plt.savefig("images/relacao_desconto_lucro.png")
    plt.show()

# %%
#margem por categoria
def grafico_margem_percentual(margem_percentual):
    plt.bar(margem_percentual["Categoria"],margem_percentual["Margem_por_categoria"],color="green")
    plt.title("Margem de Lucro por categoria")
    plt.xlabel("Categoria")
    plt.ylabel("Margem de Lucro")
    plt.tight_layout()
    plt.savefig("images/margem_percentual.png")
    plt.show()

# %%

# %%
#regiões mais lucrativas
def grafico_regioes_mais_lucrativas(regioes_mais_lucrativas):
    plt.figure(figsize=(8,4))
    plt.barh(regioes_mais_lucrativas["Região"],regioes_mais_lucrativas["Lucro"],color="green")
    plt.title("Regioes mais lucrativas")
    plt.xlabel("Lucro")
    plt.ylabel("Regiao")
    plt.tight_layout()
    plt.savefig("images/regioes_mais_lucrativas.png")
    plt.show()
