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
    modulos = separador + modulos + 'COMMIT WORK;'
    
    programas = ExtraiProgramas.executa(conexao)
    programas = separador + programas + 'COMMIT WORK;'
    
    menus = ExtraiMenus.executa(conexao)
    menus = separador + menus + 'COMMIT WORK;'
    
    relatorios = ExtraiRelatorios.executa(conexao)
    relatorios = separador + relatorios + 'COMMIT WORK;'
    
    autonomia = ExtraiAutonomias.executa(conexao)
    autonomia = separador + autonomia + 'COMMIT WORK;'    
 
    return  modulos + programas + menus + relatorios + autonomia

arq = open("Programas.sql", "w")
arq.write(montaprogramas())
arq.close()
