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