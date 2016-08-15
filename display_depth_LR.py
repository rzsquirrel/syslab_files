from pickle import load

fin=open('pts1.pkl','rb')
pts1=load(fin)
fin.close()

fin2=open('pts2.pkl','rb')
pts2=load(fin2)
fin2.close()

from matplotlib import pyplot as plt
plt.subplot(121),plt.imshow(pts1)
plt.subplot(122),plt.imshow(pts2)
