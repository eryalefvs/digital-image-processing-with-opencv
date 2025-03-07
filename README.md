# Processamento Digital de Imagens - 6º Período

Este repositório contém os códigos desenvolvidos durante a disciplina de férias Processamento Digital de Imagens, cursada no 6º período de Engenharia da Computação. Cada pasta representa uma aula com experimentos práticos sobre técnicas de manipulação e análise de imagens.

## Conteúdo das Aulas

### Aula 02 - Detecção de Objetos por Cor

Nesta aula, foi explorado o conceito de segmentação por cor utilizando o modelo de cores HSV. O objetivo foi identificar objetos vermelhos dentro de uma imagem.

Técnicas utilizadas:

- Conversão de imagens para o espaço de cores HSV.

- Criação de máscaras para segmentação de cor.

- Uso de contornos para identificar objetos e desenhar sua borda.


Imagem base utilizada:
<img src="/Aula-02/red_ball.jpg">

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

### Aula 04 - Filtragem e Realce de Detalhes

Esta aula focou no realce de bordas e remoção de ruídos em imagens.

Técnicas utilizadas:

- Aplicação de filtros de suavização (Média, Mediana, Gaussiano).

- Realce de bordas usando operadores de convolução.

- Uso de morfologia matemática para refinar segmentação.

## Conclusão

Os experimentos realizados permitem compreender técnicas fundamentais de processamento de imagens, como segmentação, detecção de bordas e filtragem. O conhecimento adquirido pode ser aplicado em sistemas de visão computacional, reconhecimento de padrões e automação de análise visual.
