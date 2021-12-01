Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
======== RESTART: C:/Users/ADESIPO EMMANUELLA/Documents/develop/hello.py =======
Hello World
>>> fred = 100
>>> print(fred)
100
>>> fred = 200
>>> print(fred)
200
>>> fred = 200
>>> fred = john
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    fred = john
NameError: name 'john' is not defined
>>> john = fred
>>> print(john)
200
>>> found_coins = 20
>>> magic_coins = 10
>>> stolen_coins = 3
>>> found_coins + magic_coins + stolen_coins * 52
186
>>> stolen_coins = 2
>>> found_coins + magic_coins + stolen_coins * 52
134
>>> fred = "Why do horillas have big nostrils? Big fingers!!"
>>> print(fred)
Why do horillas have big nostrils? Big fingers!!
>>> fred = '''How do dinosaurspay their bill?
With tyrannosaurus checks!'''
>>> print(fred)
How do dinosaurspay their bill?
With tyrannosaurus checks!
>>> silly_string = 'He said, "Aren't can't shouldn't wouldn't."'
SyntaxError: invalid syntax
>>> single_quote_str = 'He said, "Aren\'t can\'t shouldn\'t wouldn\'t."'
>>> print(single_quote_str)
He said, "Aren't can't shouldn't wouldn't."
>>> 