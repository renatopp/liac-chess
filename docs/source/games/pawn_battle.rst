=================
Batalha dos Peões
=================

A Batalha dos Peões é uma versão simplificada do jogo tradicional de Xadrez, criada para auxiliar o aprendizado do mesmo. Com regras modificadas, o jogo pode envolver diversas configurações diferentes do tabuleiro, mas sendo sempre utilizado um conjunto de peões e opcionalmente uma ou mais das seguintes peças: cavalo, bispo, torre, ou rainha. O Rei, peça mais importante do Xadrez, obrigatoriamente não é utilizado. 

-------------------------
Configuração do Tabuleiro
-------------------------

A Batalha dos Peões pode ser jogada com diversas configurações diferentes do tabuleiro, mas em todas elas há necessariamente um conjunto de peões dispostos de forma simétrica para os dois jogadores. Além desses peões, é opcional o uso de cavalos, bispos, torres e rainhas. Os dois jogadores precisam ter a mesma quantidade e tipos de peças. 

A configuração mais simples do jogo é um tabuleiro contendo apenas 2 peões para cada jogador, enquanto a mais completa contém 8 peões, 2 torres, 2 cavalos, 2 bispos, e 1 rainha para cada jogador. As duas configurações estão ilustradas nas figuras (1) e (2). Note que em qualquer configuração, as peças devem obedecer suas posições originais no Xadrez.

.. figure:: /_static/imgs/configuration_2pawns.png
   :width: 200px
   :align: center

   Fig 1. Configuração mais simples do Batalha dos Peões.


.. figure:: /_static/imgs/configuration_complete.png
   :width: 200px
   :align: center

   Fig 2. Configuração mais completa do Batalha dos Peões.

----------------
Condução do Jogo
----------------

Por convenção, o jogador com as peças brancas inicia a partida e a partir de então os movimentos são alternados. O jogador é obrigado a realizar um movimento não sendo possível passar a vez mesmo que isso seja desvantajoso. A partida continua até que um jogador vença ou o empate seja declarado. 

--------------------
Condições de Vitória
--------------------

A falta do Rei faz com que os objetivos na Batalha dos Peões sejam bem diferentes do Xadrez clássico. Dessa forma, para se vencer um jogo é necessário que uma das condições abaixo seja satisfeita:

- **Peão promovido**: pelo menos um dos peões no jogo chegue na última linha do tabuleiro (no caso das brancas) ou chegue na primeira linha (no caso das pretas); ou
- **Captura dos peões**: o jogador deve capturas todos os peões do oponente.

A figura (3) ilustra a primeira condição sendo satisfeita pelo jogador que controla as peças brancas, ou seja, um peão branco chegou na última linha do tabuleiro. A figura (4) ilustra a segunda condição sendo satisfeita, nesse caso, o jogador que controla as peças pretas vence pois todos os peões brancos foram capturados.


.. figure:: /_static/imgs/win_promotion.png
   :width: 200px
   :align: center

   Fig 3. Vitória das brancas pela promoção do peão.


.. figure:: /_static/imgs/win_capture.png
   :width: 200px
   :align: center

   Fig 4. Vitória das preta pela captura de todos os peões do oponente.


-------------------
Condições de Empate
-------------------

A Batalha do Peões segue as mesmas regras do Xadrez para o empate. Ou seja, se uma das seguintes condições for satisfeita, o jogo empata:

- **Nenhum movimento válido**: um jogador ainda tiver peças mas não poder fazer nenhum movimento válido com elas em seu turno.
- **Regra dos 50 movimentos**: cada jogador realizar 50 movimentos sem nenhuma captura.

A figura (5) ilustra um caso de empate onde nenhum jogador pode fazer nenhum movimento válido.


.. figure:: /_static/imgs/tie_nomove.png
   :width: 200px
   :align: center

   Fig 5. Situação de empate, pois nenhum jogador tem movimentos válidos.


----------------------
Movimentação das Peças
----------------------

.. NOTE:: Todas as peças na Batalha dos Peões obedecem as mesmas regras do Xadrez em relação à movimentação e captura.

Todas as peças (com exceção do Cavalo), independente de quantas casas andem, têm seu raio de ação limitado pelas outras peças, amigas ou inimigas. Caso uma peça amiga esteja em seu caminho, ela não poderá parar na casa desta peça amiga, ou em qualquer outra casa que, para chegar nela, deve passar pela casa ocupada. No caso de uma peça inimiga, ainda não é permitido chegar em uma casa passando pela casa ocupada, porém, é possível capturar a peça adversária, removendo-a de jogo e posicionando a peça captora na casa que a peça inimiga ocupava.

- A **Torre** se movimenta nas direções ortogonais, isto é, pelas linhas (horizontais) e colunas (verticais), não podendo se mover pelas diagonais. Ela pode mover quantas casas desejar pelas colunas e linhas, porém, apenas em um sentido em cada jogada.

- O **Bispo** se movimenta nas direções diagonais, ou seja, na direção das casas da mesma cor. Ela pode mover quantas casas desejar pelas diagonais, porém, apenas em um sentido (cada jogada), existe o bispo da casa preta e o bispo da casa branca, e os mesmos não podem mudar de cor durante o jogo.

- A **Dama** pode movimentar-se quantas casas quiser ou puder, na diagonal, vertical ou horizontal, porém, apenas em um sentido em cada jogada, a dama (ou rainha) anda com os movimentos de todas as outras peças (exceto o cavalo), andando quantas casas quiser.

- O movimento do **Cavalo** é em "forma de L", ou seja, anda duas casas na horizontal ou vertical e depois uma casa na vertical ou horizontal, ou vice-versa. O cavalo pode saltar sobre qualquer peça sua ou do adversário. A captura ocorre quando uma peça adversária se encontra na casa final do movimento realizado pelo cavalo.

- O **Peão** movimenta-se apenas uma casa para frente e captura outros peões e peças na primeira casa diagonal superior. Caso uma peça ou peão fique na frente do peão, será impossível movê-lo. Somente se alguma peça adversária fique na sua diagonal acima, ele poderá capturá-la e mudar de coluna. No primeiro movimento de qualquer peão, ele poderá mover-se uma ou duas casas, a critério do enxadrista. Ao contrário das outras peças, o peão não pode mover-se para trás.

Cada peão, em seu primeiro movimento, pode optar por mover uma ou duas casas, desde que exista esta opção (casas livres à sua frente). O movimento de captura do peão é diferente da forma com que ele movimenta-se, ou seja, a captura é feita em diagonal, podendo capturar a peça que se encontra na diagonal próxima, à frente. Se um peão encontrar uma peça adversária à sua frente, ele ficará impedido de se mover até que apareça uma peça adversária em sua diagonal para ser capturada.

En Passant
~~~~~~~~~~

Quando um peão estiver na quinta casa, ou seja, tiver sido movimentado três casas além da sua casa de origem e um peão adversário, da coluna ao lado da sua, executar o seu primeiro movimento saltando duas casas, fugindo do confronto com o peão que já tinha movido três casas, este peão poderá ser capturado en passant e o peão que realiza a captura irá ocupar a casa que o adversário saltou ao mover duas casas. Esta captura somente poderá ser feita imediatamente após o lance feito pelo adversário (movimento de duas casas), caso contrário, não poderá mais ser feita. A figura (6) exemplifica o movimento de en passant.

.. figure:: /_static/imgs/mov_enpassant.gif
   :width: 200px
   :align: center

   Fig 6. Movimento de en passant executado pelas brancas.


---------
Leia Mais
---------

- `Chess - Wikipedia <https://en.wikipedia.org/wiki/Chess>`_
- `Rules of Chess - Wikipedia <https://en.wikipedia.org/wiki/Rules_of_chess>`_


