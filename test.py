
try:
    f = open("test.txt", "w+")
    for i in range(10):
        f.write("This is asd %d\r\n" % (i+1))
finally:
    f.close()