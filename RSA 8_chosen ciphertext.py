
from Crypto.Util.number import bytes_to_long, getPrime
from gmpy2 import invert
import os

encrypted_flag =1105211821110344174160775464061672203721232650052900248858543621128425223193430884413358529380064276847992984424565434775695769013604001405282985768196424036630431686807432231771907235979727365916462557180173188778128971259553938741794055126831651572800596935648787624798316712461600672439442983086791137335392434798640492624323275368122315475573902708832701785619731538416444272306750689063382291983834256144019265592328302896473175263209789040457510929774956219374282337857808328483148043182903906258411694780501183864244314076792014984714018927701643460635855210929922693796948077196789820160064532473650755631070
n=12822249141979253601236284245899066593046559950225401453514318543361360872667195334366023171299118361121192669156546561922459630015648797033641126378691074629256751734316623367990692859729091514636318398123382374297630888558469310390426954981849365154856804809898193291548037286081702131022099703064508866430990298074996382688361385469975393114655102379467001515131842814445158169428065496555219330633225104568316181052807628554680101304682748392971157282715743219803918710111294986669056977928600675194698286220703198363983652373964072079315629226387512118761503558740248631993763666438818817692138335978550100681417
e = 65537
"""
已知C=flag^e(mod n)
令C_1=2^e(mod n)
则 C_2=(2*flag)^e(mod n)
计算2*flag=C_3(mod n)
"""
C_1=pow(2,e,n)
C_2=pow(C_1*encrypted_flag,1,n)
print(C_2)
C_3=2377853285045091334301900693487109554495953153969168730189187035564660815054879448838271250242893617798391754757678295221043724065716713769621016417820821807371029650716958061897403922816482811205929162804022919965848286435492014389537110205368026442581810736709703956729939668742467405055892742251224431722868215859392103641138917965029104974190457363246881433834728804817586432255293540874343757081105739636587823425165657642403146190352392628778034870494326142024379884778534542520643430885605718341386306284834221359669429079313325442007874294455440095558404661797208213670774653023049174003011486685379237017190
"""
python算不出来 故以下代码在sage计算
i=0
while True:
    if (C_3+i*n)%2==0:
        print((C_3+i*n)/2)
        break
    i=i+1

"""