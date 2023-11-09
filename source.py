import cv2
import sys
from pathlib import Path
import math

mp = {}

def euclidean_distance(color1, color2):
  b1, g1, r1 = color1
  b2, g2, r2 = color2
  return math.sqrt((r1-r2)**2 + (g1-g2)**2 + (b1-b2)**2)

def are_close(color1, color2, threshold):
  d = euclidean_distance(color1, color2)
  return d <= threshold

def dfs(visited, out, x, y, new_color, target_color):
  if x < 0 or y < 0 or x >= len(visited[0]) or y >= len(visited):
    return
  blue, green, red = out[y][x]
  curr = (blue,green,red)
  if (visited[y][x] == 1 or not are_close(target_color, curr, 10)):
    return
  
  visited[y][x] = 1
  out[y][x] = new_color

  return dfs(visited, out, x+1, y, new_color, target_color)
  return dfs(visited, out, x-1, y, new_color, target_color)
  return dfs(visited, out, x, y+1, new_color, target_color)
  return dfs(visited, out, x, y-1, new_color, target_color)

def generate_new_photo(image, new_color):
  output = image.copy()
  height, width, _ = image.shape
  visited = [[ 0 for x in range(0,width)] for y in range(0,height)]
  for y in range(height):
    for x in range(width):
      # note: imread() returns in B G R order
      blue, green, red = image[y][x]
      curr = (blue,green,red)
      if curr not in mp:
        mp[curr] = 1
      else:
        mp[curr] += 1

  highest = 0
  res = (0,0,0)
  for key, val in mp.items():
    if val > highest:
      highest = val
      res = key

  print("Most prominent color found: BGR", res) 

  for y in range(height):
    for x in range(width):
      blue, green, red = image[y, x]
      curr = (blue,green,red)
      if curr == res:
        dfs(visited, output, x, y, new_color, res)

  return output

### Driver ###
def main():
  n = len(sys.argv)
  if n != 2: 
    sys.exit("usage: python source.py <filename>")
  
  help_msg = "usage: python source.py <filename>\n\nOptions:\n-foo"
  if sys.argv[1] in {"-help", "-h", "--h", "--help"}:
    sys.exit(help_msg)

  img = Path(sys.argv[1])
  if not img.exists():
    sys.exit("error: invalid filename")

  if not img.exists():
    sys.exit("error: invalid filename")

  image = cv2.imread(sys.argv[1])
  if image is not None:
    new_color = (229, 204, 255) #pink 
    new_photo = generate_new_photo(image, new_color)
  else:
    sys.exit("Failed to load the image.")

  cv2.imwrite(('./res/output/out.jpg'), new_photo)
  cv2.destroyAllWindows()

if __name__ == "__main__":
  main()
