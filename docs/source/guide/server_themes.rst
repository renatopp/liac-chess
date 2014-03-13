----------------
Mudando os Temas
----------------

Temas Padrão
~~~~~~~~~~~~

As imagens abaixo mostram os temas padrão do Liac Chess.

.. figure:: /_static/imgs/theme_default.png
   :width: 200px

   Default.

.. figure:: /_static/imgs/theme_blackandwhite.png
   :width: 200px

   Black and White.

.. figure:: /_static/imgs/theme_greenfields.png
   :width: 200px

   Green Fields.

.. figure:: /_static/imgs/theme_blueskies.png
   :width: 200px

   Blue Skies.

.. figure:: /_static/imgs/theme_deeppurple.png
   :width: 200px

   Deep Purple.

.. figure:: /_static/imgs/theme_yellowcard.png
   :width: 200px

   Yellow Card.

.. figure:: /_static/imgs/theme_baseball.png
   :width: 200px

   Baseball

.. figure:: /_static/imgs/theme_babyblue.png
   :width: 200px

   Baby Blue

.. figure:: /_static/imgs/theme_rainforest.png
   :width: 200px

   Rain Forest

.. figure:: /_static/imgs/theme_moss.png
   :width: 200px

   Moss

.. figure:: /_static/imgs/theme_candy.png
   :width: 200px

   Candy

.. figure:: /_static/imgs/theme_grapepie.png
   :width: 200px

   Grape Pie

.. figure:: /_static/imgs/theme_vintage.png
   :width: 200px

   Vintage

.. figure:: /_static/imgs/theme_napolitano.png
   :width: 200px

   Napolitano


Criando Novos Temas
~~~~~~~~~~~~~~~~~~~

Os temas no Liac Chess são parametrizaveis, assim, você pode modificar os temas existentes ou criar novos. O arquivo "themes.json", no formato JSON, guarda todos os temas do software, então basta adicionar um novo item nele e reiniciar o programa para ter um novo tema.

Um tema é definido como o seguinte exemplo::
    
    "rainforest": {
        "name": "Rain Forest",
        "light_color": "#9AAB9B",
        "dark_color": "#718351"
    }


onde "rainforest" é um id único e não pode repetir no arguivo, "Rain Forest" é o nome do tema e será mostrado no menu do programa, os campos "light_color" e "dark_color" são as cores das casas claras e escuras, respectivamente, no formato hexadecimal.













