msg = 50
total =[]
trimmed=[]
n=30
for msgs in range(1,n+1):
    total.append(msgs*msg)
    trimmed.append(min(msgs, 5) * msg)

sum(total)
print(sum(total))
print(sum(trimmed))
