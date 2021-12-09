# -*- coding: utf-8 -*-
import sys
from io import StringIO

def printToFile(fileName : str, s : str) -> None:
	with open(fileName, 'a', encoding="utf-8") as temp:
		temp.write(s)

def out(s : str) -> None:
	global isTOFILE
	if(isTOFILE == False):
		print(s)
	else:
		global toFile
		toFile.write(s + "\n")

def out4(sc : int, s : str) -> None:
	out(str(" "*(sc*4)) + s)

if __name__ == "__main__":
	if(len(sys.argv) < 2 or len(sys.argv) > 3):
		print("Syntax error. Check README.md")
		exit()
	if(len(sys.argv) == 2):
		isTOFILE = False
	else:
		isTOFILE = True
		toFile = StringIO()
		fileName = sys.argv[2]
		if(fileName[-3:] != ".py"):
			fileName += ".py"
		with open(fileName, 'w', encoding="utf-8") as temp:
			temp.write("")

	N = int(sys.argv[1])
	if(N < 0):
		print("Only positive numbers")
		exit()


	out("import sys")
	out("# -*- coding: utf-8 -*-")
	out("")

	out4(0, "def sum2Number(a : int, b : int):")
	out4(1, "if(a < 0 or b < 0):")
	out4(2, "raise ValueError(\"sumCulator can add only positive (+ zero) numbers\")")
	out4(1, f"if(a > {N} or b > {N}):")
	out4(2, f"raise ValueError(\"sumCulator can add only numbers, not more than {N}\")")

	out("")

	li = 0
	si = 0
	NN = N*N
	for i in range(N+1):
		for j in range(N+1):
			li-=-1
			si-=-1
			if(isTOFILE and li == 1000000):
				print(f"{int((si/NN)*100)}% generated")
				printToFile(fileName, toFile.getvalue())
				toFile = StringIO()
				li = 0
			out4(1, f"if(a == {i} and b == {j}):")
			out4(2, f"print({i+j})")

	out("")

	out4(0, "if __name__ == \"__main__\":")
	out4(1, "if(len(sys.argv) != 3):")
	out4(2, "print(\"sumCulator can add only 2 numbers. For example: \")")
	if(isTOFILE == False):
		out4(2, "print(\"> python sumCulator.py number1 number2\")")
	else:
		out4(2, f"print(\"> python {fileName} number1 number2\")")
	out4(2, "exit()")
	out4(1, "a, b = map(int, (sys.argv[1], sys.argv[2]))")
	out4(1, "sum2Number(a, b)")




	if(isTOFILE):
		printToFile(fileName, toFile.getvalue())