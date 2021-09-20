#Amal Omar 
#6/26/21 
#Project 4
import graphicsPlus as gr
 
 
def building_init(x, y, scale,screen_width,screen_height): #This function builds a building
    b_Height= 600*scale
    b_Width= 500*scale
    d_Height= 60*scale
    d_Width = 50*scale
    w_Height = 30*scale
    w_Width = 30*scale
    frame = gr.Rectangle(gr.Point(x,y), gr.Point(x + b_Width,y + b_Height))
    frame.setFill ('Brown')
    # This has P3 and P4
    window1 = gr.Rectangle(gr.Point(x + b_Width/6 - w_Width/2,y + b_Height - b_Height*0.8),gr.Point(x + b_Width/6 + w_Width/2,y + b_Height - b_Height*0.8 + w_Height))
    window1.setFill('black')
    # This has P5 and P6
    window2 = gr.Rectangle(gr.Point(x + 3*b_Width/6 - w_Width/2,y + b_Height - b_Height*0.8),gr.Point(x + 3*b_Width/6 + w_Width/2,y + b_Height - b_Height*0.8 + w_Height))
    window2.setFill('black')
    # This has P7 and P8
    window3 = gr.Rectangle(gr.Point(x + 5*b_Width/6 - w_Width/2,y + b_Height - b_Height*0.8),gr.Point(x + 5*b_Width/6 + w_Width/2,y + b_Height - b_Height*0.8 + w_Height))
    window3.setFill('black')
    # This has P9 and P10
    window4 = gr.Rectangle(gr.Point(x + b_Width/6 - w_Width/2,y + b_Height - b_Height*0.6),gr.Point(x + b_Width/6 + w_Width/2,y + b_Height - b_Height*0.6 + w_Height))
    window4.setFill('black')
    # This has P11 and P12
    window5 = gr.Rectangle(gr.Point(x + 3*b_Width/6 - w_Width/2,y + b_Height - b_Height*0.6),gr.Point(x + 3*b_Width/6 + w_Width/2,y + b_Height - b_Height*0.6 + w_Height))
    window5.setFill('black')
    # This has P13 and P14
    window6 = gr.Rectangle(gr.Point(x + 5*b_Width/6 - w_Width/2,y + b_Height - b_Height*0.6),gr.Point(x + 5*b_Width/6 + w_Width/2,y + b_Height - b_Height*0.6 + w_Height))
    window6.setFill('black')
    door = gr.Rectangle(gr.Point(x + b_Width/2-d_Width/2,y + b_Height-d_Height), gr.Point(x + b_Width/2+d_Width/2,y + b_Height))
    door.setFill('Gray') 
    grass = gr.Rectangle(gr.Point(0,y + b_Height), gr.Point(screen_width,screen_height))
    grass.setFill('green')
    return [grass,frame,window1,window2,window3,window4,window5,window6,door]
 
def sun_init(x,y,scale): #This function draws a sun on the right side of the screen
    radius = 5*scale
    sun = gr.Circle(gr.Point(x,y),radius)
    sun.setFill('yellow')
    return [sun]
 
def bench_init(x,y,scale, screen_height,screen_width): #This function draws a bench with two legs
    bench_w = 100*scale
    bench_h = 10*scale
    leg_h = 40*scale
    leg_w = 5*scale
    bench_frame1 = gr.Rectangle(gr.Point(x,y -25), gr.Point(x + bench_w, y + bench_h))
    bench_frame2 = gr.Rectangle(gr.Point(x,y + bench_h + 5), gr.Point(x +bench_w, y + (bench_h)*1.25 + 5))
    bench_leg1 = gr.Rectangle(gr.Point(x,y + (bench_h)*1.25 + 5) , gr.Point(x + leg_w, y + leg_h))
    bench_leg2 = gr.Rectangle(gr.Point(x + bench_w - leg_w,y + (bench_h)*1.25 + 5) , gr.Point(x + bench_w, y + leg_h))
    bench_frame1.setFill('blue')
    bench_frame2.setFill('blue')
    bench_leg1.setFill('blue')
    bench_leg2.setFill('blue')
    return [bench_frame1,bench_frame2, bench_leg1, bench_leg2]
 
def main():
    win = gr.GraphWin("My window", 1200, 1200)
    building = building_init(50,50, 1,1200,1200) # [frame,window1,window2,window3,window4,window5,window6,door]
    bench = bench_init(600,600,2,1200,1200) #[bench_frame1,bench_frame2, bench_leg1, bench_leg2]
    sun = sun_init(1050,80,10) #[sun]
    for element in building:
        element.draw(win)
    for element in bench:
        element.draw(win)
    for element in sun:
        element.draw(win)
    win.getMouse() 
    win.close()
 
    
if __name__ == "__main__":   
    main()
 