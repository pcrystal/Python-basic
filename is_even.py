#funtion tools
#
#import functools
#from functools import reduce
#
#total = reduce(lambda item,running_total:item + running_total,[1,2,3,4,5])
#print(total)

#     how to determine even numbers
#def is_even(numbers): return numbers % 2== 0
  
#numbers = [1,56,234,87,4,76,24,69,90,135]
#
#print(list(filter(is_even,numbers)))

#        how to determine odd numbers
#def is_odd(numbers): return numbers % 2== 1
    
#numbers = [1,56,234,87,4,76,24,69,90,135]

#print(list(filter(is_odd,numbers)))
#
#   how to determine even numbers using lambda

#def is_even(numbers): return numbers % 2== 0
  
#numbers = [1,56,234,87,4,76,24,69,90,135]
#
#print(list(filter(lambda numbers:numbers%2==0,numbers)))
#
#print(list(filter(lambda numbers:numbers%2==1,numbers)))

#         spilting words and length of words
                
#sentence = "the quick brown fox jumps over the lazy dog"
#words = sentence.split()
#print (words)
#print(len(words))
#print(list(len(word) for word in words)

#numbers = [34.6 - 203.4, 44.9,68.3,-12.2,44.6,-12.7]
#print(list(filter(lambda numbers:numbers > 0 ,numbers)))

#numbers=[1,3,4,6,8.4,10,400,5000]
#print(list(filter(lambda numbers:numbers%2==0,numbers)))

#print(list(filter(lambda numbers:numbers%2==0,numbers)))


#list1 = range (1,51)
#print(list(list1))
#print(list(filter(lambda list1:list1 %2==0,list1)))
#print(list(filter(lambda list1:list1 %2==1,list1)))
#print([u for u in list1 if u%2==0])
#print([u for u in list1 if u%2==1])
#  
#        length of words

#def alphabets():
#    words = ("hello", "my","name","is","phoebe")
#    print (list(len(words) for words in words))
#alphabets()

#            capitalise
#def alphabets():
#    capitalise =("hello","my","name","is","phoebe")
#    case =[i.upper() for i in capitalise]
#    length = [len(i) for i in capitalise]
#    print(tuple(zip(case, length)))
#    
#    
#alphabets()

#    factorial
    
def factorial():
    
    num = int(input("enter a number: "))
    
    fact = 1
    
    for i in range(1, num + 1):
        fact = fact * i
        print(fact)
       
       
        
factorial()
