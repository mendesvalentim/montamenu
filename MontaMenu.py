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

def modulos():
    modulo = ExtraiModulos.executa(conexao)
    modulo = separador + modulo + 'COMMIT WORK;'
    arq = open("Modulos.sql", "w")
    arq.write(modulo)
    arq.close()   
    return modulo
    
def programas():
    programa = ExtraiProgramas.executa(conexao)
    programa = separador + programa + 'COMMIT WORK;'
    arq = open("Programas.sql", "w")
    arq.write(programa)
    arq.close()   
    return programa

def menus():
    menu = ExtraiMenus.executa(conexao)
    menu = separador + menu + 'COMMIT WORK;'    
    arq = open("Menus.sql", "w")
    arq.write(menu)
    arq.close()  
    return menu

def relatorios():
    relatorio = ExtraiRelatorios.executa(conexao)
    relatorio = separador + relatorio + 'COMMIT WORK;'
    arq = open("Relatorios.sql", "w")
    arq.write(relatorio)
    arq.close()       
    return relatorio  

def autonomias():
    autonomia = ExtraiAutonomias.executa(conexao)
    autonomia = separador + autonomia + 'COMMIT WORK;'        
    arq = open("Autonimias.sql", "w")
    arq.write(autonomia)
    arq.close()       
    return autonomia

def montaprogramas():    
    return  modulos() + programas() + menus() + relatorios()
    
arq = open("MenuCompleto.sql", "w")
arq.write(montaprogramas())
arq.close()
