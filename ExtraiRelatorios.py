# coding=UTF-8

def executa(conexao):
    cursor = conexao.cursor()
    cursor.execute("""SELECT IDRELATORIO, TITULO, TAG, DESCRICAO, CAMINHO, PROGRAMA, USUARIO 
                    FROM TGERRELATORIOS ORDER BY 1""")
    
    query = ("UPDATE OR INSERT INTO TGERRELATORIOS (IDRELATORIO, TITULO, TAG, "
            "DESCRICAO, CAMINHO, PROGRAMA, USUARIO)"
            " VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}');\n ")
    relatorios = ''
    for row in cursor:
        IDRELATORIO, TITULO, TAG, DESCRICAO, CAMINHO, PROGRAMA, USUARIO = row
        relatorios = relatorios + query.format(IDRELATORIO, TITULO, TAG, DESCRICAO, CAMINHO, PROGRAMA, USUARIO)
        
    cursor.close()
    return relatorios