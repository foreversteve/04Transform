from display import *
from matrix import *
from draw import *

"""
Goes through the file named filename and performs all of the actions listed in that file.
The file follows the following format:
	 Every command is a single character that takes up a line
	 Any command that requires arguments must have those arguments in the second line.
	 The commands are as follows:
		 line: add a line to the edge matrix -
			   takes 6 arguemnts (x0, y0, z0, x1, y1, z1)
		 ident: set the transform matrix to the identity matrix -
		 scale: create a scale matrix,
				then multiply the transform matrix by the scale matrix -
				takes 3 arguments (sx, sy, sz)
		 translate: create a translation matrix,
					then multiply the transform matrix by the translation matrix -
					takes 3 arguments (tx, ty, tz)
		 rotate: create a rotation matrix,
				 then multiply the transform matrix by the rotation matrix -
				 takes 2 arguments (axis, theta) axis should be x y or z
		 apply: apply the current transformation matrix to the edge matrix
		 display: clear the screen, then
				  draw the lines of the edge matrix to the screen
				  display the screen
		 save: clear the screen, then
			   draw the lines of the edge matrix to the screen
			   save the screen to a file -
			   takes 1 argument (file name)
		 quit: end parsing

See the file script for an example of the file format
"""
def parse_file( fname, points, transform, screen, color ):
	file=open(fname,'rU').read().split('\n')
	args = set(["line","ident","scale","move","rotate","apply","display","save"])
	index= 0
	while index < len(file):
		if file[index] == "line":
			arr = [int(val) for val in file[index+1].split()]
			add_edge(points,arr[0],arr[1],arr[2],arr[3],arr[4],arr[5])

			index+=2
			continue
		elif file[index] == "ident":
			matrix = new_matrix()
			ident(matrix)

			transform = matrix
			index+=1
			continue
		elif file[index] == "scale":
			arr = [int(val) for val in file[index+1].split()]
			# print(arr)
			sm = make_scale(arr[0],arr[1],arr[2])
			# print_matrix(sm)
			# print_matrix(transform)
			matrix_mult(sm,transform)

			index+=2
			continue
		elif file[index] == "move":
			arr = [int(val) for val in file[index+1].split()]
			sm = make_translate(arr[0],arr[1],arr[2])
			
			matrix_mult(sm,transform)

			index+=2
			continue

		elif file[index] == "rotate":
			arr = file[index+1].split()
			arr[1] = int(arr[1])
			sm = 0
			if arr[0] == "x":
				sm = make_rotX(arr[1])
			if arr[0] == "y":
				sm = make_rotY(arr[1])
			if arr[0] == "z":
				sm = make_rotZ(arr[1])
			# print_matrix(sm)
			matrix_mult(sm,transform)
			index+=2
			continue

		elif file[index] == "apply":
			matrix_mult(transform,points)
			for col in range(len(points)):
				for row in range(len(points[0])):
					points[col][row] = int(points[col][row])
			index+=1
			continue
		elif file[index] == "display":
			clear_screen(screen)
			draw_lines(points,screen,color)

			display( screen )
			index+=1
		elif file[index] == "save":
			clear_screen(screen)
			draw_lines(points,screen,color)

			save_extension(screen,file[index+1])
			index+=2
		else:
			print("wtf")
			return
















