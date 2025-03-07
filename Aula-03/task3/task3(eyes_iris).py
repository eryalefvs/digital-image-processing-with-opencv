import cv2
import numpy as np

image = cv2.imread(r"C:\Users\eryal\Pictures\eyes.jpg")
image = cv2.resize(image, (630, 494))

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
edges = cv2.Canny(blurred, 30, 100)

circles = cv2.HoughCircles(blurred, cv2.HOUGH_GRADIENT, dp=1.2, minDist=20,
                           param1=50, param2=30, minRadius=10, maxRadius=50)

output = image.copy()
if circles is not None:
    circles = np.uint16(np.around(circles))
    for i in circles[0, :]:
        cv2.circle(output, (i[0], i[1]), i[2], (0, 255, 0), 1)

output_rgb = cv2.cvtColor(output, cv2.COLOR_BGR2RGB)

cv2.imshow("iris", output_rgb)
cv2.waitKey(0)
cv2.destroyAllWindows

cv2.imwrite("iris_rgb.jpg", output_rgb)