import cv2
vidcap = cv2.VideoCapture('TLR_22000_oct2_19Leftnight_Trim.mp4')
def getFrame(sec):
    vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
    hasFrames,image = vidcap.read()
    if hasFrames:
        #cv2.imwrite("./data/image"+str(count)+".jpg", image)     # save frame as JPG file
        name = "./data/frame"+str(count)+".jpg"
        print ('Creating...' + name)
        cv2.imwrite(name, image)
    return hasFrames
sec = 0
frameRate = 0.05 #//it will capture image in each 0.5 second
count=1
success = getFrame(sec)

try:
    if not os.path.exists('data'):
        os.makedirs('data')
except OSError:
    print ('Error: Creating directory of data')
    
while success:
    count = count + 1
    sec = sec + frameRate
    sec = round(sec, 2)
    success = getFrame(sec)