x, y, w, h = map(int, input().split())
# (x,y)
# (w,h)

Min = min(x, y, w-x, h-y)
print(Min)


# 왼쪽 꼭짓점(0, 0)
# (x,y) 에서 왼쪽경계면(y축) 까지의 거리는 x
# (x,y) 에서 아래쪽경계면(x축) 까지의 거리는 y
# (x,y) 에서 오른쪽 경계면 까지의 거리는 w-x
# (x,y) 에서 위쪽 경계면 까지의 거리는 h-y
