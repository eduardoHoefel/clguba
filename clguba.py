#pylint:disable=all
import sys,codecs,argparse,string
from functools import reduce as E #encoded is R
print(eval('(lambda '+codecs.encode(','.join(string.ascii_lowercase[:len(sys.argv)-2])+':'+sys.argv[1], 'rot_13')+')('+','.join(sys.argv[2:])+')'))
