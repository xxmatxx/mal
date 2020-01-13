from prompt_toolkit import PromptSession
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.lexers import PygmentsLexer
from prompt_toolkit.styles.pygments import style_from_pygments_cls

from pygments.lexers.lisp import HyLexer
from pygments.styles import get_style_by_name

from step4_if_fn_do import REP
from mal_types import MalException

style = style_from_pygments_cls(get_style_by_name('manni'))

completer = WordCompleter([
    "def!","let*","fn*","if","+","-","/","*"
], ignore_case=True)

def main():
    session = PromptSession(
        lexer=PygmentsLexer(HyLexer),
        completer=completer,
        style=style
        )

    header = "mal START"
    footer = "mal END"
    print(header)
    try:
        while True:
            try:
                text = session.prompt('>')
                text = REP(text)
                print(text)
            except MalException as m:
                print(str(m))
    except (KeyboardInterrupt, EOFError) as e:
        pass
    print(footer)

if __name__ == '__main__':
    main()