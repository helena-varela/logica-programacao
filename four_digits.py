N = (input())
qnts = len(N)

if qnts == 4:
    print(N)
elif qnts == 3:
    print("0"+N)
elif qnts == 2:
    print("00"+N)
elif qnts == 1:
    print("000"+N)