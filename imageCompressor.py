from PIL import Image
import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

SRC = os.path.join(ROOT_DIR, "src")

def changeAspect(size, rate):

    x = (size[0]/rate)
    y = (size[1]/rate)
    return (int(x), int(y))

def compress(path, rate=60):
    baseDir = os.path.dirname(path)
    fileName = os.path.basename(path).split(".")[0]
    extension = os.path.basename(path).split(".")[1]

    img = Image.open(path)
    size = changeAspect(img.size, 4)
    
    img = img.resize(size,Image.LANCZOS)

    compressDir = baseDir.replace("\\src","\\Compressed")
    os.makedirs(compressDir, exist_ok=True)
    
    img.save(os.path.join(compressDir, f"{fileName}_COM.{extension}"), optimize=True, quality=rate)
    return (fileName)

def main():
    files = os.listdir(SRC)
    filesLen = len(files)
    for file,i in zip(files, range(filesLen)):
        filePath = os.path.join(SRC, file)
        print(f"{i+1}/{filesLen} Saved: {compress(filePath, 95)}")
    input("Done...")

if __name__ == "__main__":
    main()