numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

numbers[4] = 0
a = round(sum(numbers) / (len(numbers)), 2)
numbers[4] = a

print("Измененный список:", numbers)
