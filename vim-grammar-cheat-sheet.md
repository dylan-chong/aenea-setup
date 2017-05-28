    mapping = {
        'insert': Key('i'),
        'big insert': Key('I'),
        'append': Key('a'),
        'big append': Key('a'),
        'open': Key('o'),
        'big open': Key('O'),
        'sust': Key('S'),
        }
        
    spec = ('[upper | natural] ( proper | camel | rel-path | abs-path | score | sentence |'
            'scope-resolve | jumble | dotword | dashword | natword | snakeword | '
            'brooding-narrative')

        'up': Text('k'),
        'down': Text('j'),
        'left': Text('h'),
        'right': Text('l'),

        'gup': Key('c-u'),
        'gown': Key('c-d'),

        'lope': Text('b'),
        'yope': Text('w'),
        'elope': Text('ge'),
        'iyope': Text('e'),

        'lopert': Text('B'),
        'yopert': Text('W'),
        'elopert': Text('gE'),
        'eyopert': Text('E'),

        'apla': Text('{'),
        'anla': Text('}'),
        'sapla': Text('('),
        'sanla': Text(')'),

        'care': Text('^'),
        'hard care': Text('0'),
        'doll': Text('$'),

        'screecare': Text('g^'),
        'screedoll': Text('g$'),

        'scree up': Text('gk'),
        'scree down': Text('gj'),

        'wynac': Text('G'),

        'wynac top': Text('H'),
        'wynac toe': Text('L'),
