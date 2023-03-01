import cv2
from PIL import Image

ascii_chars = [" ", ".", ",", "-", "~", "+", "=", "#", "@"]

def get_str_ascii(intent):
  return ascii_chars[int(intent / 29)]

def ascii_image(frame, scale):
  img = Image.fromarray(frame)

  width, height = img.size
  pixel = img.load()

  text = ""
  for y in range(height):
    for x in range(width):
      if y % (scale * 2) == 0 and x % scale == 0:
        r, g, b = pixel[x, y]
        intent = (r + g + b) / 3

        text = text + get_str_ascii(intent);

    if y % (scale * 2) == 0:
      text = text + "\n"
  print(text)

def ascii_video(path, scale):
  cap = cv2.VideoCapture(path)

  while cap.isOpened():
    ret, frame = cap.read()

    if ret:
      ascii_image(frame, scale)
    else:
      break

  # Libérer les ressources
  cap.release()
  cv2.destroyAllWindows()

ascii_video("assets/bad-apple.mp4", 4)