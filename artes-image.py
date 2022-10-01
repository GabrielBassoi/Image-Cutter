from PIL import Image

imageName = input("Image name: ")
img = Image.open(imageName)

n1, n2, n3, n4 = 0, 0, 512, 512

for n in range(3):
    print(f"Loading image {n}")
    img.crop((n1, n2, n3, n4)).save(f"in/{n}.png")
    n1 += 10
    n3 += 10

print("Finish!!!")
