----------------------
Criando Bots em Python
----------------------

O Liac Chess já vem com um cliente base escrito em Python e um bot aleatório, nos quais você pode se basear. O objetivo desse cliente é deixar a parte de comunição e tratamento das mensagens servidor-cliente transparente para o programador.

Para criar um novo bot, basta herdar do cliente base, por exemplo::

    from base_client import LiacBot

    class MeuBot(LiacBot):
        name = 'Meu Novo Bot'
        ip = '127.0.0.1'
        port = 50100

        def __init__(self):
            # Construtor

            super(MeuBot, self).__init__()

        def on_move(self, state):
            # Computar a próxima jogada aqui!

            self.send_move((0, 0), (2, 3)) 

        def on_game_over(self, state):
            # Game over aqui, não deve responder o servidor!

            print 'Game Over.'

Os métodos ``on_move`` e ``on_game_over`` são chamados pelo cliente base e o programador deve implementá-los de acordo com o objetivo do bot. O método ``on_move`` será chamado sempre que foz a vez do bot de jogar, o bot então deve calcular a próxima jogada e enviar pelo método ``send_move``, que receve duas tuplas, com as coordenadas do movimento. Com o novo bot criado, basta chamar o método ``start``::

    bot = MeuBot()
    bot.start()

Como uma implementação básica, o Liac Chess também é acompanhado de um bot aleatório, criado para servir de baseline para os novos bots. Isso quer dizer que, um bot inteligente deve conseguir ganhar todas as partidas do bot aleatório, caso contrario, há alguma coisa errada com o bot.

Para iniciar o bot aleatório basta chamá-lo pelo terminal::

    $ python random_bot.py white

para o jogador 1, ou::

    $ python random_bot.py black

para o jogador 2.


