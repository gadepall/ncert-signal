import matplotlib.pyplot as plot

def x(n):
        if n<0:
                return 0
        else:
                return 8 + 9*n
      
	
x_range = range(-10,11)
y_range=[x(n) for n in range(-10,11)]

plot.stem(x_range,y_range)

plot.xlabel('n')
plot.ylabel('x(n)')
#plot.title('Stem plot of x(n) v/s n')
plot.savefig("x(n)_plot.png")

plot.show()
exit()

