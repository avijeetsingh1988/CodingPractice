lst=[5,4,1,2,3,8,7,9]
fl=0
for lv in lst:
    if lv > fl:
        fl=lv

sl = 0
for lv in lst:
    if lv > sl and lv != fl:
        sl=lv

print(sl)



lst1 = [7,7,7,7,7,2,7,7,7,7]
print()