import sys,codecs,functools as F
_,E,Z=sys.argv,F.reduce,','.join
print(eval('(lambda %s:%s)(%s)'%(Z('nopqrstuvwxyzabcdefghijklm'[:len(_)-2]),codecs.encode(_[1],'rot_13'),Z(_[2:]))))
