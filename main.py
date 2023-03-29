import cv2

# Read the input image
img = cv2.imread('minion.jpg')
# Convert the input image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Apply bilateral filter
bilateral = cv2.bilateralFilter (gray, 15, 20, 20)
# Apply median blur to the grayscale image
gray = cv2.medianBlur(gray, 5)
# Apply adaptive thresholding to the blurred image
thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
# Convert the thresholded image to color
thresh = cv2.cvtColor(thresh, cv2.COLOR_GRAY2BGR)
# Apply bilateral filter to the input image
color = cv2.bilateralFilter(img, 9, 250, 250)
# Combine the color image and the thresholded image
cartoon = cv2.bitwise_and(color, thresh)
# Display the output image
cv2.imshow('Cartoonized Image', cartoon)
cv2.waitKey(0)
cv2.destroyAllWindows()

