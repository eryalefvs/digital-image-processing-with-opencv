import cv2
import numpy as np

caminho_imagem = r"C:\Users\eryal\Pictures\red_ball.jpg"
imagem = cv2.imread(caminho_imagem)
if imagem is None:
    print("Erro: Não foi possível carregar a imagem.")
    exit()

imagem = cv2.resize(imagem, (640, 480))

hsv = cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV)

lower_red1 = np.array([0, 55, 50])
upper_red1 = np.array([10, 255, 255])
lower_red2 = np.array([170, 55, 50])
upper_red2 = np.array([180, 255, 255])

mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
mask = cv2.bitwise_or(mask1, mask2)

contornos, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(imagem, contornos, -1, (0, 255, 0), 2)

cv2.imshow("Original com Contornos", imagem)
cv2.imshow("Máscara", mask)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("Original_com_Contornos.jpg", imagem)
cv2.imwrite("Máscara.jpg", mask)