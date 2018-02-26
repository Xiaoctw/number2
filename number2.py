sites={}
i=0
filename="file"
for line in open(filename):
    while True:
        sites=None
        i=line.find("http://",i)
        if i>-1:
            i+=len("http://")
            for j in range(i,len(line)):
                if not (line[j].isalnum() or line[j] in ".-"):
                    site=line[i:j].lower()
                    break
            if site and "." in site:
                sites.setdefault(site,set()).add(filename)#字典当中的值为一个集合
a=set()
b={}
b[3]="fsd"
print(b)
seta=set()
seta.add("fds")
seta.add("trr")
print(seta)
x=["zebra",49,-879,"rdddd"]
b=x.copy()
print(b)
数字="Number"

