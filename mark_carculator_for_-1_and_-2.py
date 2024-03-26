mark1 = 0
mark2 = 0
mark3 = 0
mark4 = 0
mark5 = 0
mark6 = 0
ma1 = 0 
ma2 = 0
ma3 = 0
ma4 = 0
ma5 = 0
ma6 = 0
print('Hi there,')
name=input("What is your name : ")
print('Hi',name,',Nice to meet you')
print('This is a program that will help you find result of your exam mark')
c = int(input('Which class you are studying."1" for +2, "2" for +1 : '))
if c == 1:
  mark1 = int(input('How much mark do you get in English : '))
  mark2 = int(input('How much mark do you get in Physics : '))
  mark3 = int(input('How much mark do you get in Malayalam : '))
  mark4 = int(input('How much mark do you get in Maths : '))
  mark5 = int(input('How much mark do you get in Chemistry : '))
  mark6 = int(input('How much mark do you get in Biology : '))
elif c == 2:
  ma1 = int(input('How much mark do you get in English : '))
  ma2 = int(input('How much mark do you get in Malaayalam : '))
  ma3 = int(input('How much mark do you get in Maths : '))
  ma4 = int(input('How much mark do you get in Biology : '))
  ma5 = int(input('How much mark do you get in Chemistry : '))
  ma6 = int(input('How much mark do you get in Physics : '))
else: 
  print('Please enter your class')
if c == 1 :
  print('These are the result of your +2 exam')
  if    mark1 >=90 and mark1 <=100 : 
     print ("You have a+ for english in +2")
  elif    mark1>=80 and mark1<=89 :
     print('You have a for english in +2')
  elif    mark1>=70 and mark1<=79 :
     print('You have b+ for english+2')
  elif    mark1>=60 and mark1<=69 :
     print('You have b for english in +2')
  elif    mark1>=50 and mark1<=59 :
     print('You have c for english in +2')
  elif    mark1>=40 and mark1<=49 :
     print('You have d+ for english in +2')
  elif    mark1>=30 and mark1<=39 :
     print('You have d for english in +2')
  elif   mark1<29 :
     print('You have failed for english in +2')
  else:
     print('invalid.Please correct the mark of english') 

  if    mark2 >=108 and mark2 <=120: 
    print('You have a+ for physics in +2')  
  elif   mark2>=96 and mark2<=107:
     print ('You have a for physics in +2') 
  elif   mark2>=84 and mark2<=95:
     print ('You have b+ for physics in +2') 
  elif   mark2>=72 and mark2<=83:
     print ('You have b for physics in +2')  
  elif   mark2>=60 and mark2<=71:
     print ('You have c for physics in +2') 
  elif   mark2>=48 and mark2<=59:
     print ('You have d+ for physics in +2') 
  elif   mark2>=36 and mark2<=47:
     print ('You have d for physics in +2') 
  elif    mark2<36 :
     print('You have failed for physics in +2')
  else:
     print('invalid.Please correct the mark of physics')

  if    mark3>=90 and mark3 <=100:     
     print ('You have a+ for malayalam in +2')
  elif    mark3>=80 and mark3<=89 :
     print('You have a for malayalam in +2')
  elif    mark3>=70 and mark3<=79 :
     print('You have b+ for malayalam in +2')
  elif    mark3>=60 and mark3<=69 :
     print('You have b for malayalam in +2')
  elif    mark3>=50 and mark3<=59 :
     print('You have c for malayalam in +2')
  elif    mark3>=40 and mark3<=49 :
     print('You have d+ for malayalam in +2')
  elif    mark3>=30 and mark3<=39 :
     print('You have d for malayalam in +2')
  elif   mark3<29 :
     print('You have failed for malayalam in +2')
  else:
     print('invalid.Please correct the mark of malayalam')   

  if    mark4>=108 and mark4<=120: 
    print('You have a+ for maths in +2')  
  elif   mark4>=96 and mark4<=107:
     print ('You have a for maths in +2') 
  elif   mark4>=84 and mark4<=95:
     print ('You have b+ for maths in +2') 
  elif   mark4>=72 and mark4<=83:
     print ('You have b for maths in +2')  
  elif   mark4>=60 and mark4<=71:
     print ('You have c for maths in +2')  
  elif   mark4>=48 and mark4<=59:
     print ('You have d+ for maths in +2') 
  elif   mark4>=36 and mark4<=47:
     print ('You have d for maths in +2') 
  elif    mark4<36 :
     print('You have failed for maths in +2')
  else:
     print('invalid.Please correct the mark of maths')

  if    mark5>=108 and mark5<=120: 
    print('You have a+ for chemistry in +2')  
  elif   mark5>=96 and mark5<=107: 
     print ('You have a for chemistry in +2') 
  elif   mark5>=84 and mark5<=95:
     print ('You have b+ for chemistry in +2') 
  elif   mark5>=72 and mark5<=83:
     print ('You have b for chemistry in +2')  
  elif   mark5>=60 and mark5<=71:
     print ('You have c for chemistry in +2') 
  elif   mark5>=48 and mark5<=59:
     print ('You have d+ for chemistry in +2') 
  elif   mark5>=36 and mark5<=47:
     print ('You have d for chemistry in +2') 
  elif    mark5<36 :
     print('You have failed for chemistry in +2')
  else:
     print('invalid.Please correct the mark of chemistry')         


  if    mark6 >=108 and mark6 <=120: 
    print('You have a+ for biology in +2')  
  elif   mark6>=96 and mark6<=107:
     print ('You have a for biology in +2') 
  elif   mark6>=84 and mark6<=95:
     print ('You have b+ for biology in +2') 
  elif   mark6>=72 and mark6<=83:
     print ('You have b for biology in +2')  
  elif   mark6>=60 and mark6<=71:
     print ('You have c for biology in +2') 
  elif   mark6>=48 and mark6<=59:
     print ('You have d+ for biology in +2') 
  elif   mark6>=36 and mark6<=47:
     print ('You have d for biology in +2') 
  elif    mark6<36 :
     print('You have failed for biology in +2')
  elif    mark6>120:
     print('invalid.Please correct the mark of biology')                    

  ar =(mark1+mark2+mark3+mark4+mark5+mark6)                                    
  percent=(ar/680*100)     
  if  mark1<=100 and mark2<=120 and mark3<=100 and mark4<=120 and mark5<=120 and mark6<=120: 
    print (name,'.You have',       percent,'percentage of mark in +2')
    print('Total mark = ',ar,' out of 680') 
  else:
    print('SORRY',name,'.We cannot show the percentage because you have enter wrong mark.',name,'Please check the marks you have entered')

if c == 2 :
  print('These are the result of your +1 exam')
  if    ma1>=90 and ma1 <=100 :
     print ("You have a+ for english in +1")
  elif    ma1>=80 and ma1<=89 :
     print('You have a for english in +1')
  elif    ma1>=70 and ma1<=79 :
     print('You have b+ for english in +1')
  elif    ma1>=60 and ma1<=69 :
     print('You have b for english in +1')
  elif    ma1>=50 and ma1<=59 :
     print ('You have c for english in +1')
  elif    ma1>=40 and ma1<=49 :
     print('You have d+ for english in +1')
  elif    ma1>=30 and ma1<=39 :
     print('You have d for english in +1')
  elif   ma1<29 :
     print('You have failed for english in +1')
  else :
     print('invalid.Please correct the mark of english')    
  
  if    ma2>=90 and ma2 <=100 :
     print ("You have a+ for malaayalam in +1")
  elif    ma2>=80 and ma2<=89 :
     print('You have a for malaayalam in +1')
  elif    ma2>=70 and ma2<=79 :
     print('You have b+ for malaayalam in +1')
  elif    ma2>=60 and ma2<=69 :
     print('You have b for malaayalam in +1')
  elif    ma2>=50 and ma2<=59 :
     print ('You have c for malaayalam in +1')
  elif    ma2>=40 and ma2<=49 :
     print('You have d+ for malaayalam in +1')
  elif    ma2>=30 and ma2<=39  :
     print('You have d for malaayalam in +1')
  elif   ma2<29 :
     print('You have failed for malaayalam in +1')
  else :
     print('invalid.Please correct the mark of malaayalam')

  if    ma3>=73 and ma3 <=80 :
     print ("You have a+ for maths in +1")              
  elif    ma3>=64 and ma3<=72 :
     print('You have a for maths in +1')
  elif    ma3>=54 and ma3<=63 :
     print('You have b+ for maths in +1')
  elif    ma3>=48 and ma3<=55 :
     print('You have b for maths in +1')
  elif    ma3>=40 and ma3<=47 :
     print ('You have c for maths in +1')
  elif   ma3<39 :
     print('You have failed for maths in +1')
  else :
     print('invalid.Please correct the mark of maths')
  
  if    ma4>=73and ma4 <=80:
     print ("You have a+ for biology in +1")
  elif    ma4>=64 and ma4<=72:
     print('You have a for biology in +1')
  elif    ma4>=54 and ma4<=63:
     print('You have b+ for biology in +1')
  elif    ma4>=48 and ma4<=55:
     print('You have b for biology in +1')
  elif    ma4>=40 and ma4<=47:
     print ('You have c for biology in +1')
  elif    ma4<39:
     print('You have failed for biology in +1')
  else:
     print('invalid.Please correct the mark of biology')

  if    ma5>=73 and ma5 <=80 :
     print ("You have a+ for chemistry in +1")  
  elif    ma5>=64 and ma5<=72:
     print('You have a for chemistry in +1')
  elif    ma5>=54 and ma5<=63:
     print('You have b+ for chemistry in +1')
  elif    ma5>=48 and ma5<=55:
     print('You have b for chemistry in +1')
  elif    ma5>=40 and ma5<=47:
     print('You have c for chemistry in +1')
  elif    ma5<39:
     print('You have failed for chemistry in +1')
  else:
     print('invalid.Please correct the mark of chemistry')

  if    ma6>=73 and ma6 <=80 :
     print ("You have a+ for physics in +1")
  elif    ma6>=64 and ma6<=72:
     print('You have a for physics in +1')
  elif    ma6>=54 and ma6<=63:
     print('You have b+ for physics in +1')
  elif    ma6>=48 and ma6<=55:
     print('You have b for physics in +1')
  elif    ma6>=40 and ma6<=47:
     print('You have c for physics in +1')
  elif    ma6<39:
     print('You have failed for physics in +1')
  else:
     print('invalid.Please correct the mark of physics')
  aera =(ma1+ma2+ma3+ma4+ma5+ma6)
  percentage = (aera/520*100)
  if ma1 and ma2 <=100 and ma3 and ma4 and ma5 and ma6 <=80:
    print(name,'.You have', percentage,'percentage of mark in +1')
    print('Total mark = ',aera,' out of 520')
  else:
    print('SORRY',name,'.We cannot show the percentage because you have enter wrong mark.',name,'Please check the marks you have entered')