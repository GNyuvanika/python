mat_a=[[4,4],[4,4]]
mat_b=[[8,8],[8,8]]

rows_a=len(mat_a)
cols_a=len(mat_a[0])
rows_b=len(mat_b)
cols_b=len(mat_b[0])

result=[[0,0],[0,0]]

for i in range(rows_a):
    for j in range(cols_b):
        for k in range(cols_a):
            result[i][j]=mat_a[i][k]+mat_b[k][j]

for rows in result:
    print(rows)
