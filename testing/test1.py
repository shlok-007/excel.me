import cv2
max_img_dim=150

imgName= "meme1.jpeg"
img= cv2.imread(imgName , cv2.IMREAD_UNCHANGED)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
