import sys
import os
import cv2

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from source import generate_new_photo
from source import euclidean_distance

def test_generate_new_photo():
  image = cv2.imread("single_color.jpg")
  new_color = (229, 204, 255) # pink
  new_image = generate_new_photo(image, new_color)

  cv2.imwrite("out.jpg", new_image)

  test_image = cv2.imread("out.jpg")
  is_pink = True
  
  height, width, _ = test_image.shape

  for y in range(height):
    for x in range(width):
      b, g, r = test_image[y][x]
      curr = (b, g, r)

      threshold = 10

      # check that color it was changed to still is within threshold
      if curr != new_color and euclidean_distance(curr, new_color) > threshold:
        print("Failed at ", "y: ", y, "x: ", x)
        print("BGR : ", curr)
        is_pink = False
        break

  assert is_pink
