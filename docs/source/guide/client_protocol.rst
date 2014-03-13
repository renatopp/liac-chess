------------------------
Protocolo de Comunicação
------------------------

Para criar um novo bot para jogar no Liac Chess, é necessário faze-lo se comunicar com o servidor, e para isto, é necessário definir um protocolo de comunicação. Um protocolo de comunicação define que tipo de mensagens o servidor e os clientes podem enviar, o formato dessas mensagens, e quando elas serão enviadas. O Liac Chess utiliza mensagens no formato `JSON <https://en.wikipedia.org/wiki/JSON>`_, dessa forma, o ideal é que o bot utilize uma biblioteca para codificação e decodificação de objetos em JSON.

Por questão de simplicidade, o Liac Chess foi desenvolvido para que a comunição entre cliente-servidor seja a menor possível. Do ponto de vista do bot, o pipeline de comunição pode ser descrito como ilustrado na figura (1):

.. figure:: /_static/imgs/communication_pipeline.png
   :width: 600px
   :align: center

   Fig 1. Pipeline de comunição, do ponto de vista do cliente.

O primeiro passo no processo de comunição é a conexão com o servidor. Consulte as configurações do servidor para saber o endereço e porta de conexão, que por padrão é ``127.0.0.1:50100`` para o primeiro cliente e ``127.0.0.1:50200`` para o segundo cliente.

Em seguida, o cliente deve mandar uma mensagem com o nome do bot. Note que esta é a primeira mensagem entre cliente e servidor. A mensagem de nome segue o seguinte formato::

    {
        "name": STRING
    }

A próxima mensagem é por parte do servidor com o estado do tabuleiro e acontece apenas quando o jogo começa. O estado do tabuleiro é a maior mensagem de todo o processo de comunição e segue o seguinte formato::

    {
        "board"             : STRING,
        "enpassant"         : COORDENADA,
        "who_moves"         : -1 OU 1,
        "bad_move"          : BOOLEAN,
        "white_infractions" : INTEGER,
        "black_infractions" : INTEGER,
        "winner"            : -1, 0 OU 1,
        "50moves"           : BOOLEAN,
        "draw"              : BOOLEAN
    }

O estado do tabuleiro é descrito em detalhes na próxima seção. 

Ao receber o estado do tabuleiro, o cliente deve calcular a próxima jogada em enviar para o servidor, com a seguinte mensagem::

    {
        "from": COORDENADA,
        "to": COORDENADA
    }


.. Os tipos descritos nas mensagens devem seguir o padrão JSON, por exemplo:

.. COORDENADA
..     Uma lista de duas dimensões com a posição no tabuleiro. Ex: ``[0, 0]``.

.. STRING
..     String com aspas duplas. Ex: ``"String"``.

.. BOOLEAN
..     Valor booleano: ``true`` ou ``false``.