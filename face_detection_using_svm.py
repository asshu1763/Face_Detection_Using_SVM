import matplotlib.pyplot as plt
import matplotlib.image as mimg
import numpy as np

samp=20
train_data=np.zeros((20*5,144*120*3))
train_label=np.zeros((20*5))

count=-1
plt.figure(1)
plt.ion()

for i in range(1,6):
  for j in range(1,samp+1):
    plt.cla()
    count=count+1
    print(count+1)
    path='facesample/facesamples/a%d/%d.png'%(i,j)
    im=mimg.imread(path)
    feat=im.reshape(1,-1)
    train_data[count,:]=feat
    train_label[count]=i

    plt.imshow(im,cmap='gray')
    plt.title('actress no.::  '+str(i)+'  ::  sample no.::  '+str(j))
    plt.pause(0.1)

test_data=np.zeros((1,144*120*3))
test_label=np.zeros(1)

a=int(input("Enter the number to select the image you want to test (choose only from 1 to 15) :: "))

count=-1
for i in range(a,a+1):
  path='facesample/testdata/%d.png'%i
  im=mimg.imread(path)
  feat=im.reshape(1,-1)
  test_data[count,:]=feat
  test_label[count]=i

  plt.imshow(im,cmap='Blues')
  plt.title('The Test Image')

for i in range(0,1):
  test_sample=test_data[i,:]
  actual_label=test_label[i]

  d=np.zeros((samp*5))

  for j in range(0,samp*5):
    d[j]=np.sum((test_sample-train_data[j,:])**2)

  val=d.min()
  ind=d.argmin()

plt.imshow(im,cmap='gray')
plt.pause(0.1)

if ind in np.arange(1,21):
  print('This picture belongs to Aishwarya Rai Bachchan')
if ind in np.arange(21,41):
  print('This picture belongs to Kajal Aggarwal')
if ind in np.arange(41,61):
  print('This picture belongs to Shriya Saran')
if ind in np.arange(61,81):
  print('This picture belongs to Rashmika Mandanna')
if ind in np.arange(81,101):
  print('This picture belongs to Tamanna Bhatia')

