
import os

def con_input(filename):
	cons = []
	with open(filename, 'r', encoding='utf-8-sig') as f:
		for line in f:
			cons.append(line.strip())
	return cons

def con_output(con_output):
	person = None
	rolyne_word_count = 0
	rolyne_sticker_count = 0
	rolyne_image = 0
	FrankC_word_count = 0
	for p in con_output:
		s = p.split(' ') #用空白鍵做分割
		time = s[0]
		name = s[1]
		if name == 'rolyne_chen':
			if s[2] == '貼圖':
				rolyne_sticker_count +=1
			elif s[2] == '圖片':
				rolyne_image += 1
			else:
				for m in s[2:]:
					rolyne_word_count += len(m)
		elif name =='FrankC':
			for n in s[2:]:
				FrankC_word_count +=len(n)
	print('rolyne_chen說了', rolyne_word_count, '傳了', rolyne_sticker_count,'個貼圖')
	print('Frankc說了', FrankC_word_count)

#	with open(con_output, 'w') as f:
	#		f.write()

def write_file(filename, new):
	with open(filename, 'w') as f: #寫進filename
		for p in new:
			f.write(p + '\n')
		

def main():
	cons = con_input('[LINE]Frankc.txt')
	print(cons)
	cons = con_output(cons)
	print(cons)
	#write_file('output.txt', cons)
main()#此為呼叫的動作

#此程式主要有幾個步驟，首先先將檔案導入清單
#第二再將程式進行轉換
#第三再將其寫入程式
#記得每次都要有main程式