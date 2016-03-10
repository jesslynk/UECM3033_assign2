import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import scipy.linalg as sp

img=mpimg.imread('neko.jpg')
[r,g,b] = [img[:,:,i] for i in range(3)]

#to find U, Sigma and V for the red,green and blue matrix
Ured,Sred,Vred = sp.svd(r,False,True,False,True)
Sred = np.diag(Sred)

Ugreen,Sgreen,Vgreen = sp.svd(g,False,True,False,True)
Sgreen = np.diag(Sgreen)

Ublue,Sblue,Vblue = sp.svd(b,False,True,False,True)
Sblue = np.diag(Sblue)


#to find the none zero elements in sigma of each red, green and blue matrices
print("The number of non zero elements in Sigma are", len(Sred),"," ,len(Ured),"and" ,len(Vred), "respectively.")

#lower the resolution picture to 30
Sred_new = np.zeros_like(Sred)
Sred_new[0:30] = Sred[0:30]
rnew = Ured@Sred_new@Vred

Sgreen_new = np.zeros_like(Sgreen)
Sgreen_new[0:30] = Sgreen[0:30]
gnew = Ugreen.dot(Sgreen_new).dot(Vgreen)

Sblue_new = np.zeros_like(Sblue)
Sblue_new[0:30] = Sblue[0:30]
bnew = Ublue.dot(Sblue_new).dot(Vblue)

img[:,:,0] = rnew
img[:,:,1] = gnew
img[:,:,2] = bnew

#to plot the images
fig = plt.figure(1)
ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,3)
ax4 = fig.add_subplot(2,2,4)
ax1.imshow(img)
ax2.imshow(rnew, cmap = 'Reds')
ax3.imshow(gnew, cmap = 'Greens')
ax4.imshow(bnew, cmap = 'Blues')

plt.show()
plt.savefig('images_low')


#lower the resolution picture to 200
Sred_new = np.zeros_like(Sred)
Sred_new[0:200] = Sred[0:200]
rnew = Ured@Sred_new@Vred

Sgreen_new = np.zeros_like(Sgreen)
Sgreen_new[0:200] = Sgreen[0:200]
gnew = Ugreen.dot(Sgreen_new).dot(Vgreen)

Sblue_new = np.zeros_like(Sblue)
Sblue_new[0:200] = Sblue[0:200]
bnew = Ublue.dot(Sblue_new).dot(Vblue)

img[:,:,0] = rnew
img[:,:,1] = gnew
img[:,:,2] = bnew

#to plot the images
fig = plt.figure(2)
ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,3)
ax4 = fig.add_subplot(2,2,4)
ax1.imshow(img2)
ax2.imshow(rnew, cmap = 'Reds')
ax3.imshow(gnew, cmap = 'Greens')
ax4.imshow(bnew, cmap = 'Blues')

plt.show()
plt.savefig('images_high')




