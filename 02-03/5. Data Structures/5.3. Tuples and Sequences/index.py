from curses import BUTTON2_PRESSED


t = 12345, 54321, 'hello!'
t[0]
12345
t
(12345, 54321, 'hello!')
 # Tuples may be nested:
u = t, (1, 2, 3, 4, 5)
u
((12345, 54321, 'hello!'), (1, 2, 3, 4, 5))
 # Tuples are immutable:
t[0] = 88888
