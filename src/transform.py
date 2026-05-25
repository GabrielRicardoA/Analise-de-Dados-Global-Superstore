import pandas as pd
def transformar_dados(df):
    df_preenchidos = df.copy()

    df_preenchidos.columns = [
        "ID_da_Linha","ID_do_Pedido",
        "Data_do_Pedido","Data_do_Envio",
        "Modo_de_Envio","ID_do_Cliente",
        "Nome_do_Cliente","Segmento",
        "Cidade","Estado","País",
        "Código_Postal","Mercado","Região",
        "ID_do_Produto","Categoria","Subcategoria",
        "Nome_do_Produto","Vendas","Quantidade",
        "Desconto","Lucro","Custo_do_Frete","Prioridade_do_Pedido"
    ]

    df_preenchidos["mes_do_pedido"] = df_preenchidos["Data_do_Pedido"].dt.month_name(locale="pt_BR.utf8")
    df_preenchidos["mes_do_pedido_int"] = df_preenchidos["Data_do_Pedido"].dt.month

    return df_preenchidos