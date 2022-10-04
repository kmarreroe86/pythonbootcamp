isWinning = True

number1 = 8
number2 = 3

result1 = number1 / number2 #2.6666
result2 = number1 // number2 #2 => Floor round
result3 = round(number1 / number2) #3 => closest integer value
result4 = round(number1 / number2, 2) #2.67 => specific decimal places

print(result2)


#f-string || String interpolation
print(f"number {number1} divided by {number2} is equal to {result1}")


# 