with open('input.txt') as f:
  text = f.read().strip().split('\n')

# Part One of day1
def partOne():
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
            
# Part Two of day1
def partTwo():
    max1 = 0
    max2 = 0
    max3 = 0
    count = 0
    for x in text:
            if(x == ''):
                count = 0
            else:
                count += int(x)
            if count > max1: 
                max3 = max2
                max2 = max1
                max1 = count
            elif count > max2:
                max3 = max2
                max2 = count    
            elif count > max3:
                max3 = count    
    print(max1+max2+max3)
    
partOne()
partTwo()



