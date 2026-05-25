#%%
from src.extract import carregar_dados
from src.transform import transformar_dados

from src.analysis import (
    faturamento_por_mes,
    lucro_mensal,
    segmentos_que_mais_faturam,
    segmentos_que_mais_lucram,
    categorias__que_mais_faturam,
    categorias_que_mais_lucram,
    subcategorias_que_mais_faturam,
    subcategorias_que_mais_lucram,
    relacao_lucro_desconto,
    margem,
    ticket,
    regioes_lucrativas
)

from src.visualization import (
    grafico_faturamento_por_mes,
    grafico_lucro_por_mes,
    grafico_segmentos__que_mais_faturam,
    grafico_segmentos__que_mais_lucram,
    grafico_categorias__que_mais_faturam,
    grafico_categorias__que_mais_lucram,
    grafico_subcategorias_que_mais_faturam,
    grafico_subcategorias_que_mais_lucram,
    grafico_relacao_desconto_lucro,
    grafico_margem_percentual,
    grafico_regioes_mais_lucrativas
)


df = carregar_dados("data/raw/Global Superstore.xls")

df = transformar_dados(df)


faturamento = faturamento_por_mes(df)
lucro = lucro_mensal(df)
segmentos_faturamento = segmentos_que_mais_faturam(df)
segmentos_lucro = segmentos_que_mais_lucram(df)
categorias_faturamento = categorias__que_mais_faturam(df)
categorias_lucro = categorias_que_mais_lucram(df)
subcategorias_faturamento = subcategorias_que_mais_faturam(df)
subcategorias_lucro = subcategorias_que_mais_lucram(df)
desconto_lucro = relacao_lucro_desconto(df)
margem_categoria = margem(df)
ticket_medio = ticket(df)
regioes_lucro = regioes_lucrativas(df)


grafico_faturamento_por_mes(faturamento)
grafico_lucro_por_mes(lucro)
grafico_segmentos__que_mais_faturam(segmentos_faturamento)
grafico_segmentos__que_mais_lucram(segmentos_lucro)
grafico_categorias__que_mais_faturam(categorias_faturamento)
grafico_categorias__que_mais_lucram(categorias_lucro)
grafico_subcategorias_que_mais_faturam(subcategorias_faturamento)
grafico_subcategorias_que_mais_lucram(subcategorias_lucro)
grafico_relacao_desconto_lucro(desconto_lucro)
grafico_margem_percentual(margem_categoria)
grafico_regioes_mais_lucrativas(regioes_lucro)


print(f"Ticket médio por pedido: {ticket_medio:.2f}")