M, H = map(int, input().split())
N = int(input())  

max_happiness = 0
for _ in range(N):
    C, B = map(int, input().split())  
    milk_happiness = C * M
    honey_happiness = B * H
    max_happiness += max(milk_happiness, honey_happiness)

print(max_happiness)