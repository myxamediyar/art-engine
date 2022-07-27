from PIL import Image

mainPath = "./collection/"
collectionSize = 400

def resize():
    base = Image.new('RGB', (825, 825))
    for i in range(1, collectionSize + 1):
        img = Image.open(mainPath + str(i) + ".png").convert('RGB')
        base.paste(img,(0, 0))
        newbase = base.resize((400, 400), Image.ANTIALIAS)
        newbase.save(f'./resized/{i}.jpeg', format='jpeg')
        print("Resized object " + str(i))
resize()

