import numpy as np
from pente import Pente
from movimento import Movimento

if __name__ == "__main__":
    jogo = Pente()
    jogo.print_tabuleiro(jogo.tabuleiro)

    print("Inserir a jogada no seguinte formato: linha,coluna")
    while (jogo.encerrado == 0):
        if (jogo.encerrado == 1):
            break
        v_p = input ("Jogada P :")
        jogo.colocar_peca(Movimento(int(v_p.split(',')[0]), int(v_p.split(',')[1]), 'P'))
        v_b = input ("Jogada B :")
        jogo.colocar_peca(Movimento(int(v_b.split(',')[0]), int(v_b.split(',')[1]), 'B'))
        # Validacao vertical
        # jogo.colocar_peca(Movimento(3,3,'B'))
        # jogo.colocar_peca(Movimento(4,3,'P'))
        # jogo.colocar_peca(Movimento(5,3,'P'))
        # jogo.colocar_peca(Movimento(6,3,'B'))
        # jogo.colocar_peca(Movimento(7,3,'B'))

        # Validacao horizontal
        # jogo.colocar_peca(Movimento(3,3,'B'))
        # jogo.colocar_peca(Movimento(3,4,'P'))
        # jogo.colocar_peca(Movimento(3,5,'P'))
        # jogo.colocar_peca(Movimento(3,6,'B'))
        # jogo.colocar_peca(Movimento(3,7,'B'))

        # Validacao diagonald
        # jogo.colocar_peca(Movimento(11,7,'B'))
        # jogo.colocar_peca(Movimento(15,3,'B'))
        # jogo.colocar_peca(Movimento(14,4,'P'))
        # jogo.colocar_peca(Movimento(13,5,'P'))
        # jogo.colocar_peca(Movimento(12,6,'B'))

        # Validacao diagonale
        # jogo.colocar_peca(Movimento(10,10,'B'))
        # jogo.colocar_peca(Movimento(9,9,'P'))
        # jogo.colocar_peca(Movimento(12,12,'B'))
        # jogo.colocar_peca(Movimento(8,8,'P'))
        # jogo.colocar_peca(Movimento(11,11,'B'))
        # jogo.colocar_peca(Movimento(7,7,'B'))
        # jogo.colocar_peca(Movimento(13,13,'P'))
        # jogo.colocar_peca(Movimento(14,14,'P'))
        # jogo.colocar_peca(Movimento(15,15,'B'))