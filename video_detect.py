import cv2
cap = cv2.VideoCapture('C:\Users\ACER\Dropbox\My PC (LAPTOP-81TS7IIL)\Desktop\human_count\in.avi')

human_cascade = cv2.CascadeClassifier('C:\Users\ACER\Dropbox\My PC (LAPTOP-81TS7IIL)\Desktop\human_count\haarcascade_fullbody.xml')

def detect(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    bounding_box_cordinates =  human_cascade.detectMultiScale(gray, 1.9, 1)
    
    person = 1
    for x,y,w,h in bounding_box_cordinates:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)
        cv2.putText(frame, f'person {person}', (x,y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), 1)
        person += 1
    
    cv2.putText(frame, 'Status : Detecting ', (40,40), cv2.FONT_HERSHEY_DUPLEX, 0.8, (255,0,0), 2)
    cv2.putText(frame, f'Total Persons : {person-1}', (40,70), cv2.FONT_HERSHEY_DUPLEX, 0.8, (255,0,0), 2)
    cv2.imshow('output', frame)
    return frame
while(True):
    
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    # Our operations on the frame come here
    frame = detect(frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()