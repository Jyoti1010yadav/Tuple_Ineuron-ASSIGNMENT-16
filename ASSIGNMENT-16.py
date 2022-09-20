# 1. Write a python script to store multiple items in a single variable ( Items are “Java” ,“Python”, “SQL”, “C” ) using tuple
tuple1=("Java","Python", "SQL", "C")
print(tuple1)
print()

# 2. Write a python program to store only one item using tuple.
one_item=("jyoti",)
print(one_item,type(one_item))
print()

# 3. Write a python program to reverse the tuple.
items=("jyoti","ashu",5,63.2,45,86,"smart","care")
for i in items:
    print(i)
print()    

# 4. Write a python program to Swap two tuples in Python.
tuple1=("jyoti","ashu","2",1,6,8,12)
tuple2=("career","focus","6",45,23)
print("Before swap: tuple1 ",tuple1)
print("Before swap: tuple2 ",tuple2)
print()
tuple1,tuple2=tuple2,tuple1
print("after swap: tuple1 ",tuple1)
print("after swap: tuple2 ",tuple2)
print()

# 5. Write a python program to check if all items in the tuple are the same.
tuple1=("jyoti","ashu","2",1,6,8,12)
tuple2=("career","focus","6",45,23)
print(tuple1,"and ",tuple2,"all items in the tuple are the same.",tuple1==tuple2)
t1=(2,6,4,8)
t2=(2,6,4,8)
print(t1,"and ",t2,"all items in the tuple are the same.",t1==t2)
print()

# 6. Write a python program to divide the tuple into four variables. tuple1=(100, 200, 300, 400)
tuple1=(100, 200, 300, 400)
a,b,c,d=tuple1
print("tuple1",tuple1)
print("a=",a,"b=",b,"c=",c,"d=",d,sep=" ")
print()

# 7. Write a python program to copy elements 4 and 5 from the following tuple into a new tuple. tuple1=(1,2,3,4,5,6)
tuple1=(1,2,3,4,5,6)
list_tuple=list(tuple1)
list=[]
for i in list_tuple:
    if i==5 or i==6:
        list.append(i)
        continue
print(tuple(list))
print()
# 8. Write a python program to Sort a tuple of tuples by the second item. tuple1 = (('a', 21),('b', 37),('c', 11), ('d',29))
tuple1 = (('a', 21),('b', 37),('c', 11), ('d',29))
sort_tuple=sorted(tuple1,key=lambda a:a[1])
print(sort_tuple)
print()

# 9. Write a python program to print the value 20 from given nested tuple tuple1 = ("Python", [10, 20, 30], (2, 4, 16))
tuple1 = ("Python", [10, 20, 30], (2, 4, 16))
print(tuple1[1][1])
print()

# 10. Write a python program to change the first item (22) of a list within the following tuple to 222. tuple1 = (11, [22, 33], 44, 55)

'''
if anyone is just reading my code ,plz tell me this commented code are why wrong becoz its show type error?
tuple_1 = (11, [22, 33], 44, 55)
print(tuple_1)
x=list(tuple_1)
x[1][0]=222
print(tuple(x))
'''
# 10. Write a python program to change the first item (22) of a list within the following tuple to 222. tuple1 = (11, [22, 33], 44, 55)
# note:----> You can modify the contents of lists but not of tuples. And according to question 
# we should also know that only a reference of the list is stored into a tuple.
tuple1 = (11, [22, 33], 44, 55)
tuple1[1][0]= 222
print(tuple1)
