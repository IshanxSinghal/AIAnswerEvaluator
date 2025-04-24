import cv2
import os
import numpy as np

def preprocess_image(img_path):
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    img = cv2.GaussianBlur(img, (5, 5), 0)
    img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                                cv2.THRESH_BINARY_INV, 11, 2)
    return img

def segment_answers(preprocessed_img, save_dir, base_name):
    contours, _ = cv2.findContours(preprocessed_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for i, cnt in enumerate(contours):
        x, y, w, h = cv2.boundingRect(cnt)
        if h > 30 and w > 50:  # filter small boxes
            roi = preprocessed_img[y:y+h, x:x+w]
            cv2.imwrite(os.path.join(save_dir, f"{base_name}_ans{i}.png"), roi)
