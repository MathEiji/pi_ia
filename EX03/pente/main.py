import numpy as np
from pente import Pente
from movimento import Movimento

if __name__ == "__main__":
    jogo = Pente()
    jogo.print_tabuleiro(jogo.tabuleiro)

    # Validacao vertical
    jogo.colocar_peca(Movimento(3,3,'B'))
    jogo.colocar_peca(Movimento(4,3,'B'))
    jogo.colocar_peca(Movimento(5,3,'B'))
    jogo.colocar_peca(Movimento(6,3,'B'))
    jogo.valida_consecutivas(Movimento(7,3,'B'))
    jogo.colocar_peca(Movimento(7,3,'B'))

    # Validacao horizontal
    # jogo.colocar_peca(Movimento(3,3,'B'))
    # jogo.colocar_peca(Movimento(3,5,'B'))
    # jogo.colocar_peca(Movimento(3,7,'B'))
    # jogo.colocar_peca(Movimento(3,6,'B'))
    # jogo.valida_consecutivas(Movimento(3,4,'B'))
    # jogo.colocar_peca(Movimento(3,4,'B'))

    # Validacao diagonald
    # jogo.colocar_peca(Movimento(14,4,'B'))
    # jogo.colocar_peca(Movimento(13,5,'B'))
    # jogo.colocar_peca(Movimento(11,7,'B'))
    # jogo.colocar_peca(Movimento(15,3,'B'))
    # jogo.valida_consecutivas(Movimento(12,6,'B'))
    # jogo.colocar_peca(Movimento(12,6,'B'))

    # Validacao diagonale
    # jogo.colocar_peca(Movimento(10,10,'B'))
    # jogo.colocar_peca(Movimento(9,9,'B'))
    # jogo.colocar_peca(Movimento(12,12,'B'))
    # jogo.colocar_peca(Movimento(8,8,'B'))
    # jogo.valida_consecutivas(Movimento(11,11,'B'))
    # jogo.colocar_peca(Movimento(11,11,'B'))