#Okoye-Nobert Chukwuebuka

from aluLib import *

window_width = 1000
window_height = 500

# Note that functions are expected to be lowercase, so don't be tempted to capitalize

def congo_brazaville():
    #Your code for the Congo brazaville flag goes here

    disable_stroke()  #this function removed the strokes from the triangles drawn
    set_fill_color(1, 1, 0) #this sets the default color of the rectangle to yellow
    draw_rectangle(0,0,window_width,window_width)

    set_fill_color(0, 1, 0) #this sets the top left triangle green
    draw_triangle(0,0,500,0,0,500)

    set_fill_color(1, 0, 0)  #this sets the top left triangle red
    draw_triangle(1000,0,1000,1000,500,500)


start_graphics(congo_brazaville, width=window_width, height=window_height)


def niger():
    # Your code for the Niger flag goes here
    disable_stroke() #this function removed the strokes from the triangles drawn
    set_fill_color(1, 0.5, 0) #this sets the default color of the rectangle to orange
    draw_rectangle(0,0,window_width,window_height/3)


    set_fill_color(0, 0.8, 0) #this sets the default color of the rectangle to green
    draw_rectangle(0,334,window_width,window_height/3)

    set_fill_color(1, 0.5, 0) #this sets the default color of the rectangle to orange
    draw_circle(500,250,80)
start_graphics(niger, width=window_width, height=window_height)



def guinea():
    # Your code for the Guinea flag goes here
    disable_stroke()  #this function removed the strokes from the rectangles drawn
    set_fill_color(1, 1, 0) #this sets the default color of the rectangle to yellow
    draw_rectangle(0,0,window_width,window_height)

    set_fill_color(1, 0, 0) #this sets the default color of the rectangle to red
    draw_rectangle(0,0,window_width/3,window_height)

    set_fill_color(0, 1, 0) #this sets the default color of the rectangle to green
    draw_rectangle(668,0,window_width/3,window_height)




start_graphics(guinea, width=window_width, height=window_height)