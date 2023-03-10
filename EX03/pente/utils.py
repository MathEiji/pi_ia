import numpy as np
from movimento import Movimento

class Utils:

    def subir_vertical(movimento: Movimento, iterator: int):
        var_x = movimento.linha - iterator
        var_y = movimento.coluna
        return var_x, var_y
    
    def descer_vertical(movimento: Movimento, iterator: int):
        var_x = movimento.linha + iterator
        var_y = movimento.coluna
        return var_x, var_y
    
    def direita_horizontal(movimento: Movimento, iterator: int):
        var_x = movimento.linha
        var_y = movimento.coluna + iterator
        return var_x, var_y

    def esquerda_horizontal(movimento: Movimento, iterator: int):
        var_x = movimento.linha
        var_y = movimento.coluna - iterator
        return var_x, var_y

    def subir_diagonald(movimento: Movimento, iterator: int):
        var_x = movimento.linha - iterator
        var_y = movimento.coluna + iterator
        return var_x, var_y
    
    def descer_diagonald(movimento: Movimento, iterator: int):
        var_x = movimento.linha + iterator
        var_y = movimento.coluna + iterator
        return var_x, var_y
    
    def subir_diagonale(movimento: Movimento, iterator: int):
        var_x = movimento.linha - iterator
        var_y = movimento.coluna - iterator
        return var_x, var_y
    
    def descer_diagonale(movimento: Movimento, iterator: int):
        var_x = movimento.linha + iterator
        var_y = movimento.coluna - iterator
        return var_x, var_y
    
    def cor_oposta(movimento: Movimento):
        if movimento.cor == 'P':
            return 'B'
        else:
            return 'P'

    def gera_possibilidades_horizontal(movimento: Movimento):
        consec_d = ''
        consec_e = ''
        linha = movimento.linha 
        coluna = movimento.coluna
        print(linha, coluna)

        for i in range(5):
            col_e = coluna + (-i - 1)
            col_d = coluna + (i + 1)
            if i == 0:
                if col_e>=0:
                    consec_e = np.array([[linha, col_e]])
                if col_d<19:    
                    consec_d = np.array([[linha, col_d]])
                # possibilidades = np.insert(possibilidades,len(possibilidades) , tmp)
            elif i>0:
                if col_e >= 0:
                    if type(consec_e) is not str:
                        tmp = np.array([[linha, col_e]])
                        consec_e = np.insert(consec_e,len(consec_e) , tmp, axis=0)
                    else:
                        consec_e = np.array([[linha, col_e]])
                if col_d < 19:
                    if type(consec_d) is not str:
                        tmp = np.array([[linha, col_d]])
                        consec_d = np.insert(consec_d,len(consec_d) , tmp, axis=0)
                    else:
                        consec_d = np.array([[linha, col_d]])

        return consec_e, consec_d
    

    def gera_possibilidades_vertical(movimento: Movimento):
        consec_up = ''
        consec_down = ''
        linha = movimento.linha 
        coluna = movimento.coluna
        print(linha, coluna)

        for i in range(5):
            linha_up = linha + (-i - 1)
            linha_down = linha + (i + 1)
            if i == 0:
                if linha_up >= 0:
                    consec_up = np.array([[linha_up, coluna]])
                if linha_down < 19:
                    consec_down = np.array([[linha_down, coluna]])
            elif i>0:
                if linha_up >= 0:
                    if type(consec_up) is not str:
                        tmp = np.array([[linha_up, coluna]])
                        consec_up = np.insert(consec_up,len(consec_up) , tmp, axis=0)
                    else:
                        consec_up = np.array([[linha_up, coluna]])
                if linha_down < 19:
                    if type(consec_down) is not str:
                        tmp = np.array([[linha_down, coluna]])
                        consec_down = np.insert(consec_down,len(consec_down) , tmp, axis=0)
                    else:
                        consec_down = np.array([[linha_down, coluna]])

        return consec_up, consec_down
    