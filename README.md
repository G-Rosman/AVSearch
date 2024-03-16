# ANTLR_PRO

This template should help get you started developing with Antlr4 and Python3

### Generate Python scripts and tokens

```sh
antlr4 -Dlanguage=Python3 YourGrammar.g4
```
### If there is not any Visitor.py files
```sh
antlr4 -Dlanguage=Python3 -visitor YourGrammar.g4
```

### Увидеть графф токены и их позиции и трассировку
```sh
antlr4-parse ANTLR_PRO.g4 translationUnit -tree -gui -tokens -trace CodeExample1.cpp
```

### Увидеть токены и их позиции 
```sh
antlr4-parse ANTLR_PRO.g4 translationUnit -tokens CodeExample1.cpp
```