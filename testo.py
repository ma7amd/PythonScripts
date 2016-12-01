import webbrowser
import time 
import os
import re
import turtle
import urllib.request
import sys
import socket


"""
total_breaks = 3
break_count = 0

print("This program started on " + time.ctime())
while(break_count < total_breaks):
    time.sleep(7200) 
    webbrowser.open("https://www.youtube.com/watch?v=_myucRTDI2w")
    break_count += 1
####################################################################################

def rename_files():
    #get file names  from a folder 
    files_names = os.listdir(r'E:\Finished From Chrome\prank\prank') #listdir() changeing the dir to the above level dir
    saved_path = os.getcwd()
    print('Current Working directory is ' + saved_path)
    os.chdir(r'E:\Finished From Chrome\prank\prank') #you must change dir to return to the dir that contain files

    #for each file, rename filename
    for file_name in files_names:
        print('Old Name - ' + file_name)
        print('New Name - ' + re.sub('[0-9]',"", file_name))
        #os.rename(file_name, file_name.translate('0123456789'))
        os.rename(file_name, re.sub('[0-9]',"", file_name))
    os.chdir(saved_path)

rename_files()
################################################################################################




def square_movements(some_turtle):
    for i in range(1,5):
        some_turtle.forward(200)
        some_turtle.right(90)
        
def triangle_moves(some_turtle):
    for step in range(1, 4):
        some_turtle.forward(200)
        some_turtle.right(120)

def turtle_shapes():
    
    window = turtle.Screen()
    window.bgcolor('black')
    
   
#create the titi turtle - draws a square
    titi = turtle.Turtle()
    titi.shape("turtle")
    titi.color('yellow')
    titi.speed(4)
    for i in range(1, 37):
        square_movements(titi)
        titi.right(10)
    
#create the lily turtle - draws a circle    
    lily = turtle.Turtle()
    lily.shape('arrow')
    lily.color('red')
    lily.circle(200)

    
#create the jody turtle - draws a triangle
    jody = turtle.Turtle()
    jody.shape("turtle")
    jody.color('white')
    for x in range(1, 11):
        triangle_moves(jody)
        jody.forward(10)
       
    window.exitonclick()

turtle_shapes()
#####################################################

import turtle
#Haha TTpro
def draw_triangle(the_turtle,length,ori,recursion):
    recursion=recursion+1
    meow= the_turtle

    for i in range(0,3):
        if(recursion<4):
        #if (0):
            meow.forward(length/2)
            meow.left(120)
            draw_triangle(meow,length/2,0,recursion)
            meow.right(120)
            meow.forward(length/2)
        else:
            meow.forward(length)
        if (ori==1):
            meow.left(120)
        else:
            meow.right(120)

meow = turtle.Turtle() # init
meow.speed(10) # speed = 1 to slow turtle down
meow.color("white","green") # set color5
meow.shape("turtle") # set shape to a turtle
background = turtle.Screen()  # create background
background.bgcolor("black")     # set background color to red


draw_triangle(meow,200,1,0)

#meow.forward(100)
#meow.left(120)
#draw_triangle(meow,100,0,0)
#meow.right(120)

background.exitonclick()      # click anywhere to close background

######################################################################################


#flower by Turtle

import turtle
import math

def p_line(t, n, length, angle):
    #Draws n line segments.
    for i in range(n):
        t.fd(length)
        t.lt(angle)
 
def polygon(t, n, length):
    #Draws a polygon with n sides.
    angle = 360/n
    p_line(t, n, length, angle)
 
def arc(t, r, angle):
    #Draws an arc with the given radius and angle.
    arc_length = 2 * math.pi * r * abs(angle) / 360
    n = int(arc_length / 4) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
 
    # Before starting reduces, making a slight left turn.
    t.lt(step_angle/2)
    p_line(t, n, step_length, step_angle)
    t.rt(step_angle/2)


def petal(t, r, angle):
    #Draws a petal using two arcs.
    for i in range(2):
        arc(t, r, angle)
        t.lt(180-angle)


def flower(t, n, r, angle, p):
    #Draws a flower with n petals.
    for i in range(n):
        petal(t, r, angle)
        t.lt(p/n)


def leaf(t, r, angle, p):
    #Draws a leaf and fill it.
    t.begin_fill() # Begin the fill process.
    t.down()
    flower(t, 1, 40, 80, 180)
    t.end_fill()



def main():
 
    window=turtle.Screen() #creat a screen
    window.bgcolor("blue")
    lucy=turtle.Turtle()
    lucy.shape("turtle")
    lucy.color("red")
    lucy.width(5)
    lucy.speed(0)
 
# Drawing flower
    flower(lucy, 10, 40, 100, 360)
 
# Drawing pedicel
    lucy.color("brown")
    lucy.rt(90)
    lucy.fd(200)
 
# Drawing leaf
    lucy.rt(270)
    lucy.color("green")
    leaf(lucy, 40, 80, 180)
    lucy.ht()
    window.exitonclick()
 
main()
#############################################################################


def urlify(s):

    # Remove all non-word characters (everything except numbers and letters)
    s = re.sub(r"[^\w\s]", '', s)

    # Replace all runs of whitespace with a single dash
    s = re.sub(r"\s+", '%20', s)

    return s



# Prints: I-cant-get-no-satisfaction"
#print(urlify("I can't get no satisfaction!"))

def check_profanity(text_to_check):
    #url = "http://www.wdyl.com/profanity?q=" + urllib.parse.urlencode({'sensor' : 'false', 'address' : text_to_check})
    #print(url)
    connection = urllib.request.urlopen("http://www.wdyl.com/profanity?q=" + text_to_check)
    output = connection.read().decode()
    connection.close()
    if "true" in output:
        print("Profanity Alert!!")
    elif "false" in output:
        print("This document has no curse words!")
    else:
        print("could not scan the document properly")




def read_text():
    quetes = open(r"C:\Users\Muhammad\Desktop\fucku.txt")
    contents_of_file = quetes.read()
    urlify(contents_of_file)
    print(contents_of_file)
    quetes.close()
    check_profanity(contents_of_file)
    
    
read_text()    



#!/usr/bin/python
# This script's basic function is to take a URL as input
# and download the page, then uses the wdyl.com API to 
# check if the data has any kind of curse word in it.



def check_profanity(input_text):
    connection = urllib.request.urlopen("http://www.wdyl.com/profanity?q="+input_text)
    output = connection.read().decode()
    print(output)
    connection.close()

def get_content(inp_dom):
    timeout = 10
    socket.setdefaulttimeout(timeout)

    req = urllib.request(inp_dom)
    response = urllib.request.urlopen(req)
    content = response.read().decode()

    return content

argno = len(sys.argv)

if(argno != 2):
    print("Usage: jsinix_curse_check.py http://domain.com")
    sys.exit()

else:
    domain = sys.argv[1]
    all_content = get_content(domain)
    check_profanity(all_content)
"""

class Movie():
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

toy_story = Movie("Toy Story", "A story of a toy comes to life", "", "")

print(toy_story.title)


        