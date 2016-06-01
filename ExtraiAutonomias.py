# coding=UTF-8
import fdb
import ConfigParser

Config = ConfigParser.ConfigParser()
Config.read("c:\\ello\\windows\\ello.ini")
caminho = Config.get('Dados', 'Database')
conexao = fdb.connect(caminho, 'sysdba', 'masterkey')
 
cursor = conexao.cursor()
cursor.execute("""SELECT IDAUTONOMIA, IDAUTONOMIAPARENT, 
                         MODULO, DESCRICAO,
                         MENSAGEM, PADRAO,
                         TIPOVALOR, VISIVEL 
                  FROM TGERAUTONOMIA ORDER BY 1""")

query = ("UPDATE OR INSERT INTO TGERRELATORIOS (IDAUTONOMIA, "
         "IDAUTONOMIAPARENT, MODULO, DESCRICAO,"
         "MENSAGEM, PADRAO, TIPOVALOR, VISIVEL "
         "VALUES ({0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}'); ")

for row in cursor:
    IDAUTONOMIA, IDAUTONOMIAPARENT, MODULO, DESCRICAO, MENSAGEM, PADRAO, TIPOVALOR, VISIVEL = row
    print query.format(IDAUTONOMIA, IDAUTONOMIAPARENT, MODULO, DESCRICAO, MENSAGEM, PADRAO, TIPOVALOR, VISIVEL)
