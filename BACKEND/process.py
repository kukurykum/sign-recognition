import cv2 as cv
import numpy as np
import os


def recognize(img):
    path = r'..\IMAGES'  # path do bazy znaków
    size = 80
    counter_result = []
    signs = []
    signs_names = []
    main_image = cv.imread(img)

    try:
        for image_path in os.listdir(path):
            input_path = os.path.join(path, image_path)
            image = cv.imread(input_path)

            signs.append(input_path)  # tworzymy listę znaków z bazy
            image_path = image_path.replace("-", " ")
            signs_names.append(image_path.rstrip(".png"))

            counter = 0

            for x in range(0, size):
                for y in range(0, size):
                    red = image[x, y, 2]
                    red1 = main_image[x, y, 2]
                    green = image[x, y, 1]
                    green1 = main_image[x, y, 1]
                    blue = image[x, y, 0]
                    blue1 = main_image[x, y, 0]
                    temp = (int(red) + int(green) + int(blue)) - (int(red1) + int(green1) + int(blue1))
                    if temp != 0:
                        counter += 1
            counter_result.append(int(counter))

        min_index = np.argmin(counter_result)
        final_path = signs[min_index]
        if counter_result[min_index] == 0:
            compatibility = 100
        else:
            compatibility = 100 - (counter_result[min_index] / (size * size) * 100)

        print("sciezka z bazy: " + final_path)
        print("nazwa znaku: " + signs_names[min_index])
        print("zgodnosc: " + str(compatibility) + "% \n")

        final_result = [signs_names[min_index], final_path, compatibility]
        return final_result
    except:
        return False

