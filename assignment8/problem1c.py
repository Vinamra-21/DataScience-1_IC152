from matplotlib import pyplot as plt
plt.rcParams.update({'font.size': 22})


# install pillow using:
# pip3 install pillow
# if above does not work and you are on windows, try:-
# py -m pip3 install pillow

# importing Image and ImageOps from PIL
from PIL import Image, ImageOps

# creating image object:
imInp = Image.open('problem1cInput.jpg')

# converting imInp to grayscale:
imGrayscale = ImageOps.grayscale(imInp)

# converting image to numpy array
import numpy as np
pixels2D = np.array(imGrayscale)
print(pixels2D.shape)

# showing/saving image
# imGrayscale.show()
# imGrayscale.save('problem1cOutput.jpg')
# Write code for finding histogram here:
plt.hist(pixels2D.flatten(),bins=500) #plotting histogram 1
plt.title('Problem1c_i Pixel Values')
plt.xlabel('Greyscale Values')
plt.ylabel('pixel count')
plt.tight_layout()
#show and save plot
plt.savefig('problem1ci.png')
# plt.show()
plt.clf()
# Write code for finding histogram of difference of pixel's intensity
# with its left neighbour here:
lst_ii = []
for j in range(np.shape(pixels2D)[0]):
    for i in range(1,np.shape(pixels2D)[1]):
        lst_ii += [int(pixels2D[j,i])-int(pixels2D[j,i-1])]       
plt.hist(lst_ii,bins=250,rwidth=.5) #plotting histogram 2    
plt.title("Problem1c_ii Difference of pixel's intensity",fontsize='16')
plt.tight_layout()
plt.xlabel('Pixel Difference Value')
plt.ylabel('Count')
#show and save plot
plt.savefig('problem1cii.png')
# plt.show()



