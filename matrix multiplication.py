mat_a=[[2,2],[2,2]]
mat_b=[[2,2],[2,2]]

rows_a=len(mat_a)
cols_a=len(mat_a[0])
rows_b=len(mat_b)
cols_b=len(mat_b[0])

result=[[0,0],[0,0]]

for i in range(rows_a):
    for j in range(cols_b):
        for k in range(rows_a):
            result[i][j]+=mat_a[i][k]*mat_b[k][j]

for row in result:
    print(row)
































