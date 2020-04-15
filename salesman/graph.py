import math

def euclid(p,q):
    x = p[0]-q[0]
    y = p[1]-q[1]
    return math.sqrt(x*x+y*y)

class Graph:

    # Complete as described in the specification, taking care of two cases:
    # the -1 case, where we read points in the Euclidean plane, and
    # the n>0 case, where we read a general graph in a different format.
    # self.perm, self.dists, self.n are the key variables to be set up.
    def __init__(self,n,filename):
        self.points = []
        with open(filename) as file:
            for i in file.readlines():
                nodes = i.split(' ')
                self.points.append([int(nodes[1]), int(nodes[-1].split('\n')[0])])
        self.n = len(self.points) - 1
        self.dists = [i for i in range(self.n)]
        for i in self.points:
            #print(i)
            if self.points[self.points.index(i)] != self.points[-1]:
                self.dists[self.points.index(i)] = euclid(i, self.points[self.points.index(i)+1])
            # else:
            #     self.dists[self.points.index(i)] = euclid(i, self.points[0])
        self.perm = [i for i in range(self.n)]
        self.curr_cost = 0
        self.starting_vertex = n



    # Complete as described in the spec, to calculate the cost of the
    # current tour (as represented by self.perm).
    def tourValue(self):
        temp = self.starting_vertex
        for i in range(self.n):
            self.curr_cost += euclid(self.points[self.starting_vertex], self.points[i])
            temp = self.points[i]
        self.curr_cost += euclid(self.points[self.starting_vertex], self.points[0])
        return self.curr_cost


    # Attempt the swap of cities i and i+1 in self.perm and commit
    # commit to the swap if it improves the cost of the tour.
    # Return True/False depending on success.
    def trySwap(self,i):
        return True if euclid(self.perm[i]) < self.perm[(i+1)] else False

    # Consider the effect of reversiing the segment between
    # self.perm[i] and self.perm[j], and commit to the reversal
    # if it improves the tour value.
    # Return True/False depending on success.              
    def tryReverse(self,i,j):
        pass

    def swapHeuristic(self):
        better = True
        while better:
            better = False
            for i in range(self.n):
                if self.trySwap(i):
                    better = True

    def TwoOptHeuristic(self):
        better = True
        while better:
            better = False
            for j in range(self.n-1):
                for i in range(j):
                    if self.tryReverse(i,j):
                        better = True
                

    # Implement the Greedy heuristic which builds a tour starting
    # from node 0, taking the closest (unused) node as 'next'
    # each time.
    def Greedy(self):
        pass