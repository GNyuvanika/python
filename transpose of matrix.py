a=[[1,2],[3,4]]
result=[[0,0],[0,0]]
for i in range(len(a)):
    for j in range(len(a)):
        result[i][j]=a[j][i]
for rows in result:
    print(rows)
