#讀取檔案 reviews.txt

data = []
count = 0

with open("reviews.txt", "r") as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(data)


