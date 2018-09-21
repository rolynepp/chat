import os

def con_input(filename):
	cons = []
	with open(filename, 'r', encoding='utf-8-sig') as f:
		for line in f:
			cons.append(line.strip())
	return cons

def con_output(con_output):
	new = []
	person = None
	for p in con_output:
		if p == 'rolyne':
			person = 'rolyne'
			continue
		elif p =='Tom':
			person = 'Tom'
			continue
		if person:		
			new.append(person + ':'+ p)

	return new
#	with open(con_output, 'w') as f:
	#		f.write()

def write_file(filename, new):
	with open(filename, 'w') as f: #寫進filename
		for p in new:
			f.write(p + '\n')
		

def main():
	cons = con_input('input.txt')
	cons = con_output(cons)
	print(cons)
	write_file('output.txt', cons)
main()#此為呼叫的動作

#此程式主要有幾個步驟，首先先將檔案導入清單
#第二再將程式進行轉換
#第三再將其寫入程式
#記得每次都要有main程式