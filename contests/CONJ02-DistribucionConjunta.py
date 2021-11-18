N = int(input())
M = int(input()) #Num Var
p = int(input()) #hiper

headers = input().split(',')
data = []

for i in range(M):
  data.append(input().split(','))

aux = input().split(",")


def idx(name, headers):
    for i in range(len(headers)):
        if(headers[i] == name):
            return i
    
    return 0

cols = []
for x in aux:
    cols.append(idx(x, headers))

cols.sort()

def get_pcon(cols):
    exp1 = p
    for x in data:
        cnt = 0
        for i in range(len(cols)):
            if(x[cols[i][0]] == cols[i][1]):
                cnt+= 1
        
        if(cnt == len(cols)):
            exp1+= 1
    
    cards = 1
    for col in cols:
        st = set()
        for elem in data:
            st.add(elem[col[0]])
        
        cards*= len(st)
    
    val_cal = ""
    for i in range(len(cols)):
        if(i != 0):
            val_cal+=","
        val_cal+= headers[cols[i][0]] + "=" + cols[i][1] 
    
    print( "P(" + val_cal + ")={:.6f}".format(exp1/(M + p*cards)) )

def uniq_vals(data, col):
    st = []
    for x in data:
        if(x[col] in st):
            continue
        st.append(x[col])
    
    return st
    

uniqs = []
cnt = []
ids = []
vuelta = []
total = 1

for x in cols:
    uniqs.append(list(uniq_vals(data, x)))
    if(total == 0):
        ids.append(1)
    else:
        ids.append(total)
        
    total*= len(uniqs[-1])
    cnt.append(0)
    vuelta.append(0)




for u in range(total):
    vals = []
    i = 0
    for x in cols:
        vals.append([x, uniqs[i][cnt[i]]])
        i+= 1
    
    get_pcon(vals)
    
    for j in range(len(cols)):
        vuelta[j]+= 1
        if(vuelta[j] == ids[j]):
            cnt[j] = (cnt[j] + 1)%len(uniqs[j])
            vuelta[j] = 0

        
    