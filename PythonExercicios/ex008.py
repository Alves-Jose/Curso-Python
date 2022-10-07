m=float(input('\033[4;31mDigite uma metragem: \033[m'))
cm=m*100
mm=m*1000
km=m/1000
dc=m/10
hc=m/100
dec=m*10
print('\033[1;35mSua medida em metros é:{:.0f} \nSua medida em centímetros é:{:.0f} \nSua medida em milímetros é:{:.0f} \nSua medida em decímetros é:{:.0f} \nSua medida em decâmetro é:{:.0f} \nSua medida em hectômetro é:{:.0f} \nSua medida em quilômetros é:{:.1f}\033[m'.format(m, cm, mm, dec, dc, hc, km))