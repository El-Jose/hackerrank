# Enter your code here. Read input from STDIN. Print output to STDOUT
word = input()
lowercase = []
uppercase = []
odd_digits = []
even_digits = []

for i in word:
    if i.isnumeric() and int(i) % 2 == 0:
        even_digits.append(i)
    elif i.isnumeric() and int(i) % 2 != 0:
        odd_digits.append(i)
    elif i.isupper():
        uppercase.append(i)
    elif i.islower():
        lowercase.append(i)

lowercase = "".join(sorted(lowercase))
uppercase = "".join(sorted(uppercase))
odd_digits = "".join(sorted(odd_digits))
even_digits = "".join(sorted(even_digits))
        
print(f"{lowercase}{uppercase}{odd_digits}{even_digits}")
#print(*(sorted(input(), key=lambda x: (x.isdigit(), x.isdigit() and int(x)%2==0, #x.isupper(), x.islower(), x))), sep='')
