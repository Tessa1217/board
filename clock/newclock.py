import numpy as np
import cv2

def makeR(angle):
    radian=np.deg2rad(angle)
    R=np.array([[np.cos(radian), -np.sin(radian), 0],
    [np.sin(radian), np.cos(radian), 0],
    [0, 0, 1]])
    return(R)

def makeT(a,b):
    T=np.eye((3))
    T[0,2]=a
    T[1,2]=b
    return(T)

def draw(canvas, q, color):
    cv2.line(canvas,(q[0,0],q[1,0]),(q[0,1],q[1,1]),color)
    cv2.line(canvas,(q[0,1],q[1,1]),(q[0,2],q[1,2]),color)
    cv2.line(canvas,(q[0,2],q[1,2]),(q[0,3],q[1,3]),color)
    cv2.line(canvas,(q[0,3],q[1,3]),(q[0,0],q[1,0]),color)

def clock(canvas, color):
    r=200
    xcen, ycen=400,400
    clock=cv2.circle(canvas, (xcen, ycen), r, color, 4)
    center=cv2.circle(canvas, (xcen, ycen), 4, color, -1)
    degree=0
    num=0
    while degree<360:
        p=np.array([[0,0,1],[12,0,1]]).T
        q=np.array([[0,0,1],[20,0,1]]).T
        h=makeT(xcen,ycen)@makeR(-90)@makeR(degree)@makeT(r-12,0)
        h2=makeT(xcen,ycen)@makeR(-90)@makeR(degree)@makeT(r-20,0)
        p2=h@p
        p2=p2.astype('int')
        q2=h2@q
        q2=q2.astype('int')
        if num%5==0:
            cv2.line(canvas,(q2[0,0],q2[1,0]),(q2[0,1],q2[1,1]),color,2)
        else:
            cv2.line(canvas,(p2[0,0],p2[1,0]),(p2[0,1],p2[1,1]),color)
        degree=degree+6
        num=num+1

def niddle(canvas,angle,color,length):
    p=np.array([[0,0,1],[length,0,1]]).T
    h=makeT(400,400)@makeR(-90)@makeR(angle)
    q=h@p
    q=q.astype('int')
    cv2.line(canvas,(q[0,0],q[1,0]),(q[0,1],q[1,1]),color,3)

def main():
    canvas=np.zeros((1600, 1000, 3), dtype='uint8')
    degho=0
    degmi=0
    while True:
        if degmi%360==0:
            color=(np.random.randint(0,255),np.random.randint(0,255),np.random.randint(0,255))
        canvas[:,:,:]=(0,0,0)
        degho=degho+0.25
        degmi=degmi+3
        clock(canvas,color)
        niddle(canvas,degho,color,80)
        niddle(canvas,degmi,color,130)
        cv2.imshow('window', canvas)
        cv2.waitKey(100)


if __name__=='__main__':
    main()