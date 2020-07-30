import cv2
import copy
import numpy as np

class MinkowskiBouligandDimension:

    def __init__(self, img):
        self.img = copy.deepcopy(img)

    def test(self):
        print("OK")

    def isDiferent(self, crop_img):
        auxPix = np.array([255, 255, 255])

        for pixels in crop_img:
            for pixel in pixels:
                if((pixel != auxPix).all()):
                    return True
        return False


    def getData(self, exponente, height, width):
        img = copy.deepcopy(self.img)
        floatlWidth = width / exponente
        integerWidth = integerlHeight = int(floatlWidth)

        auxWidth = integerWidth
        auxHeight = integerlHeight

        posX = 0
        posY = 0

        boxesTouched = 0

        while((posY + auxHeight) <= height):
            posX = 0
            while((posX + auxWidth) <= width):
                crop_img = self.img[posY:posY + auxHeight, posX:posX + auxWidth]

                if(self.isDiferent(crop_img)):
                    boxesTouched += 1
                    cv2.rectangle(img, (posX, posY), (posX + auxWidth, posY + auxHeight), (0, 0, 0), thickness = -1)
                else:
                    cv2.rectangle(img, (posX, posY), (posX + auxWidth, posY + auxHeight), (0, 0, 0), thickness = 1)

                posX += auxWidth
            posY += auxHeight

        cv2.putText(img, "Total Squares: %s" % (exponente**2), (20, height - 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2, cv2.LINE_AA)
        cv2.putText(img, "Squares Touched: %s" % (boxesTouched), (20, height - 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2, cv2.LINE_AA)

        return boxesTouched, img


    def paintGrid(self, exponente, height, width):
        img = copy.deepcopy(self.img)
        floatlWidth = width / exponente
        integerWidth = integerlHeight = int(floatlWidth)

        auxWidth = integerWidth
        auxHeight = integerlHeight

        posX = 0
        posY = 0

        while((posY + auxHeight) <= height):
            posX = 0
            while((posX + auxWidth) <= width):
                cv2.rectangle(img, (posX, posY), (posX + auxWidth, posY + auxHeight), (0, 0, 0), thickness = 1)
                posX += auxWidth
            posY += auxHeight

        return img

    def getImg(self):
        return self.img
