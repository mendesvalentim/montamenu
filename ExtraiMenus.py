# coding=UTF-8

def executa(conexao):
    cursor = conexao.cursor()
    cursor.execute("""SELECT IDMENU, IDMENUPARENT, DESCRICAO, TIPO, IMAGEM, 
                      IDPROGRAMA, EMPRESA, USUARIO 
                      FROM TGERMENU ORDER BY 1""")
    
    query = ("INSERT INTO TGERMENU (IDMENU, IDMENUPARENT, DESCRICAO, TIPO, "
                                    "IMAGEM, IDPROGRAMA, EMPRESA, USUARIO) "
                "VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}');\n ")
    menus = ''
    for row in cursor:
        IDMENU, IDMENUPARENT, DESCRICAO, TIPO, IMAGEM, IDPROGRAMA, EMPRESA, USUARIO = row
        menus = menus + query.format(IDMENU, IDMENUPARENT, DESCRICAO, TIPO, IMAGEM, IDPROGRAMA, EMPRESA, USUARIO)
            
    cursor.close()
    
    return menus