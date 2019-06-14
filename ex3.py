import cv2

image = cv2.imread("Image/lunar.jpg",cv2.IMREAD_GRAYSCALE)

cv2.imshow("Moon",image)



cv2.waitKey(0)

cv2.destroyAllWindows()


height,width = image.shape

print(height,width)