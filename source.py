import cv2

mp = {}

image = cv2.imread('./res/one_color.jpg')
output = image.copy()

if image is not None:
  height, width, _ = image.shape
  for y in range(height):
    for x in range(width):
      # note: imread() returns in B G R order
      blue, green, red = image[y, x]
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

# naive O(n)
for y in range(height):
  for x in range(width):
    blue, green, red = image[y, x]
    curr = (blue,green,red)
    if curr == res:
      # TODO fix fill
      # could set a fill tolerance and need to calculate  
      # similarity of colors around
      output[y, x] = (229, 204, 255)

cv2.imwrite('./res/out.jpg', output)
cv2.destroyAllWindows()
