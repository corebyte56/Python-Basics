from turtle import *

# Setup
bgcolor("black")       # Set background color
color("red")           # Set pen and fill color
pensize(3)             # Thicker outline
speed(5)               # Control drawing speed (1–10)

# Draw heart shape  
begin_fill()
left(140)
forward(180)
circle(-90, 200)
left(120)
circle(-90, 200)
forward(180)
end_fill()

# Write text
penup()
goto(0, -20)           # Move to position below heart
color("white")
write("I ❤️ You", align="center", font=("Arial", 24, "bold"))
hideturtle()

done()
