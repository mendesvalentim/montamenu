# coding=UTF-8
import fdb
import ConfigParser

Config = ConfigParser.ConfigParser()
Config.read("c:\\ello\\windows\\ello.ini")
caminho = Config.get('Dados', 'Database')
conexao = fdb.connect(caminho, 'sysdba', 'masterkey')
 
cursor = conexao.cursor()
cursor.execute("""SELECT IDPROGRAMA, PROGRAMA, DESCRICAO, OBSERVACAO, TIPO,
                  MODULO, IDPESQUISA,PESQINCREMENTAL, TAG, COMISSAO
                  FROM TGERPROGRAMA ORDER BY 1""")

query = ("UPDATE OR INSERT INTO TGERPROGRAMA(IDPROGRAMA, PROGRAMA, DESCRICAO,"
         "OBSERVACAO, TIPO, MODULO, IDPESQUISA, PESQINCREMENTAL, TAG, COMISSAO)"
         "VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}', '{8}', '{9}' ); ")

for row in cursor:
    IDPROGRAMA, PROGRAMA, DESCRICAO, OBSERVACAO, TIPO, MODULO, IDPESQUISA,PESQINCREMENTAL, TAG, COMISSAO = row
    
    print query.format(IDPROGRAMA, PROGRAMA, DESCRICAO, OBSERVACAO, TIPO, MODULO, IDPESQUISA,PESQINCREMENTAL, TAG, COMISSAO)    