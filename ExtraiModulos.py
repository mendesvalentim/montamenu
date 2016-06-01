# coding=UTF-8
import fdb
import ConfigParser

Config = ConfigParser.ConfigParser()
Config.read("c:\\ello\\windows\\ello.ini")
caminho = Config.get('Dados', 'Database')
conexao = fdb.connect(caminho, 'sysdba', 'masterkey')
 
cursor = conexao.cursor()
cursor.execute("""SELECT IDMODULO, DESCRICAO, TIPOEMPRESA 
                  FROM TGERMODULO ORDER BY 1""")

query = ("UPDATE OR INSERT NTO TGERMODULO (IDMODULO, DESCRICAO, TIPOEMPRESA) VALUES ('{0}', '{1}', '{2}'); ")

for row in cursor:
    IDMODULO, DESCRICAO, TIPOEMPRESA = row
    print query.format(IDMODULO, DESCRICAO, TIPOEMPRESA)