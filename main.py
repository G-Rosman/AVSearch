from antlr4 import *
from ANTLRCpp.ANTLR_PROLexer import ANTLR_PROLexer
from ANTLRCpp.ANTLR_PROParser import ANTLR_PROParser
from ANTLRCpp.ANTLR_PROVisitor import ANTLR_PROVisitor
from ANTLRCpp.ANTLR_PROListener import ANTLR_PROListener
from ANTLRCpp.ANTLR_PROErrorListener import GrammerErrorListener
import sys


def main(arg):
    stream = FileStream(arg)
    lexer = ANTLR_PROLexer(stream)
    stream = CommonTokenStream(lexer)
    parser = ANTLR_PROParser(stream)

    error_listener = GrammerErrorListener()
    parser.removeErrorListeners()
    parser.addErrorListener(error_listener)

    tree = parser.translationUnit()
    visitor = ANTLR_PROVisitor()
    visitor.file_path = arg
    visitor.visitTranslationUnit(tree)

    print("\033[92m" + "Code correct finished \U0001F600" + "\033[0m")


if __name__ == '__main__':
    if len(sys.argv) > 1:
        Code = sys.argv[1]
    else:
        print("No file specified. Using default file 'CodeExample.cpp'.")
        Code = "CodeExample1.cpp"
    
    main(Code)