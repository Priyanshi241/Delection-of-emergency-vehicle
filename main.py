import cv2
#Load the image.

image = cv2.imread
("C:/Users/shiva/Downloads/firel.jpg")

# Convert the image to grayscale
gray = cv2.cvtColor (image, cv2.COLOR_BGR2GRAY)
# Apply Canny edge detection

canny = cv2.Canny (gray, 50, 200)
#Find contours in the image.

contours, = cv2.findContours (canny, cv2.RETR_EXTERNAL, CV2.CHAIN_APPROX_SIMPLE)

# Find the contour with the maximum area (which should be the ambulance)
max_contour = max (contours, key=cv2.contourArea)

# Get the bounding box of the contour
x, y, w, h = cv2.boundingRect (max_contour)

# Draw the bounding box on the original image
cv2.rectangle (image, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Display the result
cv2.imshow ("Bounding box", image)
cv2.waitkey (0)
cv2.destroyAllWindows ()
