with open('input.txt') as f:
  text = f.read().strip().split('\n')

# Part One of advent of code
maxn = 0
count = 0

for x in text:
    if(x == ''):
        count = 0
    else:
        count += int(x)

    if(count > maxn):
        maxn=count

print(maxn)