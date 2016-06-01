# coding=UTF-8
import fdb
import ConfigParser

Config = ConfigParser.ConfigParser()
Config.read("c:\\ello\\windows\\ello.ini")
caminho = Config.get('Dados', 'Database')
conexao = fdb.connect(caminho, 'sysdba', 'masterkey')
 
cursor = conexao.cursor()
cursor.execute("""SELECT IDMENU, IDMENUPARENT, DESCRICAO, TIPO,
                  IMAGEM, IDPROGRAMA, EMPRESA, USUARIO 
                  FROM TGERMENU ORDER BY 1""")

query = ("INSERT INTO TGERMENU (IDMENU, IDMENUPARENT, DESCRICAO, TIPO,"
                                  "IMAGEM, IDPROGRAMA, EMPRESA, USUARIO)"
            "VALUES ({0}, {1}, '{2}', {3}, {4}, {5}, {6}, '{7}' ); ")

for row in cursor:
    IDMENU, IDMENUPARENT, DESCRICAO, TIPO, IMAGEM, IDPROGRAMA, EMPRESA, USUARIO = row
    print query.format(IDMENU, IDMENUPARENT, DESCRICAO, TIPO, IMAGEM, IDPROGRAMA, EMPRESA, USUARIO)
            