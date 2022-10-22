import os

lines = []
with open("output.txt", 'r') as f:
    for l in f.readlines():
        lines.append(l.strip())

lines = [l.split() for l in lines]

d = 0
for l in lines:
    # if l[2] == '279':
    #     os.system(f'aws s3 rm s3://speechparacrawl/{l[3]}')
    if int(l[2]) <= 279:
        # os.system(f'aws s3 rm s3://speechparacrawl/{l[3]}')
        d += 1
print(d)