import cv2
import math
import uuid
import os
from minkowski_bouligand_dimension import MinkowskiBouligandDimension

if __name__ == "__main__":
    name = "eltri.png"
    img = cv2.imread("resources/%s" % (name))

    exponente = 2
    limite = 1200

    resultados = []
    minkowskiBouligandDimension = MinkowskiBouligandDimension(img)
    height, width, _ = img.shape
    
    u = uuid.uuid1()
    mDir = 'out/%s  %s' % (name[0: name.index(".")], u)
    os.mkdir(mDir)
    i = 1

    while(exponente < limite):
        imgTitle = '%s/%s %s.png' % (mDir, name[0: name.index(".")], i)
        boxesTouched, newImage = minkowskiBouligandDimension.getData(exponente, height, width)
        resultados.append((exponente, boxesTouched, "%s %s.png" % (name[0: name.index(".")], i)))
        cv2.imwrite(imgTitle, newImage)
        exponente *= 2
        i += 1
    
    try:
        f = open("%s/results.txt" % (mDir), "w+")
        g = open("%s/resultsToExcel.txt" % (mDir), "w+")
        
        for resultado in resultados:
            logn = math.log(resultado[1])
            logx = math.log(resultado[0])

            mText = """img: %s 
Boxes Touched: %s
Total boxes: %s
log(N): %s
log(x): %s

------------------------------

""" % (resultado[2], resultado[1], resultado[0], logn, logx)

            f.write(mText)
        
        g.write("N\tX\n")
        for resultado in resultados:
            logn = math.log(resultado[1])
            logx = math.log(resultado[0])
            mText = "%s\t%s\n" % (logn, logx)
            g.write(mText)
    finally:
        f.close()
        g.close()
        print("OK!")