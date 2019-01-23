import numpy as np
a =np.array([1,2,3])
print(a.shape)
print(a.dtype)

###Different type
b=np.array([])

dtype-data type
shape- length of array along each dimension
size - number of elements in the entire array

doubleD array:
c=np.array([(1,2,3),(4,5,6),(4,5,6,)])
print(c.shape)

horizontally or vertically append the data
hstack-horizontally append the data
vstack-vertically append the data

f=np.array([1,2,3])
g=np.array([4,5,6])
print("horizontal append",np.hstack((f,g)))
print("vertical appned",np.vstack((f,g)))

import numpy as geek
print("A\n",gek.arrange(stop=6).reshape(2,3),"\n")
print("A\n",geek.arrange(start=4,stop=10).reshape(2,3),"\n")
print("A\n",geek.arrange(4,20).reashape(4.20.3),"\n")

to generate random numbers
numpy.random.normal(loc,scale,size)
loc-mean, the cenre of distribution
scale-
size-

import numpy as np
np.random.seed(0) # seed for reproductivity
x1=np.random.randint(10,size=0) #one dimensional array
x2=np.random.randint(10,size=(3,4))#two-D
x1=np .random.randint(10,size=(3,4,5))# three-D
print(x1)
print(x2)
print(x3)
print("x3 ndim",x3.ndim)
print("x3 ndim",x3.ndim)

#extract single elements
print(x1[0])
print(x2[0,0],x2[1,2])
print(x3[2,3,4])

#extract subarrays
print(x[:5])#first five elements
print(x[::-1])#last element
print(x[5:])#after 5
print(x[4:7])#middle elements

#two-D array
print(x2[:2,:3])#two rows three columns
print(x2[:3.::2])#all rows, every other columns
#reverse
print(x2)
print(x2[::-1,::-1])

#accessing rows an columns
print(x2[:,0])#first column of x2
print(x2[:,1])#second column of x2

#spliting and rearranging
a-np.arrange(16).reashape(4,4)
print("First array",a)
print("\n")
print("Vertical splitting")
b=np.vsplit(a,2)
print(b)

#broadcasting
import numpy as np
a=np.array([0,1,2])
b=np.array([5,5,5])
print(a+b)

#changing dimensions
a=np.arrange(3)
b=np.arrange(3)[;np.newaxis]	#dispplay new dimensions
print(a)
print(a+b)

#broadcasting rules from slides
#rule1: if the shape of two arrays does not match i any dimension, 
#the array with shape equal to 1 in that dimension is streched to math the other shape
#rule2: if the two arrays differ in their number of dimensions, 
#the shape of the one with fewer dimensions is paded wih oes on its leadig left sides
#rule3: if in any dimensions the sies disagree and neither is equal to one, an error is occurred

a[:,0]# first column
a[:,1]#second column
a[0,:]#first row

#fancy indexing
import numpy as np
rend=np.random.RandomState(42)
x-rand.randint(100,size=10)
print(x)
ind=[3,7,4]
print(x[ind])#passing a single list or array of indicies to obtain the same result
print(x[3],x[7],s[2])#to access three different elements

#fancy
x=np.arrange(1,2).reshape(3,4)
print(x)
row=np.array([0,1,2])
col=np.array([2,1,3])
x[row,col]#will extract (0,2) (1,1) (2,3)

#combined indexing
x=np.arrange(1,2).reshape(3,4)
print(x)
print(x[2,[2,0,1]])# third row, three element: 3rd,1st,2nd element
#slicing
print(x[0:,[2,0,1]])
print(x[1:,[2,0,1]])