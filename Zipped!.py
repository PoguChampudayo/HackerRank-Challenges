from numpy import average
n, m = map(int, input().split())
total_score = []
for i in range(m):
    total_score.append(list(map(float, input().split())))
for elem in zip(*total_score):
    print(average(elem))
    
# Sample input
# 5 3
# 89 90 78 93 80
# 90 91 85 88 86  
# 91 92 83 89 90.5
# Sample Output
# 90.0 
# 91.0 
# 82.0 
# 90.0 
# 85.5     