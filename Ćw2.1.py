import sys 

print('Podaj pierwszą wartość : ')
war1 = sys.stdin.readline()

print('Podaj drugą wartość : ')
war2 = sys.stdin.readline()

s = int(war1) * int(war2)

sys.stdout.write("%d"%s)
