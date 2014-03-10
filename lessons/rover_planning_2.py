def goroveragain(student_func,maze):
    '''
    student_func should be defined in the iPython notebook namespace and provide directions as text strings, either
    'turn right'
    'turn left'
    'turn around'
    'go forward'
    '''

    import numpy as np
    from numpy.random import random_integers as rand
    import matplotlib.pyplot as plt
    import matplotlib.animation as animation

    mazehist = maze.copy()

    position = np.array([7,7])
    target =  np.array([1,4])
    heading = np.array([0,-1]) #facing left
    right = np.array([[0,1],[-1,0]]) #rotation matrix for turning right 90 degrees
    left = np.array([[0,-1],[1,0]]) #rotation matrix for turning left 90 degrees
    escape = 0
    numpasses = 0
#   plt.figure(figsize=(10, 5))
    while escape == 0:
			numpasses = numpasses +1
			maze[position[0],position[1]] = 1
			position
			if (position[0] == target[0]) and (position[1] == target[1]):
					maze[position[0],position[1]] = 1
					maze[target[0],target[1]] = 2
					escape = 1
					out = 'made it'
			next = np.add(position,heading)
			left = np.add(position,left.dot(heading))
			if (maze[next[0],next[1]] ==3) or (maze[next[0],next[1]] == 5):
					infront = 'hazard'
			if (maze[left[0],left[1]] ==3) or (maze[left[0],left[1]] == 5):
					toleft = 'hazard'
			if (maze[next[0],next[1]] ==0) or (maze[next[0],next[1]] ==1) or (maze[next[0],next[1]] ==2):
					infront = 'who cares'
			if (maze[left[0],left[1]] ==0) or (maze[left[0],left[1]] ==1) or (maze[left[0],left[1]] ==2):
					toleft = 'who cares'
			command = student_func(infront,toleft)
			if command == 'turn right':
					heading = right.dot(heading)
			if command == 'turn left':
					heading = left.dot(heading)
			if command == 'go forward':
					position = position + heading
			if command == 'turn around':
					heading = -heading
			if numpasses == 100:
				out = 'stuck in a loop'
				break
            #plt.imshow(maze, cmap=plt.cm.Reds, interpolation='nearest')
            #plt.xticks([]), plt.yticks([])
            #plt.show()
            #print(position, heading)
			mazehist = np.dstack((mazehist,maze))
    fig = plt.figure(figsize=(8,4))

    ims = []
    for i in range(mazehist.shape[2]-1):
        im = plt.imshow(mazehist[:,:,i], cmap=plt.cm.Reds, interpolation='nearest')
        ims.append([im])

    anim = animation.ArtistAnimation(fig, ims, interval=100)

    return out


    # <codecell>

