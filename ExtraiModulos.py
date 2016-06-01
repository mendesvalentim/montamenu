# coding=UTF-8

def executa(conexao):
    cursor = conexao.cursor()
    cursor.execute("""SELECT IDMODULO, DESCRICAO, TIPOEMPRESA 
                    FROM TGERMODULO ORDER BY 1""")
    
    query = "UPDATE OR INSERT NTO TGERMODULO (IDMODULO, DESCRICAO, TIPOEMPRESA) VALUES ('{0}', '{1}', '{2}');\n"
    
    modulos = ''
    for row in cursor:
        IDMODULO, DESCRICAO, TIPOEMPRESA = row
        modulos = modulos + query.format(IDMODULO, DESCRICAO, TIPOEMPRESA)
   
    cursor.close()
    
    return modulos

