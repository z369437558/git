# a simple parser for python. use get_number() and get_word() to read
#def parser():
 ##      data = list(input().split(' '))
   #     for number in data:
    #        if len(number) > 0:
     #           yield(number)   
#
#input_parser = parser()

#def get_word():
 #   global input_parser
  #  return next(input_parser)

##   data = get_word()
  #  try:
   #     return int(data)
    #except ValueError:
     #   return float(data)

# numpy and scipy are available for use
import numpy
import scipy


a = list(input().split(";"))#读入stop word
b = list(input().split(";"))#读入 key word
dict1 = dict()
flag = 0
while(True):
    d = input()
    if '</body>' in d:
        break
    if '<title>' in c:
        while(True):
            cc = 0
            if cc==0:
                c = d
            else:
                c = input()
            if '</title>' in c:
                break
            c = c.replace(',','')
            c = c.replace('!','')
            c = c.replace('?','')
            c = c.replace('.','')
            c = list(c.split(" "))
            c = [s.lower() for s in c if isinstance(s,str)==True]
            for keyword in b:
                if keyword in a:
                    continue
                else:
                    count = 0
                    for kk in c:
                        if kk==keyword:
                            count=count+1
                    vlue1 = count*5
                    dict1[keyword]=vlue1
            cc = cc+1
    if '<abstract>' in d:
        while(True):
            cc = 0
            if cc==0:
                c = d
            else:
                c = input()
            if '</abstract>' in c:
                break
            c = c.replace(',','')
            c = c.replace('!','')
            c = c.replace('?','')
            c = c.replace('.','')
            c = list(c.split(" "))
            c = [s.lower() for s in c if isinstance(s,str)==True]
            for keyword in b:
                if keyword in a:
                    continue
                else:
                    count = 0
                    for kk in c:
                        if kk==keyword:
                            count=count+1
                    vlue2 = count*3
                    dict2[keyword]=vlue1
            cc = cc+1
    if '<body>' in d:
        while(True):
            cc = 0
            if cc==0:
                c = d
            else:
                c = input()
            if '</body>' in c:
                flag = 1
            if '</body>' in c:
                break
            c = c.replace(',','')
            c = c.replace('!','')
            c = c.replace('?','')
            c = c.replace('.','')
            c = list(c.split(" "))
            c = [s.lower() for s in c if isinstance(s,str)==True]
            for keyword in b:
                if keyword in a:
                    continue
                else:
                    count = 0
                    for kk in c:
                        if kk==keyword:
                            count=count+1
                    vlue3 = count*5
                    dict3[keyword]=vlue3
            cc = cc+1
    if flag==1:
        break
dict_c = dict()
for key in dict1:
    dict_c[key]=dict1[key]+dict2[key]+dict3[key]

    
print(dict_c)