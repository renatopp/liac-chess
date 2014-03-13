------------------------
Arquivos de Configuração
------------------------

O arquivo "config.json" guarda as configurações que um usuário pode editar no Liac Chess. O arquivo de configurações tem esta cara::

    {
        "slot_0_ip": "127.0.0.1",
        "slot_0_port": 50100,
        "slot_1_ip": "127.0.0.1",
        "slot_1_port": 50200,
        "update_frequency": 10,
        "max_move_time": 999.9,
        "max_infractions": 15
    }

As propriedades editaveis são descritas abaixo:

**slot_0_ip**
    É o endereço para conexão do jogador 1

**slot_0_port**
    É port para conexão do jogador 1

**slot_1_ip**
    É o endereço para conexão do jogador 2

**slot_1_port**
    É port para conexão do jogador 2

**update_frequency**
    A taxa de frequência do "game loop". Tem pouco impacto no jogo. Note que, isso não muda a taxa de frequência de atualização da tela.

**max_move_time**
    O tempo máximo para um jogador fazer sua jogada, em segundos.

**max_infractions**
    O número máximo de infrações que eu um jogador pode ter durante um jogo. Se esse número for alançado, o jogador com o limite de infrações perde o jogo.