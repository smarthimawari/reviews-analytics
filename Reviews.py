data = []
count = 0 #計數
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line) 
		count += 1
		if count % 1000 == 0: #%是求餘數的意思 e.g. 7%3=1
			print(len(data)) #每1000筆印一次
 
print(data[0]) #印出清單的第0個位子
