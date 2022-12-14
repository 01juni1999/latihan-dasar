try:
    raise Exception('spam', 'eggs')
except Exception as inst:
    print(type(inst))    # the exception instance
    print(inst.args)     # arguments stored in .args
    print(inst)          # __str__ allows args to be printed directly,
    print(inst)          # __str__ allows args to be printed directly,
    x, y = inst.args     # unpack args
    x, y = inst.args     # unpack args
    print('x =', x)
    print('y =', y)

    def this_fails():
        x = 1/0

try:
     this_fails()
except ZeroDivisionError as err:
  print('Handling run-time error:', err)
