import cv2
import numpy as np

caminho_imagem = r"C:\Users\eryal\Pictures\red_ball.jpg"
imagem = cv2.imread(caminho_imagem)
imagem = cv2.resize(imagem, (640, 480))

hsv = cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV)

lower_red1 = np.array([0, 60, 50])
upper_red1 = np.array([10, 255, 255])
lower_red2 = np.array([170, 60, 50])
upper_red2 = np.array([180, 255, 255])

mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
mask = cv2.bitwise_or(mask1, mask2)

kernel = np.ones((5, 5), np.uint8)
mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

contornos, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

if contornos:
    maior_contorno = max(contornos, key=cv2.contourArea)
    (x, y), raio = cv2.minEnclosingCircle(maior_contorno)
    centro = (int(x), int(y))
    raio = int(raio)
    
    M = cv2.moments(maior_contorno)
    if M["m00"] != 0:
        cx = int(M["m10"] / M["m00"])
        cy = int(M["m01"] / M["m00"])
        cv2.circle(imagem, (cx, cy), 5, (255, 0, 0), -1)

cv2.imshow("Original com Contornos", imagem)
cv2.imshow("Máscara", mask)
cv2.waitKey(0)
cv2.destroyAllWindows()
