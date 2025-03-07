import cv2
import numpy as np

image = cv2.imread(r"C:\Users\eryal\Pictures\lanes.jpg")
image = cv2.resize(image, (550, 300))
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

edges = cv2.Canny(gray, 40, 50)

lines = cv2.HoughLinesP(edges, rho=1, theta=np.pi/180, threshold=50, minLineLength=50, maxLineGap=10)

if lines is not None:
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(image, (x1, y1), (x2, y2), (0, 255, 0), 2)

cv2.imshow("Linhas Detectadas", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("Linhas_Detectadas.jpg", image)