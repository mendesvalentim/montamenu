# coding=UTF-8
import fdb
import ConfigParser

Config = ConfigParser.ConfigParser()
Config.read("c:\\ello\\windows\\ello.ini")
caminho = Config.get('Dados', 'Database')
conexao = fdb.connect(caminho, 'sysdba', 'masterkey')
 
cursor = conexao.cursor()
cursor.execute("""SELECT IDRELATORIO, TITULO, TAG, DESCRICAO, CAMINHO, PROGRAMA, USUARIO 
                  FROM TGERRELATORIOS ORDER BY 1""")

query = ("UPDATE OR INSERT INTO TGERRELATORIOS (IDRELATORIO, TITULO, TAG, "
         "DESCRICAO, CAMINHO, PROGRAMA, USUARIO)"
         " VALUES ({0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}'); ")

for row in cursor:
    IDRELATORIO, TITULO, TAG, DESCRICAO, CAMINHO, PROGRAMA, USUARIO = row
    print query.format(IDRELATORIO, TITULO, TAG, DESCRICAO, CAMINHO, PROGRAMA, USUARIO)