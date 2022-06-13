"""
    TUGAS BESAR STRATEGI ALGORITMA
    KELOMPOK 14 - IF4401
    ANGGOTA:
        Herman Gemilang - 1301204014
        Gagah Aji Gunadi - 1301204093
        Syahdan Naufal Nur Ihsan - 1301204110
    PROBLEM : 
    SOLUTION ALGORITHM: 
"""

import time

from bruteforce import bruteForce
from backtrack import backtrack

sentence = input("Masukkan 3 kata dipisah dengan spasi : ")
pattern = input("Masukkan pattern berupa 3 huruf (2 variabel): ")

opsi = int(input(
    "Silahkan pilih algoritma yang akan digunakan: \n1. Brute Force\n2. Backtracking\n"))
print()
if opsi == 1:
    startBruteForce = time.time()
    bruteForce(sentence, pattern)
    print(f"Time executed: {time.time() - startBruteForce}s")
elif opsi == 2:
    startBacktracking = time.time()
    backtrack(sentence, pattern)
    print(f"Time executed: {time.time() - startBacktracking}s")
else:
    print("Invalid input")
