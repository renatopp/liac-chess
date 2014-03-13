---------------------
Técnicas e Algoritmos
---------------------

Não existe uma técnica ou abordagem específica para fazer um Bot para jogar no Liac Chess. Porém, algumas delas são comumente utilizadas nesses tipos de jogos. Está seção não tem a intenção explicar cada uma delas, mas sim dar uma visão geral e referências para suas implementações.


Representação do Tabuleiro
~~~~~~~~~~~~~~~~~~~~~~~~~~

A primeira coisa a se preocupar ao fazer um programa de xadrez (ou mesmo um jogador para ele) é com a representação do tabuleiro. Além da modelagem do próprio tabuleiro em si, é necessário informações adicionais para representar o jogo como um todo, por exemplo, posição do en passant, de quem é o turno, etc. 

Na internet é possível encontrar diversas formas diferentes de representar um tabuleiro, peças e jogadas. Em geral, são utilizadas estruturas de dados e algoritmos parcimoniosos para garantir um bom uso de memória e processamento. Esses métodos foram criados para serem eficientes já que são heranças de um tempo em que o poder computacional dos grandes computadores era menor que os celulares de hoje em dia.

Algoritmos e estruturas eficientes ainda são necessários para desenvolver jogadores de alto nível capazes de bater campeões mundiais. Implementações "grosseiras", como utilizando orientação a objetos, não são suficientes para este nível de efiencia, mas com certeza podem ser bons o bastante para jogar contra jogadores de nível mediano.

Consulte:

- http://chessprogramming.wikispaces.com/Board+Representation
- https://en.wikipedia.org/wiki/Board_representation_%28chess%29


Geração de Movimento
~~~~~~~~~~~~~~~~~~~~

A geração de movimentos é um processo importante para se fazer um bot capaz de jogar xadrez (ou alguma de suas variantes) e sua implementação é altamente dependente da representação do tabuleiro. 

Consulte:

- http://chessprogramming.wikispaces.com/Move+Generation


Buscando o Melhor Movimento
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Em relação ao desempenho do bot, o algoritmo de busca é o mais importante. Escolher o melhor algoritmo e saber como implementá-lo é essencial para que o bot seja no mínimo competitivo.

O algoritmo mais comum para jogos de soma zero como o xadrez, damas, ou jogo da velha é o minimax. Porém, o minimax avalia todo espaço de busca, dado uma profundidade limite. Ou seja, no caso do xadrez, onde a quantidade de estados pode chegar a milhões com poucos níveis de profundidade, o uso de minimax é impraticável. Há diversas alternativas interessantes ao minimax, que em geral, são modificações do algoritmo original, como o alpha-beta e o negamax.

Consulte (minimax):

- http://chessprogramming.wikispaces.com/Minimax
- http://en.wikipedia.org/wiki/Minimax‎

Consulte (alpha-beta):

- http://chessprogramming.wikispaces.com/Alpha-Beta
- http://en.wikipedia.org/wiki/Alpha-beta_pruning

Consulte (negamax):

- http://chessprogramming.wikispaces.com/Negamax
- http://en.wikipedia.org/wiki/Negamax

Consulte:

- http://chessprogramming.wikispaces.com/Search
- http://chessprogramming.wikispaces.com/NegaScout
- http://chessprogramming.wikispaces.com/NegaC%2A
- http://chessprogramming.wikispaces.com/Iterative+Search
- http://en.wikipedia.org/wiki/Negascout
- http://en.wikipedia.org/wiki/Transposition_table
- http://en.wikipedia.org/wiki/Horizon_effect


Avaliando os Estados
~~~~~~~~~~~~~~~~~~~~

Uma boa função de avaliação deve retornar um valor alta para estado bons e valores baixos caso contrário. A questão é como decidir o que é um bom estado e o que não é. 

A escolha da função de avaliação também é um fator importante para a eficiência do algoritmo de busca, que em geral depende altamente dela para fazer podas e escolher caminhos de forma iterativa.


Consulte:

- http://chessprogramming.wikispaces.com/Evaluation


















