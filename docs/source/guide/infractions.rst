=========
Infrações
=========

Nas informações dos jogadores (localizada no painel lateral), é possível observar um cartão vermelho acompanhado por um número. Este número indica a quantidade de infrações de cada jogador. Ao atingir um número máximo de infrações (por padrão 5, mas este valor pode ser modificado no arquivo de configuração), o jogador perde o jogo.

Esta medida foi tomada devido ao uso de jogadores em rede, para que não aconteça de um jogador ficar muito tempo sem fazer algum movimento. Dessa forma, uma infração pode ocorrer nos seguintes casos:

- Ao ultrapassar o tempo limite para uma jogada (por padrao 5.9 segundos, podendo variar de acordo com o arquivo de configuração).
- Ao enviar um movimento inválido para o servidor.

Ao ultrapassar o tempo limite, o jogador ganha uma infração e o relógio é resetado. No caso do jogador enviar um movimento inválido, além do relógio resetado o estado do jogo é enviado novamente para o jogador.

