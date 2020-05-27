# Fui mais longe aqui e usei input e import

from parameter import greet

#como fazer pra dar um else na última opção, e invocar a função SEM parâmetro algum?

name = input("What's your name? ")

(greet('es'), name)
(greet('fr'), name)
(greet('en'), name)
(greet(' '), name)

# another way: using return statement

def greet2()
    return "Hello"

print(greet2(), "Glenn")
print(greet2(), "Sally")
