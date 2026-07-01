import tkinter as tk
import math

branchAngle = 0.5
recursionGens = 0


def drawBranch(x,y,length,angle): #len is the length of the branch

    if length <= 2: return

    x_end = x + math.sin(angle) * length
    y_end = y - math.cos(angle) * length

    canvas.create_line(x, y,x_end, y_end,fill='green')
    new_length = length * 0.7
    new_angle_right = angle + branchAngle
    new_angle_left = angle - branchAngle
    drawBranch(x_end,y_end,new_length,new_angle_right)
    drawBranch(x_end,y_end,new_length,new_angle_left)

def slider_changed(event):
    global branchAngle
    branchAngle = slider.get() / 10
    canvas.delete("all")
    drawBranch(300,400 -20,100,0)
    
#setting up the canvas   
root = tk.Tk()
root.geometry('800x600')
root.title('Tree')
canvas = tk.Canvas(root, width=600, height=400, bg='white')
canvas.pack(anchor=tk.CENTER, expand=True)

slider = tk.Scale(
    root,
    from_=0,
    to=100,
    orient='horizontal',
    command=slider_changed
)
slider.pack()


drawBranch(300,400 -20,100,0)

root.mainloop()