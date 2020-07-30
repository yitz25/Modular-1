import cv2
import math
import uuid
import os
from minkowski_bouligand_dimension import MinkowskiBouligandDimension

if __name__ == "__main__":
    img = cv2.imread("resources/mexico.png")

    exponente = 100
    vueltas = 5

    resultados = []
    minkowskiBouligandDimension = MinkowskiBouligandDimension(img)
    height, width, _ = img.shape
    
    u = uuid.uuid1()
    mDir = 'out/%s' % (u)
    os.mkdir(mDir)

    for i in range(vueltas):
        imgTitle = '%s/mexico%s.png' % (mDir, i + 1)
        boxesTouched, newImage = minkowskiBouligandDimension.getData(exponente, height, width)
        resultados.append((exponente**2, boxesTouched, "mexico%s.png" % (i + 1)))
        cv2.imwrite(imgTitle, newImage)
        exponente *= 2
    
    try:
        f = open("%s/results.txt" % (mDir), "w+")
        
        for resultado in resultados:
            logn = math.log(resultado[1])
            logx = math.log(resultado[0])

            mText = """img: %s 
Total boxes: %s
Boxes Touched: %s
log(N): %s
log(x): %s

------------------------------

""" % (resultado[2], resultado[0], resultado[1], logn, logx)

            f.write(mText)
    finally:
        f.close()
        print("finalizo")