N = int(input()) #Num Var
M = int(input()) #Registros
p = int(input()) #hiper

headers = input().split(',')
data = []

for i in range(M):
  data.append(input().split(','))

q_column = input()

def m(q_value, q_column, data, headers):
  idx = headers.index(q_column)
  cnt = 0
  for row in data:
    if row[idx] == q_value: 
      cnt+=1
  return cnt

def card(q_column, headers, data):
  idx = headers.index(q_column)
  distinct = []
  for row in data:
    if row[idx] not in distinct:
      distinct.append(row[idx])
  return len(distinct)

def get_distinct(q_column, headers, data):
  idx = headers.index(q_column)
  distinct = []
  for row in data:
    if row[idx] not in distinct:
      distinct.append(row[idx])
  return distinct

def porb_marg(q_value, q_column, data, headers):
  # (m[value] + p) / (M + (p * card(column))
  exp1 = m(q_value, q_column, data, headers) + p
  exp2 = M + (p * card(q_column, headers, data))
  return format(exp1/exp2,'.6f')

print("P({})".format(q_column))
for q_val in list(get_distinct(q_column, headers, data)):
  print(q_val,":",porb_marg(q_val, q_column, data, headers),sep="")