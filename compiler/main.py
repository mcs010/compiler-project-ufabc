from antlr4 import CommonTokenStream, FileStream
from src.core.IsiLanguageLexer import IsiLanguageLexer
from src.core.IsiLanguageParser import IsiLanguageParser
from exception.exception import IsiSemanticException
from exception.exception import IsiSyntaxException
from antlr4.error.ErrorListener import ErrorListener

def main():
    try:
        error_listener = IsiErrorListener()
        lexer = IsiLanguageLexer(FileStream("./File1.isi"))
        stream = CommonTokenStream(lexer)
        parser = IsiLanguageParser(stream)
        parser.removeErrorListeners()
        parser.addErrorListener(error_listener)
        parser.prog()
        parser.showCommands()

        try:
            with open("main_class.java", 'w') as file:
                file.write(parser.code_generator(1))
        except Exception as error:
            print(f"Erro: {error}")

    except IsiSemanticException as error:
        print(f"Erro de semântica: {error}")

    except Exception as error:
        print(f"Erro de sintaxe: {error}")

class IsiErrorListener(ErrorListener):
    def error_syntax(self, recognizer, symbol, line, column, message, error):
        raise IsiSyntaxException(f"Erro de sintaxe: linha {line} coluna {column}: {message}")
    
if __name__ == '__main__':
    main()