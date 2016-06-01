import fdb
import ConfigParser
import ExtraiModulos
import ExtraiProgramas
import ExtraiMenus
import ExtraiRelatorios
import ExtraiAutonomias

Config = ConfigParser.ConfigParser()
Config.read("c:\\ello\\windows\\ello.ini")
caminho = Config.get('Dados', 'Database')
conexao = fdb.connect(caminho, 'sysdba', 'masterkey')


separador = """

/* ******************************************************************************** */
/* ******************************************************************************** */
/* ******************************************************************************** */

"""
def montaprogramas():    
    modulos = ExtraiModulos.executa(conexao)
    modulos = separador + modulos + 'Commit;'
    
    programas = ExtraiProgramas.executa(conexao)
    programas = separador + programas + 'Commit;'
    
    menus = ExtraiMenus.executa(conexao)
    menus = separador + menus + 'Commit;'
    
    relatorios = ExtraiRelatorios.executa(conexao)
    relatorios = separador + relatorios + 'Commit;'
    
    autonomia = ExtraiAutonomias.executa(conexao)
    autonomia = separador + autonomia + 'Commit;'    
 
    return  modulos + programas + menus + relatorios + autonomia

arq = open("Programas.sql", "w")
arq.write(montaprogramas())
arq.close()
