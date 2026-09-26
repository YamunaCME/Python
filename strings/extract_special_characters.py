s2="abc1234567bbbb#####@@"
num=""
for x in s2:
    if not x.isalnum() and not x.isspace():
        num+=x
print(num)