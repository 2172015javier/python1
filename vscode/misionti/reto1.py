sb, hx, bn= input().split()
sb= float(sb)
hx= int(hx)
bn= int(bn)
ht= sb/192

if bn==1:
    bono= sb*0.05
else:
    bono=0

extras= hx*(1.25*ht) 
stotal= sb+extras+bono
salud= stotal*0.035
pencion= stotal*0.04
caja= stotal*0.01
stotal = round(stotal - (salud + pencion + caja),1)
print (stotal)