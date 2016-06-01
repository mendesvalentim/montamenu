# coding=UTF-8

def executa(conexao):
    cursor = conexao.cursor()
    cursor.execute("""SELECT IDPROGRAMA, PROGRAMA, DESCRICAO, OBSERVACAO, TIPO,
                    MODULO, IDPESQUISA,PESQINCREMENTAL, TAG, COMISSAO
                    FROM TGERPROGRAMA ORDER BY 1""")
    
    query = ("UPDATE OR INSERT INTO TGERPROGRAMA(IDPROGRAMA, PROGRAMA, DESCRICAO,"
            "OBSERVACAO, TIPO, MODULO, IDPESQUISA, PESQINCREMENTAL, TAG, COMISSAO)"
            "VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}', '{8}', '{9}' );\n ")
    programas = ''
    for row in cursor:
        IDPROGRAMA, PROGRAMA, DESCRICAO, OBSERVACAO, TIPO, MODULO, IDPESQUISA,PESQINCREMENTAL, TAG, COMISSAO = row
        programas = programas + query.format(IDPROGRAMA, PROGRAMA, DESCRICAO, OBSERVACAO, TIPO, MODULO, IDPESQUISA,PESQINCREMENTAL, TAG, COMISSAO)    
    
    cursor.close()
    return programas