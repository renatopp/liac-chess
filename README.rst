==========
Liac Chess
==========

Version 1.0.0

Liac Chess is being developed by the Connectionist Artificial Intelligence Laboratory (LIAC), which takes place at Federal University of Rio Grande do Sul (UFRGS), Brazil. This software was designed to be used in didactic activities for artificial intelligence classes. The goal of Liac Chess is to provide a graphical interface for chess games, which includes its variants such as the Pawn Battle, while students can focus on learning and developing the class algorithms. 

Documentation: http://inf.ufrgs.br/~rppereira/docs/liac-chess/


--------
Features
--------

- Parameterized levels, themes and other configurations.
- Fully implemented pieces: Knights, Bishops, Rooks, Queens, and Pawns.
- All Battle Pawns configurations implemented.
- Allows networked players, specially useful for testing bots.
- Allows human players, including computer vs human games.
- Test coverage for all game rules.


-----------------------------
Requirements (for developers)
-----------------------------

- Python 2.7+
- wxPython 2.9.4+ (ideally 2.9.5)

---------------
What's Missing?
---------------

- The King piece within all rules and special movements.
- The traditional chess configuration.
- A better data structure for board representation.
- A better move generation procedure (which heavily depending on the board 
  representation).
- Historic of movements and the feature of saving a game to a PGN file.
