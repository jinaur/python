n, m = map(int, input().split())

score = [0]*(m+1)
for i in range(0, n) :
    s, t = map(int, input().split())
    for j in range(m, t-1, -1) :
        score[j] = max(score[j], score[j-t]+s)

print(score[m])

# 2번 하지않게 뒤에서부터 감
# j-t가 0미만이 되면 그 시간대엔 문제를 풀수없다
# j = 11 t = 12 일땐 안되고
# j-t >= 5 일땐 score[5~8] = 10 이기에 +s해서 35나옴
# j-t < 5 일땐 score[1~4] = 0 +s해서 25나옴

