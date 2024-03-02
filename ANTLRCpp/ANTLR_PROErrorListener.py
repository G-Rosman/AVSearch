from antlr4.error.ErrorListener import ErrorListener


class GrammerErrorListener(ErrorListener):

    def __init__(self):
        print("\033[94m" + f"@Инициализирован собственный обработчик ошибок GrammerErrorListener;" + "\033[0m")

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        print("\033[91m" + f"ERROR:--------------------------------------------------------------------------------------------\n"
                           f"\tСинтаксическая ошибка возникла в {line} строке (проверьте {column} знак)!\n\tТекст сообщения об ошибке: {msg}"
                           f"\n-------------------------------------------------------------------------------------------------------" + "\033[0m")
        print('\033[91mCode finished with ERROR\033[0m \U0001F641!')
        exit()