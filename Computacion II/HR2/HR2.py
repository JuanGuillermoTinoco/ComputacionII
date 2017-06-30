#Segunda tarea de Hacherranck
#Juan Guillermo Urincho Tinoco

import sys


s = raw_input().strip(); sumatoria = 1
def total(S,sumatoria):
    for i in range(len(s)):
        if s[i].isupper()==True:
            sumatoria = sumatoria + 1
    print sumatoria
total(s,sumatoria)
