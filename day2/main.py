with open('input.txt') as f:
  text = f.read().strip().split('\n')

sum = 0
for i in text:
    #get each single choice of a line
    round = i.split()
    # (A|X = ROCK  ) (B|Y = PAPER  ) (C|Z = SCISSOR )

    c1 = round[0]
    c2 = round[1]
    if(c1 == 'A' and c2 == 'X'):
      sum += 4
    elif(c1 == 'B' and c2 == 'Y'):
      sum+= 5
    elif(c1 == 'C' and c2 == 'Z'):
      sum+= 6
    elif(c1 == 'A' and c2 == 'Y'):
      sum+=8
    elif(c1 == 'A' and c2 == 'Z'):
      sum+=3
    elif(c1 == 'B' and c2 == 'X'):
      sum+=1
    elif(c1 == 'B' and c2 == 'Z'):
      sum+=9
    elif(c1 == 'C' and c2 == 'X'):
      sum+=7
    elif(c1 == 'C' and c2 == 'Y'):
      sum+=2

print(sum)
    

