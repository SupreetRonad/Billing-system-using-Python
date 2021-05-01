
d={'1':["Coffee",15],'2':["Cold Drinks",15],'3':["Omlete",20],'4':["Jaamun",12],'5':["Chkn sdwch",40],'6':["Noodles",35],'7':["Fried rice",40],'8':["Dosa Sambar",30]}
c={}
f=1
print("Fno.\t Food\t\tCost")
print("-"*30)
for l in d.keys():
        print(l,".\t",d[l][0],"\t",d[l][1]," Rs")
print('Maximum Allowed Qty : 9');print("PRESS 'ENTER' TO PROCEED TO BILLING  at F.no\n")
while f!='':
    f=input("Fno : ")
    if f in d.keys():
                q=input("\t Qty : ");gt=''
                for i in q:
                        if ord(i) in range(49,58):
                                gt+=i
                        else:gt='0'
                                
                if gt!='0':
                        if int(f) not in c:c.update({int(f):int(gt)})
                        else:c[int(f)]+=int(gt)
                else:print('Invalid Input');
    elif f not in d.keys() and f!='':
                print("Invalid Input");                
a=input("Any offers/ Raises? (O/R/N) : ").upper()
if a=="O":z,x=0.01*(-int(input("Enter Offer/Discount %: "))),"Discount -- "
elif a=="R":z,x=0.01*int(input("Enter Raises %: ")),"Raises -- "
else:z,x=0,'Offers/Discount--'
print("-"*65)
print("S.No\t\t Food\t\t\tQty\t\tCost")
print("-"*65);j=1;tt=[]
for i in c.keys():
    t=c[i]*d[str(i)][1];tt.append(t)
    print(j,"\t"*2,d[str(i)][0],"\t"*2,c[i],"\t"*2,t,"/-")
    j+=1
print("-"*65)
print("\t\t\t\t\t Sub Total -- ",sum(tt),'/-','\n\t\t\t\t\t',x,abs(z)*100,'%','\n','-'*65,'\n\t\t\t\t\t Total -- ',sum(tt)+sum(tt)*z,'/-')
print("-"*65)
print("\t\t\t-----"," THANK YOU ","-----");
a=input('PRESS ANY KEY TO EXIT')
    

       
