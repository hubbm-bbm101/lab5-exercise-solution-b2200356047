N = int(input("Enter a number N:"))
sum_odd= 0
sum_even= 0
even_numbers= 0

for number in range (1,N+1):
    if number%2==0:
        sum_even = sum_even + number
        even_numbers = even_numbers + 1
        average= sum_even/even_numbers
    else:
        sum_odd = sum_odd + number
print(average)
print(sum_odd)
