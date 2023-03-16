import os
from PIL import Image
import uuid


img_dir = r"C:\Users\Cliff\Pictures"

jpg_images = os.listdir(img_dir)

for img in jpg_images:
    image = Image.open(os.path.join(img_dir, img))
    new_extension = 'png'
    new_filename = str(uuid.uuid4().hex)[:16]
    new_filename_full = ".".join([new_filename, new_extension])
    image.save(os.path.join(img_dir, new_filename_full))
