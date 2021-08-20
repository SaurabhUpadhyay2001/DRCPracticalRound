import json
path = r"F:\DRC Practical Round\test.json"
path_o = r"F:\DRC Practical Round\output1.json"
list1=[]
def change(body):
    if len(body)==0:
        return list1
    else:
        a=body[0]
        b=a.replace('+type','+size@5+type')            #replacing 1st element everytime
        list1.append(b)
        body.pop(0)
        return change(body)             #Recursive Body call

con=open(path,'r')
body=con.readlines()      #all content is in body
a=change(body)
abc=open(path_o,'w')
abc.writelines(a)          #writing all changes to output file
