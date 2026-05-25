import pandas as pd

#Analise das Kpis
# %%
# Faturamento por mes

def faturamento_por_mes(df):

    faturamento_por_mes = df.groupby(["mes_do_pedido","mes_do_pedido_int"]).agg({"Vendas":"sum"})
    faturamento_por_mes = faturamento_por_mes.sort_values(["mes_do_pedido_int"]).reset_index()

    return faturamento_por_mes



# %%
#Lucro por mes
def lucro_mensal(df):
    lucro_por_mes = df.groupby(["mes_do_pedido","mes_do_pedido_int"]).agg({"Lucro":"sum"})
    lucro_por_mes = lucro_por_mes.sort_values(["mes_do_pedido_int"]).reset_index()
    return lucro_por_mes

# %%
#Segmentos que mais faturam
def segmentos_que_mais_faturam(df):
    segmentos__que_mais_faturam = df.groupby("Segmento").agg({"Vendas":"sum"}).sort_values(by="Vendas")
    segmentos__que_mais_faturam = segmentos__que_mais_faturam.reset_index()
    return segmentos__que_mais_faturam

# %%
#Segmentos que mais Lucram
def segmentos_que_mais_lucram(df):
    segmentos__que_mais_lucram = df.groupby("Segmento").agg({"Lucro":"sum"}).sort_values(by="Lucro")
    segmentos__que_mais_lucram = segmentos__que_mais_lucram.reset_index()
    return segmentos__que_mais_lucram

# %%
#categorias que mais faturam

def categorias__que_mais_faturam(df):
    categorias__que_mais_fatura = df.groupby("Categoria").agg({"Vendas":"sum"}).sort_values(by="Vendas")
    categorias__que_mais_fatura = categorias__que_mais_fatura.reset_index()
    return categorias__que_mais_fatura

# %%
#categorias que mais lucram
def categorias_que_mais_lucram(df):
    categorias__que_mais_lucram = df.groupby("Categoria").agg({"Lucro":"sum"}).sort_values(by="Lucro")
    categorias__que_mais_lucram = categorias__que_mais_lucram.reset_index()
    return categorias__que_mais_lucram


# %%
#subcategorias que mais faturam 

def subcategorias_que_mais_faturam(df):
    subcategorias_que_mais_fatura  = df.groupby("Subcategoria").agg({"Vendas":"sum"}).sort_values(by="Vendas")
    subcategorias_que_mais_fatura = subcategorias_que_mais_fatura.reset_index()
    return subcategorias_que_mais_fatura


# %%
#subcategorias que mais lucram

def subcategorias_que_mais_lucram(df):
    subcategorias_que_mais_lucra  = df.groupby("Subcategoria").agg({"Lucro":"sum"}).sort_values(by="Lucro")
    subcategorias_que_mais_lucra= subcategorias_que_mais_lucra.reset_index()
    return subcategorias_que_mais_lucra


# %%
#relacao entre desconto e lucro

def relacao_lucro_desconto(df):
    relacao_desconto_lucro = df.groupby(by="Desconto").agg({"Lucro":"mean"})
    relacao_desconto_lucro = relacao_desconto_lucro.reset_index()
    return relacao_desconto_lucro

# %%
#margem por categoria

def margem(df):
    margem_percentual = df.groupby("Categoria").agg({"Lucro":"sum","Vendas":"sum"})
    margem_percentual = margem_percentual.reset_index()
    margem_percentual["Margem_por_categoria"] = (margem_percentual["Lucro"]/margem_percentual["Vendas"])*100
    return margem_percentual


# %%
#ticket médio
def ticket(df):

    ticket_medio = df.groupby("ID_do_Pedido").agg({"Vendas":"sum"})
    ticket_medio = ticket_medio.reset_index()
    ticket_medio =ticket_medio["Vendas"].mean()
    return ticket_medio
# %%
#regiões mais lucrativas
def regioes_lucrativas(df):

    regioes_mais_lucrativas = df.groupby("Região").agg({"Lucro":"sum"})
    regioes_mais_lucrativas = regioes_mais_lucrativas.reset_index()
    regioes_mais_lucrativas = regioes_mais_lucrativas.sort_values(by="Lucro")
    return regioes_mais_lucrativas



