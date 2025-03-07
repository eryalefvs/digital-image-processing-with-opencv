# 📷 Processamento Digital de Imagens - 6º Período

Este repositório contém os códigos desenvolvidos durante a disciplina de férias Processamento Digital de Imagens, cursada no 6º período de Engenharia da Computação. Cada pasta representa uma aula com experimentos práticos sobre técnicas de manipulação e análise de imagens.

## Conteúdo das Aulas

### Aula 02 - Detecção de Objetos por Cor

Nesta aula, foi explorado o conceito de segmentação por cor utilizando o modelo de cores HSV. O objetivo foi identificar objetos vermelhos dentro de uma imagem.

Técnicas utilizadas:

- Conversão de imagens para o espaço de cores HSV.

- Criação de máscaras para segmentação de cor.

- Uso de contornos para identificar objetos e desenhar sua borda.

Exemplo:

![Imagem base utilizada](/Aula-02/red_ball.jpg)

Código:
```python
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
```

Imagem com contornos e máscara da imagem:

<img src="/Aula-02/Máscara.jpg">
<img src="/Aula-02/Original_com_Contornos.jpg">


### Aula 03 - Detecção de Formas e Estruturas

Esta aula expandiu o conceito de segmentação com a detecção de formas específicas, como esferas e contornos de olhos.

Técnicas utilizadas:

- Detecção de círculos usando a transformada de Hough.

- Processamento de bordas com filtros Gaussianos e Canny.

- Uso de momentos para encontrar o centro de massa de objetos.

Imagem base:

<img src="/Aula-03/task3/eyes.jpg">

Código para detecção da íris do olho:
```python
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
```
Resultado:

<img src="/Aula-03/task3/iris_rgb.jpg">

Código para detecção de pupila:
```python
import cv2
import numpy as np

image = cv2.imread(r"C:\Users\eryal\Pictures\eyes.jpg")
image = cv2.resize(image, (630, 494))

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
edges = cv2.Canny(blurred, 30, 100)

circles = cv2.HoughCircles(blurred, cv2.HOUGH_GRADIENT, dp=1.1, minDist=20,
                           param1=52, param2=33, minRadius=13, maxRadius=50)

output = image.copy()
if circles is not None:
    circles = np.uint16(np.around(circles))
    for i in circles[0, :]:
        cv2.circle(output, (i[0], i[1]), i[2], (0, 255, 0), 1)

output_rgb = cv2.cvtColor(output, cv2.COLOR_BGR2RGB)

cv2.imshow("pupil", output_rgb)
cv2.waitKey(0)
cv2.destroyAllWindows

cv2.imwrite("pupil_rgb.jpg", output_rgb)
```
Resultado:

<img src="/Aula-03/task3/pupil_rgb.jpg">

### Aula 04 - Filtragem e Realce de Detalhes

Esta aula focou no realce de bordas e remoção de ruídos em imagens.

Técnicas utilizadas:

- Aplicação de filtros de suavização (Média, Mediana, Gaussiano).

- Realce de bordas usando operadores de convolução.

- Uso de morfologia matemática para refinar segmentação.

No exemplo, detectamos objetos em uma imagem a partir de outra imagem:

<img src="/Aula-04/mario.jpg">
<img src="/Aula-04/coin.jpg">

Código:
```python
import cv2
import numpy as np

mario_img = cv2.imread(r"C:\Users\eryal\Pictures\mario.jpg")
mario_copy = mario_img.copy()
mario_copy = cv2.cvtColor(mario_copy, cv2.COLOR_BGR2GRAY)

coin_img = cv2.imread(r"C:\Users\eryal\Pictures\coin.jpg", 0)
w, h = coin_img.shape[::-1]
print(w, h)

result = cv2.matchTemplate(mario_copy, coin_img, cv2.TM_CCOEFF_NORMED)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
threshold = 0.7
img_intermediario = np.where(result >= threshold)

for coordinate in zip(*img_intermediario[::-1]):
    x, y = coordinate
    cv2.rectangle(mario_img, (x, y), (x + w, y + h), (0, 255, 0), 1)

cv2.imshow("Detected Coins", mario_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("Detected_Coins.jpg", mario_img)
```
Resultado:

<img src="/Aula-04/Detected_Coins.jpg">

## Conclusão

Os experimentos realizados permitem compreender técnicas fundamentais de processamento de imagens, como segmentação, detecção de bordas e filtragem. O conhecimento adquirido pode ser aplicado em sistemas de visão computacional, reconhecimento de padrões e automação de análise visual.
