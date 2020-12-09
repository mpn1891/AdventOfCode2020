def GetSum(startpos,length):
    sum = 0
    for i in range(startpos,length,1):
        sum += code[i]
    return sum

code = []

def main():
    
    with open(r"input_01.txt","r") as f:
        for val in f.read().split('\n'):
            code.append(int(val))

    preLen = 25
    problemVal = 0

    for i in range(preLen,len(code),1):
        curVal = code[i]
        preamble = code[i-preLen:i]
        #print (preamble)
        matchFound = 0

        for j in preamble:
            x = curVal - int(j)
            #print(x)
            for k in preamble:
                if k==x:
                    matchFound = 1
                    break
        if matchFound ==1:
            continue
        else:
            print('found:' + str(curVal))
            problemVal = curVal
            break

    start = 0
    end = 0
    wrkSum = 0

    while wrkSum!=problemVal:

        wrkSum = GetSum(start,end)
        if wrkSum < problemVal:
            end+=1
        if wrkSum > problemVal:
            start += 1

    small = problemVal + 1
    large = 0

    for x in range(start,end,1):
        if code[x] < small:
            small = code[x]
        if code[x] > large:
            large = code[x]

    print(start,end)
    print(small+large)

if __name__ == "__main__":
    main()




