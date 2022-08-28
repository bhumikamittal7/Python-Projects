import turtle

#==================================================
# Functions
#==================================================
# t     = turtle
# sides = number of sides in my polygon
# len   = length of each side
# vertices = [none for i in range(sides)]
def drawPolygon(t, sides, size):		#source - Classroom
	# we need to return a list of vertices
	vertices = []

	angle = 360.0/sides # play around with this
	for i in range(sides):
		vertices.append(  t.pos()  )
		t.forward(size)
		t.right(angle)
	# loop ends

	return vertices

def drawEpicycloid(T, multiplier, side):		#modified version of epicycloid code from class

	numVertices = 200 # number of vertices or sides
	sideSize    = side
	v = drawPolygon(T, numVertices, sideSize)

	#==========================

	used = [False]*numVertices

	#do this for all values of current from 1 to 199
	for current in range(1, 200):
		T.penup()
		T.setposition( v[current] )
		T.pendown()

		while used[current] == False:

			used[current] = True # marking this place as used

			nextVertex = (current * multiplier) % numVertices

			# draws a line from current position to v[nextVertex]
			T.setposition( v[nextVertex] )

			current = nextVertex

def amongUs(T, BODY_COLOR):		#base source (it has been modified, not copied) - GitHub (to draw among us character)
	def body(t):
	    t.pensize(10)
	    t.fillcolor(BODY_COLOR)
	    t.begin_fill()

	    # right side
	    t.right(90)
	    t.forward(50)
	    t.right(180)
	    t.circle(40, -180)
	    t.right(180)
	    t.forward(200)

	    # head curve
	    t.right(180)
	    t.circle(100, -180)

	    # left side
	    t.backward(20)
	    t.left(15)
	    t.circle(500, -20)
	    t.backward(20)

	    t.circle(40, -180)
	    t.left(7)
	    t.backward(50)

	    # hip
	    t.up()
	    t.left(90)
	    t.forward(10)
	    t.right(90)
	    t.down()
	    t.right(240)
	    t.circle(50, -70)

	    t.end_fill()

	def glass(t):
	    t.up()
	    t.right(230)
	    t.forward(100)
	    t.left(90)
	    t.forward(20)
	    t.right(90)

	    t.down()
	    t.fillcolor("#9acedc")
	    t.begin_fill()

	    t.right(150)
	    t.circle(90, -55)

	    t.right(180)
	    t.forward(1)
	    t.right(180)
	    t.circle(10, -65)
	    t.right(180)
	    t.forward(110)
	    t.right(180)
	    
	    t.circle(50, -190)
	    t.right(170)
	    t.forward(80)

	    t.right(180)
	    t.circle(45, -30)

	    t.end_fill()

	def backpack(t):
	    t.up()
	    t.right(60)
	    t.forward(100)
	    t.right(90)
	    t.forward(75)

	    t.fillcolor(BODY_COLOR)
	    t.begin_fill()

	    t.down()
	    t.forward(30)
	    t.right(255)

	    t.circle(300, -30)
	    t.right(260)
	    t.forward(30)

	    t.end_fill()
	    
	body(T)
	glass(T)
	backpack(T)

def star(t):						#base source (it has been modified, not copied) - geeksforgeeks.org/turtle-programming-python/
	colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
	for i in range(100):
	    t.pencolor(colors[i%6])
	    t.width(i/100 + 1)
	    t.forward(i)
	    t.left(59)

def magic():
	T = turtle.Turtle()
	#==============================================
	# settings
	turtle.tracer(0,0) # turn off animation
	T.hideturtle()
	T.pensize(2)
	turtle.bgcolor("black")

	#==============================================
	#==============================================
	T.penup()
	T.goto(0, 0)
	T.pendown()
	T.pencolor("blue")
	drawEpicycloid(T, 99, 16)	
	#==============================================
	T.pencolor("black")
	amongUs(T, "red")
	#==============================================
	T.penup()
	T.setposition(395,196)
	T.pendown()
	T.pensize(0.2)
	T.pencolor("purple")
	drawEpicycloid(T,56, 1.2)
	#==============================================
	T.penup()
	T.setposition(400,300)
	T.pendown()
	T.pensize(0.5)
	T.pencolor("pink")
	drawEpicycloid(T,41, 4.5)
	#==============================================
	T.penup()
	T.setposition(-400,300)
	T.pendown()
	T.pensize(0.5)
	T.pencolor("light blue")
	drawEpicycloid(T,69, 4.5)
	#==============================================
	T.penup()
	T.setposition(-600,-200)
	T.pendown()
	star(T)
	#==============================================
	T.penup()
	T.setposition(600,-200)
	T.pendown()
	star(T)
	#==============================================
	T.penup()
	T.setposition(0,300)
	T.pendown()
	T.pencolor("orange")
	T.write("There is an imposter among us", False, 'center', font=('Arial', 30, 'bold'))
	turtle.update()
	turtle.done()

magic()