open_file = open("sheet.csv")
print("----------------------")

cup_arr = []
total_arr = []
sum_total = 0
#Print each row
for line in open_file:
	print(line)
	arr = line.rstrip("\n").split(",")
	cup_arr.append(arr[2])
	print(arr[3], arr[4])
	num = float(arr[3]) * float(arr[4])
	num = format(num, '.2f')
	num = float(num)
	sum_total += num
	total_arr.append(num)
	

#Print cupcake type
for type in cup_arr:
	print(type)
for capita in total_arr:
	print(capita)
print(format(sum_total, '.2f'))

open_file.close()

redo =open("sheet.csv")
graph = {
	"Chocolate": 0,
	"Strawberry": 0,
	"Vanilla": 0
}
	


for line in redo:
	arr = line.rstrip("\n").split(",")
	graph[arr[2]] += float(arr[3])*float(arr[4])
print("Chocolate Income: ", format(graph["Chocolate"],".2f"))
print("Strawberry Income: ", format(graph["Strawberry"],".2f"))
print("Vanilla Income: ", format(graph["Vanilla"],".2f"))
