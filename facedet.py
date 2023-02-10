import cv2
import pygame
pygame.init()
if pygame.get_init() == False:
    print(f'Pygame error: {pygame.get_error}')
detector = cv2.CascadeClassifier("haar.xml")
video = cv2.VideoCapture(0)
frame = video.read()
windowWidth = video.get(cv2.CAP_PROP_FRAME_WIDTH)
windowHeight = video.get(cv2.CAP_PROP_FRAME_HEIGHT)
rectWidth = 50
rectHeight = 50
window = pygame.display.set_mode((windowWidth,windowHeight))
font = pygame.font.Font("font/terminal.ttf",12)
text = font.render("No face detected!",True,(0,255,0,255))
textRect = text.get_rect()
textRect.center = (windowWidth//4,windowHeight//4)
(_x,_y,_w,_h) = (0,0,0,0)
while(True):
    pygame.event.get()
    ret, frame = video.read()
    frame = cv2.flip(frame,1)
    gray = frame.copy()
    gray = cv2.cvtColor(gray,cv2.COLOR_BGR2GRAY)
    faces = detector.detectMultiScale(gray,scaleFactor=1.05,minNeighbors=5,minSize=(30,30),flags=cv2.CASCADE_SCALE_IMAGE)
    if len(faces) > 0:
        for (x,y,w,h) in faces:
            (_x,_y,_w,_h) = (x,y,w,h)
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
    else:
        cv2.putText(frame,"No faces detected!",(10,10),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(255,0,0),1)
        cv2.rectangle(frame,(_x,_y),(_x+_w,_y+_h),(0,255,0),2)
        window.blit(text,textRect)
    if _x < windowWidth // 3:
        playerX = windowWidth // 3
    elif _x > windowWidth * 2 // 3:
        playerX = windowWidth * 2 // 3
    else:
        playerX = _x
    pygame.draw.rect(window,(0,255,0),pygame.Rect(playerX,windowHeight//2,rectWidth,rectHeight))
    cv2.imshow("Video",frame)
    pygame.display.update()
    window.fill((0,0,0,255))
    if cv2.waitKey(1) == 27:
        break
video.release()
cv2.destroyAllWindows()
pygame.quit()