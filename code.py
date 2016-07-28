
LL =


next={}
for s in LL:
  for i in range(0,len(s)-5):
    next[s[i:i+5]]=s[i+5]
#changing the number does solve the problem
begin="MSKDT"
seq=begin
#the problem is that there are multiple 4 letter sequences that are the same
while True:
      if begin in next:
         n=next[begin]
         seq=seq+n
         begin=begin[1:5]+n
      else:
       break
## without the break it would just print infintly 
print(seq)
      
