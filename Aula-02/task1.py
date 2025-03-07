import cv2
import numpy as np

# Carregar a imagem
caminho_imagem = r"C:\Users\eryal\Pictures\red_ball.jpg"
imagem = cv2.imread(caminho_imagem)
if imagem is None:
    print("Erro: Não foi possível carregar a imagem.")
    exit()

# Redimensionar para melhor visualização
imagem = cv2.resize(imagem, (640, 480))

# Converter para o espaço de cor HSV
hsv = cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV)

# Definir os limites de cor para detectar vermelho
lower_red1 = np.array([0, 55, 50])
upper_red1 = np.array([10, 255, 255])
lower_red2 = np.array([170, 55, 50])
upper_red2 = np.array([180, 255, 255])


# Criar máscaras para detectar tons de vermelho
mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
mask = cv2.bitwise_or(mask1, mask2)

# Encontrar contornos
contornos, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Desenhar os contornos na imagem original
cv2.drawContours(imagem, contornos, -1, (0, 255, 0), 2)

# Mostrar as imagens
cv2.imshow("Original com Contornos", imagem)
cv2.imshow("Máscara", mask)
cv2.waitKey(0)
cv2.destroyAllWindows()
