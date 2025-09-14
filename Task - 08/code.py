import os
from PIL import Image

folder = "/home/tulasi-lasya/myopencvproj/Treasure-Map/assets"  # this my assets folder path
files = sorted(os.listdir(folder)) # here it sorts the files from the folder

image_size = 128 # the image size is 128 * 128
cols = 16 
rows = (len(files) // cols)  # the length of files are 64 (bcz removed the blank images)

canvas = Image.new("RGB", (cols*image_size, rows*image_size)) # it creates a new blank image , so that we can paste the images we want in that particular image size. 
# (cols*image_size, rows*image_size) indicates that the width and height of the new blank image  

for index, file in enumerate(files):
     # enumerate(files) is used to make easier to loop through a list while keeping track of the index of each item from the files list.
    img = Image.open(os.path.join(folder, file)) # joins the folder path and file name to open it.
    row = index // cols
    col = index % cols
    canvas.paste(img, (col*image_size, row*image_size)) # we multiply col*image_size and row*image_size to get the coordinates of the image 
    # it is pasted in order according to files order in assets folder.

canvas.save("merged_map.png")
print("Done") # to confirm that it was saved 
