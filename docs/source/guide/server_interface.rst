-----------
A Interface
-----------

Tela Principal
~~~~~~~~~~~~~~

A tela principal do Liac Chess possui um visual simples e intuitivo, como mostrado na figura (1). 

.. figure:: /_static/imgs/interface.png
   :width: 600px
   :align: center

   Fig 1. Tela principal do Liac Chess.

Na figura (1) é possível observar os seguintes componentes:

1. Na **barra de menus** é possível acessar as opções e ações principais do programa, como: criar uma nova partida; pausar ou reiniciar uma partida em andamento; mudar o tema do tabuleiro; acessar as telas de ajuda; etc.

2. O **tabuleiro** mostra o estado atual das peças no jogo. No caso de jogadores humanos, ele também é utilizado para selecionar e mover peças.

3. O **cronometro** fica no canto superior direito e mostra o tempo restante que o jogador atual tem para fazer o movimento.

4. Os painéis de **informação dos jogadores** mostram o nome e o time de cada jogador, além do seu status de conexão (no caso de jogadores pela conectados por sockets) e a quantidade de infrações de cada jogador (ao lado do ícone vermelho).

5. O campo de **status da partida** mostra qual o andamento da partida, ou seja, mostra de quem é a vez de jogar, ou quem ganhou a partida, ou ainda, se a partido acabou em empate.

6. Os **botões diversos** na barra lateral são utilizados para: mudar o time dos jogadores; começar um jogo; pausar um jogo; ou reiniciar um jogo.

7. O **log da partida**, ainda não implementado, deve mostrar o histórico de jogadas da partida.


Tela de Nova Partida
~~~~~~~~~~~~~~~~~~~~

Ao selecionar no menu, a opção para criar uma nova partida, uma tela similar à ilustrada na figura (2) irá aparecer:

.. figure:: /_static/imgs/interface_newgame.png
   :width: 600px
   :align: center

   Fig 1. Tela para criar uma nova partida.

A tela de criação de nova partida possui os seguintes componentes:

1. Na barra de **modo de jogador** é possível escolher os diversos tipos de jogadores para a nova partida. Os modos são:

    - No modo **livre**, o usuário pode mover as peças livremente, sem nenhuma restrição de tempo, time ou regra. 

    - No modo **humano vs humano**, dois jogadores humanos compartilham a mesma tela de jogo, obedecendo as regras de movimentação e de ordem de jogo.

    - No modo **humano vs IA**, um jogador humano pode desafiar uma inteligência artificial conectada pela rede.

    - No modo **IA vs IA**, duas IA's podem jogar de forma automática.

  Note que, em todos os modo, exceto o primeiro, todas a regras da partida são válidas, incluindo o tempo e a ordem de movimentação de cada jogador.

2. Na barra de **modo de jogo** é possível seleciona a configuração desejada do tabuleiro. Note que as opções com uma imagem de interrogação "?" estão assim pois ainda não possuem uma imagem adequada do tabuleiro.

3. O botão **novo jogo** cria então uma nova partida com as configurações desejadas.


























