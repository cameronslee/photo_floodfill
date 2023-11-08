import cv2
import sys
from pathlib import Path

mp = {}

def dfs(visited, out, x, y, new_color, target_color):
  if x < 0 or y < 0 or x >= len(visited[0]) or y >= len(visited):
    return
  blue, green, red = out[y][x]
  curr = (blue,green,red)
  if (visited[y][x] == 1 or curr != target_color):
    return
  
  visited[y][x] = 1
  out[y][x] = new_color

  return dfs(visited, out, x+1, y, new_color, target_color)
  return dfs(visited, out, x-1, y, new_color, target_color)
  return dfs(visited, out, x, y+1, new_color, target_color)
  return dfs(visited, out, x, y-1, new_color, target_color)

def main():
  n = len(sys.argv)
  if n != 2: 
    sys.exit("usage: python source.py <filename>")
  
  img = Path(sys.argv[1])
  if not img.exists():
    sys.exit("error: invalid filename")

  image = cv2.imread(sys.argv[1])
  out = image  
  if image is not None:
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
  else:
    print("Failed to load the image.")

  highest = 0
  res = (0,0,0)
  for key, val in mp.items():
    if val > highest:
      highest = val
      res = key

  print("Most prominent color") 
  print(res)

  for y in range(height):
    for x in range(width):
      blue, green, red = image[y, x]
      curr = (blue,green,red)
      if curr == res:
        new_color = (229, 204, 255) #new_color set to pink for now
        dfs(visited, output, x, y, new_color, res)

  cv2.imwrite(('./res/output/out.jpg'), output)
  cv2.destroyAllWindows()

if __name__ == "__main__":
  main()
