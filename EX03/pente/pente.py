import numpy as np
from movimento import Movimento
from utils import Utils

class Pente:

  positions =  np.array([['-' for y in range(19)]])

  def __init__(self):
    self.tabuleiro = self.positions
    self.pretos_capturados = 0
    self.brancos_capturados = 0
    for i in range(18):
      self.tabuleiro = np.insert( self.tabuleiro, 1, self.positions, axis=0)
    print(self.tabuleiro.shape)


  def print_tabuleiro(self, tabuleiro):
    status = ""
    for i in range(len(tabuleiro)):
      for j in range(len(tabuleiro[i])):
        tmp = tabuleiro[i][j]
        if j == 18:
          status = status + tmp + "\n"
        else:
          status = status + tmp + " "
    print(status)
  

  def colocar_peca(self, movimento: Movimento):
    if self.validar_jogada(movimento):
      if movimento.cor == 'P':
        self.tabuleiro[movimento.linha][movimento.coluna] = 'P'
      elif movimento.cor == 'B':
        self.tabuleiro[movimento.linha][movimento.coluna] = 'B'
      self.print_tabuleiro(self.tabuleiro)
    else:
      print("JOGADA INVALIDA")


  def consecutivas_horizontal(self, movimento: Movimento): # Valida a existencia de consecutivas na horizontal
    pecas = 1
    for i in range(5):
      coluna_e = movimento.coluna + ((-i) - 1)
      coluna_d = movimento.coluna + (i + 1)
      anterior_e = coluna_e + 1
      anterior_d = coluna_d - 1
      if (anterior_e == movimento.coluna and self.tabuleiro[movimento.linha][coluna_e] == movimento.cor):
        pecas = pecas + 1
      else:
        if self.tabuleiro[movimento.linha][coluna_e] == movimento.cor and self.tabuleiro[movimento.linha][anterior_e] == movimento.cor:
          pecas = pecas + 1

      if (anterior_d == movimento.coluna and self.tabuleiro[movimento.linha][coluna_d] == movimento.cor):
        pecas = pecas + 1
      else:
        if self.tabuleiro[movimento.linha][coluna_d] == movimento.cor and self.tabuleiro[movimento.linha][anterior_d] == movimento.cor:
          pecas = pecas + 1

    if pecas >= 5:
      return 1
    else:
      return 0


  def consecutivas_vertical(self, movimento: Movimento):
    pecas = 1
    for i in range(5):
      linha_s = movimento.linha + ((-i) - 1)
      linha_d = movimento.linha + (i + 1)
      anterior_e = linha_s + 1
      anterior_d = linha_d - 1
      if (anterior_e == movimento.linha and self.tabuleiro[linha_s][movimento.coluna] == movimento.cor):
        pecas = pecas + 1
      else:
        if self.tabuleiro[linha_s][movimento.coluna] == movimento.cor and self.tabuleiro[anterior_e][movimento.coluna] == movimento.cor:
          pecas = pecas + 1

      if (anterior_d == movimento.linha and self.tabuleiro[linha_d][movimento.coluna] == movimento.cor):
        pecas = pecas + 1
      else:
        if self.tabuleiro[linha_d][movimento.coluna] == movimento.cor and self.tabuleiro[anterior_d][movimento.coluna] == movimento.cor:
          pecas = pecas + 1

    if pecas >= 5:
      return 1
    else:
      return 0
  

  def consecutivas_diagonald(self, movimento: Movimento):
    pecas = 1
    for i in range(5):
      var_x_sub = ((-i) - 1)
      var_y_sub = (i + 1)
      x_sub = movimento.linha + var_x_sub
      y_sub = movimento.coluna + var_y_sub
      x_anterior_sub = ((movimento.linha + var_x_sub) + 1)
      y_anterior_sub = ((movimento.coluna + var_y_sub) - 1)

      var_x_dec = (i + 1)
      var_y_dec = ((-i) - 1)
      x_dec = movimento.linha + var_x_dec
      y_dec = movimento.coluna + var_y_dec
      x_anterior_dec = ((movimento.linha + var_x_dec) - 1) 
      y_anterior_dec = ((movimento.coluna + var_y_dec) + 1)

      if (x_anterior_sub == movimento.linha and y_anterior_sub == movimento.coluna and self.tabuleiro[x_sub][y_sub] == movimento.cor):
        pecas = pecas + 1
      else:
        if self.tabuleiro[x_sub][y_sub] == movimento.cor and self.tabuleiro[x_anterior_sub][y_anterior_sub] == movimento.cor:
          pecas = pecas + 1
      
      if (x_anterior_dec == movimento.linha and y_anterior_dec == movimento.coluna and self.tabuleiro[x_dec][y_dec] == movimento.cor):
        pecas = pecas + 1
      else:
        if self.tabuleiro[x_dec][y_dec] == movimento.cor and self.tabuleiro[x_anterior_dec][y_anterior_dec] == movimento.cor:
          pecas = pecas + 1

    if pecas >= 5:
      return 1
    else:
      return 0
  

  def consecutivas_diagonale(self, movimento: Movimento):
    pecas = 1
    for i in range(5):
      var_x_sub = ((-i) - 1)
      var_y_sub = ((-i) - 1)
      x_sub = movimento.linha + var_x_sub
      y_sub = movimento.coluna + var_y_sub
      x_anterior_sub = ((movimento.linha + var_x_sub) + 1)
      y_anterior_sub = ((movimento.coluna + var_y_sub) + 1)

      var_x_dec = (i + 1)
      var_y_dec = (i + 1)
      x_dec = movimento.linha + var_x_dec
      y_dec = movimento.coluna + var_y_dec
      x_anterior_dec = ((movimento.linha + var_x_dec) - 1) 
      y_anterior_dec = ((movimento.coluna + var_y_dec) - 1)

      # Movimento(12,6,'B')          
      print(str(i) + " Anterior "+ str(x_anterior_dec) + "," + str(y_anterior_dec))
      print(str(i) + " Pos " + str(x_dec) + "," + str(y_dec))

      if (x_anterior_sub == movimento.linha and y_anterior_sub == movimento.coluna and self.tabuleiro[x_sub][y_sub] == movimento.cor):
        pecas = pecas + 1
        print("_1_")
      else:
        if self.tabuleiro[x_sub][y_sub] == movimento.cor and self.tabuleiro[x_anterior_sub][y_anterior_sub] == movimento.cor:
          pecas = pecas + 1
          print("_2_")
      
      if (x_anterior_dec == movimento.linha and y_anterior_dec == movimento.coluna and self.tabuleiro[x_dec][y_dec] == movimento.cor):
        pecas = pecas + 1
        print("_3_")
      else:
        if self.tabuleiro[x_dec][y_dec] == movimento.cor and self.tabuleiro[x_anterior_dec][y_anterior_dec] == movimento.cor:
          pecas = pecas + 1
          print("_4_")

    print(pecas)
    if pecas >= 5:
      return 1
    else:
      return 0

  def valida_consecutivas(self, movimento: Movimento): # Testar para validar o vertical e horizontal, diagonal vai precisar realizar um calculo
    # tmp = self.consecutivas_diagonale(movimento)
    # print("ola", tmp)
    if (self.consecutivas_vertical(movimento) or self.consecutivas_horizontal(movimento) or self.consecutivas_diagonald(movimento) or self.consecutivas_diagonale(movimento)):
      return 1
    else:
      return 0


  def validar_fim(self, movimento: Movimento):
    if self.pretos_capturados >= 10: # 10 pecas pretas capturadas, vencedor branco
      return 1
    elif self.brancos_capturados >= 10: # 10 pecas brancas capturadas, vencedor preto
      return 1
    elif len(list(zip(*np.where(self.tabuleiro == '-')))) == 0: # caso nao tenha nenhum espaco no tabuleiro, empate
      return 1
    elif self.valida_consecutivas(movimento):
      return 1
    return 0

  def captura_vertical(self, movimento: Movimento):
      v = np.empty([])
      cor_oposta = Utils.cor_oposta(movimento)
      tmp = 1
      x_sup, y_sup = Utils.subir_vertical(movimento, tmp)
      x_inf, y_inf = Utils.descer_vertical(movimento, tmp)
      if self.tabuleiro[x_sup][y_sup] == cor_oposta and self.tabuleiro[movimento.linha][movimento.coluna] == movimento.cor:
        x_sup1, y_sup1 = Utils.subir_vertical(movimento, (tmp + 1))
        if self.tabuleiro[x_sup1][y_sup1] == cor_oposta: #and self.tabuleiro[x_sup][y_sup] == cor_oposta:
          x_sup2, y_sup2 = Utils.subir_vertical(movimento, (tmp + 2))
          x_sup3, y_sup3 = Utils.subir_vertical(movimento, (tmp + 3))
          if self.tabuleiro[x_sup2][y_sup2] == movimento.cor and  (self.tabuleiro[x_sup3][y_sup3] == '-' or self.tabuleiro[x_sup3][y_sup3] == movimento.cor):
            v1 = np.array([[x_sup, y_sup]])
            v2 = np.array([[x_sup1, y_sup1]])
            v = np.insert( v, 1, v1, axis=0)
            v = np.insert( v, 1, v2, axis=0)
  
      if self.tabuleiro[linha_d][movimento.coluna] == movimento.cor and self.tabuleiro[anterior_d][movimento.coluna] == movimento.cor:
        pecas = pecas + 1
      
      return v

  def validar_captura(self, movimento): #Criar funcao que valida se houve pecas capturadas
    v, h, de, dd = 0
    for i in range(4):
      # vertical
      tmp = i + 1
      tmp_v = Utils.subir_vertical(movimento, tmp)
      # if self.tabuleiro[][]
      
    return 1


  def validar_jogada(self, movimento: Movimento):
    #Valida se a posicao existe no tabuleiro
    if movimento.linha > len(self.tabuleiro[0])-1 or movimento.coluna > len(self.tabuleiro[0])-1:
      return 0
    else:
      # Valida se existe alguma peca na posicao
      if self.tabuleiro[movimento.linha][movimento.coluna] != '-':
        return 0
      else:
        return 1
  