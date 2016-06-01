# coding=UTF-8

def executa(conexao):
    cursor = conexao.cursor()
    cursor.execute("""SELECT IDAUTONOMIA, IDAUTONOMIAPARENT, 
                             MODULO, DESCRICAO,
                             MENSAGEM, PADRAO,
                             TIPOVALOR, VISIVEL 
                      FROM TGERAUTONOMIA ORDER BY 1""")

    query = ("UPDATE OR INSERT INTO TGERAUTONOMIA (IDAUTONOMIA, "
             "IDAUTONOMIAPARENT, MODULO, DESCRICAO,"
             "MENSAGEM, PADRAO, TIPOVALOR, VISIVEL "
             "VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}');\n ")
    autonomia = ''
    for row in cursor:
        IDAUTONOMIA, IDAUTONOMIAPARENT, MODULO, DESCRICAO, MENSAGEM, PADRAO, TIPOVALOR, VISIVEL = row
        autonomia = autonomia + query.format(IDAUTONOMIA, IDAUTONOMIAPARENT, MODULO, DESCRICAO, MENSAGEM, PADRAO, TIPOVALOR, VISIVEL)

    cursor.close()
    return autonomia