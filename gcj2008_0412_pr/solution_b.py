import sys

def fgets(f):
  return f.readline().rstrip("\n")

def solve_case():
  pass

if __name__ == '__main__':
  if len(sys.argv) < 2:
    print "Gimme the input file..."
    sys.exit()
  fin = open(sys.argv[1], 'r')
  for case_index in range(int(fgets(fin))):
    num, src, trg = fgets(fin).split(' ', 3)
    r = solve_case(num, src, trg)
    print "Case #%d: %s" % (case_index+1, r)
  fin.close()