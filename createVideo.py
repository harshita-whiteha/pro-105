import os
import cv2

path = "img/"
list = []

for i in os.listdir(path):
    name,ext = os.path.splitext(i)

    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        file_name = path+"/"+ i

       # print(file_name)
               
        list.append(file_name)
        
print(len(list))
count = len(list)

frame = cv2.imread(list[0])
height,width,layers = frame.shape
size = (width,height)
#print(size)

out = cv2.VideoWriter("project.avi",cv2.VideoWriter_fourcc(*"DIVX"),0.8,size)

for i in range(0,count-1):

    frame = cv2.imread(list[i])
    out.write(frame)

    cv2.imshow("its bp",frame)
    if cv2.waitKey(1) == 32:
        break
out.release()
print("DONE")