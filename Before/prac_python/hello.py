fruits = ['사과','배','배','감','수박','귤','딸기','사과','배','수박']
def fruit_num(fruits, target):
  count = 0
  for fruit in fruits:
    if fruit == target:
      print('target')
      count += 1
  return count


water_num = fruit_num(fruits, '수박')
print(water_num)

def count_fruits(target):
	count = 0
	for fruit in fruits:
		if fruit == target:
			count += 1
	return count

subak_count = count_fruits('수박')
print(subak_count)
