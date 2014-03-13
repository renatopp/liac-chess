-------------------
Estado do Tabuleiro
-------------------

O estado do tabuleiro é enviado pelo servidor durante a execução do jogo, e contém todas as informações necessárias para que um bot gere a próxima jogada. Esta seção descreve em detalhes essas informações:

**board**
    É a configuração do tabuleiro representada como uma string de 64 posições. O tabuleiro é representado de cima para baixo, ou seja, o primeiro caractere representa a casa da primeira linha, o segunda caractere representa a segunda cada da primeira linha, e assim por diante, até o último caractere que representa a última casa da última linha. As peças são representadas como sua abreviatura no padrão inglês, ou seja: **K** para o rei, **Q** para a rainha, **R** para as torres, **B** para os bispos, **N** para os cavalos, e **P** para os peões, sendo as letras minúsculas para as peças pretas e maiúsculas para as peças brancas. As casas vazias são representadas com um ponto **.**. Com isso, a posição inicial do xadrez tradicional pode ser descrita como::

        "rnbqkbnrpppppppp................................PPPPPPPPRNBQKBNR"

**enpassant**
    Indica se é possível executar a jogada en passant em alguma posição do tabuleiro. Se existir o en passant, este campo é uma lista de 2 dimensões com a posição, ex: ``[2, 3]``, caso contrário, é ``null``. Note que, este campo mostra a posição anterior ao movimento do peão. Por exemplo, se as preta possuem um peão na posição e4 e um peão branco vai da casa d2 para d4, este campo vai mostrar a casa d3.


**who_moves**
    Indica de quem é a vez de jogar. Um bot só recebe o estado do tabuleiro quando é a sua vez de jogar, assim, este campo será sempre igual em uma partida e o bot pode usá-lo para saber a cor de suas peças. Assume ``-1`` para pretas e ``1`` para brancas.

**bad_move**
    Caso o bot gere uma jogada inválida, o servidor não executa nenhum movimento e envia o mesmo estado para o bot, com este campo em ``true``. Ao enviar para o servidor uma jogada inválida, uma infração é anotada.

**white_infractions**
    Número de infrações do jogador que controla as peças brancas.

**black_infractions**
    Número de infrações do jogador que controla as peças pretas.

**winnner**
    Indica se algum jogador venceu o jogo. Assume o valor ``-1`` para pretas e ``1`` para brancas. Enquanto nenhum jogador obtiver as condições necessárias para a vitória, este campo assume o valor ``0``.

**50moves**
    Indica o andamento da regra das `50 jogadas <https://en.wikipedia.org/wiki/Fifty-move_rule>`_. Assume ``true`` se houve 80 jogadas seguidas (por parte dos dois jogadores) sem nenhuma captura. Ao chegar a 100 jogadas, o jogo empata.

**draw**
    Indica se o jogo empatou, sendo ``true`` ou ``false``.


Note que, ao terminar um jogo (ou seja, ao receber um estado onde o campo **winner** é diferente de ``0`` ou **draw** é ``true``), o bot não deve responder o servidor.
