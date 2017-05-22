    operateCharMap = {
        "parens": "rparen",
        "word": "w",
        "scent": "s",
        "para": "p",
        "bracks": "rbracket",
        "braces": "rbrace",
        "quotes": "dquote",
        "single quotes": "squote",
    }

    advCharMap = {
            "inner": "i",
            "around": "a",
    }

    verbCharMap = {
            "dosh": "d",
            "copy": "y",
            "change": "c",
            "select": "v",
    }

    lineVerbCharMap = {
            "dosh line": "d:2",
            "copy line": "y:2",
            "change line": "c:2,escape",
            "select line": "s-V",
            "kill till end": "s-D",
            "select till end": "v,dollar",
            "copy till end": "y,dollar",
            "change till end": "s-C,escape",
    }

    vimGeneric = {
        # inserting:
        "<letters>": Key("%(letters)s"),
        "sky <letters>": Key("s-%(letters)s"),
        "num <numbers>": Key("%(numbers)s"),
        "<numbers>": Key("%(numbers)s"),
        "space [repeat <n>]": Key("space:%(n)d"),
        "<specials> [repeat <n>]": Key("%(specials)s:%(n)d"),
        "say <text>": Function(lower_that),
        # "<text>": Function(lower_that),
        "cap <text>": Function(cap_that),

        "(slap|slop) [<n>]": Key("enter:%(n)d"),
        "chuck [<n>]": Key("backspace:%(n)d"),
        "kill [<n>]": Key("del:%(n)d"),

        "rosh [<n>]": esc + Key("%(n)d,d,l"),
        "dosh [<n>]": esc + Key("%(n)d,d,h"),

        "[<n>] up": esc + Key("k:%(n)d"),
        "[<n>] down": esc + Key("j:%(n)d"),
        "[<n>] left": esc + Key("h:%(n)d"),
        "[<n>] right": esc + Key("l:%(n)d"),

    #    "gee up [<n>]": esc + Text("%(n)d") + Key("g,k"),
    #    "gee down [<n>]": esc + Text("%(n)d") + Key("g,j"),
    #    "gee left [<n>]": esc + Text("%(n)d") + Key("g,h"),
    #    "gee right [<n>]": esc + Text("%(n)d") + Key("g,l"),

        "[<n>] upper": Key("up:%(n)d"),
        "[<n>] downer": Key("down:%(n)d"),
        "[<n>] lefter": Key("left:%(n)d"),
        "[<n>] righter": Key("right:%(n)d"),

        "cary": esc + Key("0"),
        "car": esc + Key("caret"),
        "doll": esc + Key("dollar"),
        "go to top": esc + Key("g,g"),
        "go to bottom": esc + Key("s-G"),
        "extract [<n>]": esc + Key("x:%(n)d"),

        "paste older": esc + Key("comma,p"), # maxbrunsfeld/vim-yankstack
        "paste newer": esc + Key("comma,s-P"), # maxbrunsfeld/vim-yankstack

        # "copy that": Key("y"),

        "duplicate line [<n>]": esc + Key("y,y,p:%(n)d"),
        # "duplicate line above <n>": esc + Key("y,y,P:%(n)d"),

        "vis-mode": esc + Key("v"),
        "vis-line": esc + Key("s-v"),
        "vis-block": esc + Key("c-v"),
        "reselect that": esc + Key("g,v"),

        "sert": esc + Key("i"),
        "big sert": esc + Key("s-i"),
        "append": esc + Key("a"),
        "big append": esc + Key("s-a"),
        "scape|escape": Key("escape:2"),
        "open": esc + Key("o"),
        "big open": esc + Key("s-o"),
        "paste": esc + Key("p"),
        "big paste": esc + Key("s-p"),

        "next [<n>]": esc + Key("n:%(n)d"),
        "preeve [<n>]": esc + Key("N:%(n)d"),

        # 'match that': esc + Key("percent"),

        'rope [<n>]': esc + Key('%(n)d, w'),
        'irope [<n>]': esc + Key('%(n)d, e'),
        'lope [<n>]': esc + Key('%(n)d, b'),
        'ilope [<n>]': esc + Key('%(n)d, g, e'),

        'ropert [<n>]': esc + Key('%(n)d, s-W'),
        'iropert [<n>]': esc + Key('%(n)d, s-E'),
        'lopert [<n>]': esc + Key('%(n)d, s-B'),
        'ilopert [<n>]': esc + Key('%(n)d, g, s-E'),

        # Sneak
        'sneak': esc + Key('s'),
        'sneak back': esc + Key('s'),

        "next para [<n>]": esc + Key("%(n)d, rbrace"),
        "preev para [<n>]": esc + Key("%(n)d, lbrace"),
        "next scent [<n>]": esc + Key("%(n)d, rparen"),
        "preev scent [<n>]": esc + Key("%(n)d, lparen"),
        "next sec [<n>]": esc + Key("%(n)d, rbracket, rbracket"),
        "preev sec [<n>]": esc + Key("%(n)d, lbracket, lbracket"),

        "(undo|scratch) [<n>]": esc + Key("u:%(n)d"),
        "redo [<n>]": esc + Key("c-r:%(n)d"),
        "repeat [<n>]": esc + Key("%(n)d, dot"),

        'skip [<n>]': esc + Key("%(n)d, f"),
        'skip back [<n>]': esc + Key("%(n)d, s-F"),

        # 'jump (bill|till) again [<n>]': esc + Key("escape, %(n)d, semicolon"),
         # nnoremap K ;
        'reverse semi [<n>]': esc + Key("escape, %(n)d, f6"),
         # nnoremap <F6> ,

        # "indent that": esc + Key("rangle,rangle"),
        # "out-dent that": esc + Key("langle,langle"),
        "join [<n>]": esc + Key("s-J:%(n)d"),
        "toggle case": esc + Key("tilde"),

        # Magic:
        # "<verbKey> <advKey> <opKey>": esc + Key("%(verbKey)s") + Key("%(advKey)s") + Key("%(opKey)s"),
        "dosh [<n>] (words|word)": esc + Key("d,%(n)d") + Key("s-B"),
        "rosh [<n>] (words|word)": esc + Key("d,%(n)d") + Key("s-W"),
        "<lineVerbKey>": esc + Key("%(lineVerbKey)s"),

        "find": esc + Key("slash"),
        "find and replace": esc + Key("colon, percent, s, slash, slash, g, left, left"),
        "vis find and replace": Key("colon, s, slash, slash, g, left, left"),
        "find back": esc + Key("question"),
        # "find now <text>": esc + Key("slash") + Text("%(text)s"),
        # "find back now <text>": esc + Key("question") + Text("%(text)s"),
        # "vis find <text>": Key("slash") + Text("%(text)s"),
        # "vis find back <text>": Key("question") + Text("%(text)s"),
        "jump till <text>": esc + Key("slash") + Text("%(text)s") + Key("enter"),
        "jump back till <text>": esc + Key("question") + Text("%(text)s") + Key("enter"),

        "mark that": esc + Key("m,a"),
        "mark bravo": esc + Key("m,b"),
        "jump mark": esc + Key("backtick,a"),
        "format mark": esc + Key("g,q,backtick,a"),
        "select mark": esc + Key("v,backtick,a"),
        "copy mark": esc + Key("y,backtick,a"),
        "change mark": esc + Key("c,backtick,a"),
        "dosh mark": esc + Key("d,backtick,a"),
        "remove mark": esc + Key("m,hyphen"),

        "jump forward [<n>]": esc + Key("c-i:%(n)d"),
        "jump back [<n>]": esc + Key("c-o:%(n)d"),
        "last edit [<n>]": esc + Key("%(n)d,g,semicolon"),

        "pop [<n>]": Key("c-p:%(n)d"),
        "pop again": Key("c-x,c-p"),
        "pip [<n>]": Key("c-n:%(n)d"),
        "pip again": Key("c-x,c-n"),
        "(pip|pop) file": Key("c-x,c-f"),
        "(pip|pop) line": Key("c-x,c-l"),
        "(pip|pop) omni": Key("c-x,c-o"),
        "(pip|pop) arg": Key("c-x,c-a"),
        "(pip|pop) cancel": Key("c-e"),

        "format para": esc + Key("s-Q"),

        "comment that": esc + Key("g,c"),
        "comment line": esc + Key("g,c,c"),
        "comment para": esc + Key("g,c,a,p"),

        "(mort) [<n>]": esc + Key("c-d:%(n)d") ,
        "(lest) [<n>]": esc + Key("c-u:%(n)d") ,

        "record macro": esc + Key("q,q"),
        "end macro": Key("q"),
        "repeat macro [<n>]": Key("%(n)d,at,q"),
        "(maru) [<n>]": esc + Key("%(n)d, asterisk"),
        "(paru) [<n>]": esc + Key("%(n)d, hash"),

        ### splits:
        "split (screen|window)": esc + Key("c-w,s"),
        "split (screen|window) vertically": esc + Key("c-w,v"),
        "(screen|window) left": esc + Key("c-w,h"),
        "(screen|window) right": esc + Key("c-w,l"),
        "(screen|window) up": esc + Key("c-w,k"),
        "(screen|window) down": esc + Key("c-w,j"),
        "close (split|screen|window)": esc + Key("c-w,c"),
        "close other splits": esc + Key("colon/10,o,n,l,y/10,enter"),

        "edit file": esc + Key("colon,e,space,tab"),
        "buff-switch": esc + Key("colon,b,space,tab"),
        'buff-delete': esc + Key('colon,b,d,enter'),
        'buff-next': esc + Key('colon,b,n,enter'),
        'buff-prev': esc + Key('colon,b,p,enter'),
        'buff-list': esc + Key('colon,l,s,enter'),
        'screen (center|middle)': esc + Key("z, dot"),
        'screen top': esc + Key("z, t"),
        'screen bottom': esc + Key("z, b"),
        "swiddle": esc + Key("escape, c-p"),
        "swiddle recent": esc + Key("escape,colon,s-C,t,r,l,s-P,s-M,s-R,s-U,enter"),

        # Send
         "(eval|rip) File": esc + Key("comma,a,a"),
         # "eval File and echo": esc + Key("comma,a,e"),
         # . "eval File (open .Rout)": esc + Key("comma,a,o"),
         # --------------------------------------------------------
         "(eval Mark|rip mark)": esc + Key("comma,b,d"),
         "eye-rip mark": esc + Key("comma,b,b"),
         # "eval Mark and echo": esc + Key("comma,b,e"),
         # "eval Mark and down": esc + Key("comma,b,d"),
         # "eval Mark and echo and down": esc + Key("comma,b,a"),
         # --------------------------------------------------------
         "eval Chunk": esc + Key("comma,c,d"),
         # "eval Chunk and echo": esc + Key("comma,c,e"),
         # "eval Chunk and down": esc + Key("comma,c,d"),
         # "eval Chunk and echo and down": esc + Key("comma,c,a"),
         "eval Chunks from top": esc + Key("comma,c,h"),
         # --------------------------------------------------------
         "(eval|rip) Func": esc + Key("comma,f,d"),
         # "eval Func and echo": esc + Key("comma,f,e"),
         # "eval Func and down": esc + Key("comma,f,d"),
         # "eval Func and echo and down": esc + Key("comma,f,a"),
         # --------------------------------------------------------
         "(eval|rip) Selected": esc + Key("comma,s,d"),
         # "eval Selected and echo": esc + Key("comma,s,e"),
         # "eval Selected down": esc + Key("comma,s,d"),
         # "eval Selected and echo and down": esc + Key("comma,s,a"),

         "(eval|rip) Preev": esc + Key("g,v/2,comma,s,d"),
         # "eval Preev and echo": esc + Key("g,v/100,comma,s,e"),
         # . "eval Selected (Runuate and insert output in new tab)": esc + Key("comma,s,o"),
         # --------------------------------------------------------
         "eval Para": esc + Key("comma,p,d"),
         # "eval Para and echo": esc + Key("comma,p,e"),
         # "eval Para and down": esc + Key("comma,p,d"),
         # "eval Para and echo and down": esc + Key("comma,p,a"),
         # --------------------------------------------------------
         "eye-rip": esc + Key("comma,l"),
         "rip [<n>]": esc + Key("enter/2:%(n)d"),

         "Print that": esc + Key("comma,r,p"),
         "Name that": esc + Key("comma,r,n"),
         "Structure that": esc + Key("comma,r,t"),
         "View that": esc + Key("comma,r,v"),
         # --------------------------------------------------------
         "Argument that": esc + Key("comma,r,a"),
         "Example that": esc + Key("comma,r,e"),
         "Help that": esc + Key("comma,r,h"),
         # --------------------------------------------------------
         "Summary that": esc + Key("comma,r,s"),
         "Plot that": esc + Key("comma,r,g"),
         "Plot and summary": esc + Key("comma,r,b"),

        "assign that": Key("space,langle,hyphen,space"),
        "pipe that": Key("space,percent,rangle,percent,space"),

        "edit args": esc+Key("colon,a,r,g,s,space,asterisk,dot"),
        "run makefile": esc + Key("colon/100,exclamation,m,a,k,e,enter"),

        "close buffer": esc + Key("colon,q,enter"),
        "write and (exit|quit)": esc + Key("colon,w,q,enter"),
        "write file": esc + Key("colon,u,p,d,a,t,e,enter"),
        "write all files": esc + Key("colon,w,a,l,l,enter"),
        "write as": esc + Key("colon,s,a,v,e,a,s,space"),
    }
