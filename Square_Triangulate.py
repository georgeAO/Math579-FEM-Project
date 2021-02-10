import numpy as np

# class Node():
#     """
#     Base class for an element of a quadtree
#
#     Attributes:
#         pts (list): indices of vertices defining the triangle
#         parent (Node object): "parent node". If root node then
#         returns a string "root".
#         children (list of node objects): list of four nodes forming
#         the branch of current node
#     """
#     def __init__(self, pts, parent = "root", layer = 0):
#
#         self.pts = pts
#         self.parent = parent
#         self.children = []
#         self.divided = False
#         self.layer = layer
#         return



# class Square_QT():
#     """
#     Quadtree class for a uniform triangulation of a square
#
#     """
#
#     def __init__(self, bl = [0,0], tr = [1,1]):
#
#         # Initialize base triangle formed of 8 uniform triangles
#
#
#
#         self.xyz_init = xyz.copy()
#         #connectivity matrix
#
#         # initial spatial grid
#         self.T = T
#         self.xyz = xyz
#         # first layer of tree structure
#         self.Tree = [Node(t) for t in T]
#         self.nodes = 12
#
#         return
#
#
#     def branch(self, nd):
#         # single triangle input
#         tri = nd.pts
#         self.xyz.append(self.xyz[tri[0]]/2 + self.xyz[tri[1]]/2)
#         self.xyz.append(self.xyz[tri[1]]/2 + self.xyz[tri[2]]/2)
#         self.xyz.append(self.xyz[tri[2]]/2 + self.xyz[tri[0]]/2)
#         i = self.nodes
#         #T_new.append([tri, [[tri[0],i,i+2], [i,tri[1],i+1], [i+1,tri[2],i+2], [i, i+1, i+2]]])
#         #T_new.append([tri, [[tri[0],i,i+2], [i,tri[1],i+1], [i+1,tri[2],i+2], [i, i+1, i+2]]])
#         tt = [[tri[0],i,i+2], [i,tri[1],i+1], [i+1,tri[2],i+2], [i, i+1, i+2]]
#         nd.children = [Node(t, parent = nd, layer = nd.layer +1) for t in tt]
#         self.nodes +=3
#
#         return
#
#     def refine(self, nde, k):
#         """
#         function to add a single layer to tree stucture of T.
#
#
#         G- np.array - 1D list of coordinates
#         N defines how many refinements to perform on the grid G
#         output: quadtree structure for refined mesh
#
#                    /0\
#                   /___\
#                  /\ 3/ \
#                 /_1\/ 2_\
#
#         0 is the first node in parent.
#         k = depth of tree structure. 0 corresponds to first layer.
#         """
#         if nde.layer < k:
#             self.branch(nde)
#             for child in nde.children:
#                 self.refine(child, k)
#         else:
#             return
#         #self.nodes = 2 + 10*(N+k)**2
#         return
#
#     def connectivity(self, N, k, T_con):
#         """
#         output list of connectivity elements for the base level of children
#         """
#         if N.layer < k:
#             for child in N.children:
#                 self.connectivity(child, k, T_con)
#         else:
#             T_con.append(N.pts)
#             return
#         #self.nodes = 2 + 10*(N+k)**2
#         return
#
#     def dist_to(self, A, Qs):
#         """
#         Function to provide list of distances of the queries (Qs) to the list
#         of points in A.
#
#         Inputs:
#         A: [n,3] numpy array
#         Q: [N,3] numpy array
#
#         Output: [n, N] numpy array of distances
#         """
#         #out numpy array
#         outs = np.zeros([len(A),len(Qs)])
#         ii = 0
#         for X in A:
#             temp = X-Qs
#             outs[ii, :] = np.sqrt(temp[:,0]**2 + temp[:,1]**2 + temp[:,2]**2)
#             ii+=1
#
#         return outs
#
#     def dist_init(self, Q):
#         # find root node for each query point
#         """
#         Input: Q - [N,3] numpy array
#         Output: [N,] list of root nodes
#         """
#         XYZ = np.array(self.xyz[0:20])
#         # a = np.array([XYZ[t] for t in self.T])
#         init_dists = self.dist_to(XYZ, Q)
#
#         #build convenient data structure using the min function
#         inds = np.argpartition(init_dists,3)
#
#         #make list indexing the triangles
#
#
#         return
#
#
#
#     def NN_search(self, Qs):
#         """
#         Function to perform nearest neighbour search on quadtree structure
#
#         Input: A - Node object
#                Q: [N,3] numpy array
#
#         Output: Triangle containing point
#         """
#         self.dist_init(Qs)
#         # first find root node triangle:
#
#         #compute distance from nodes:
#
#         return
#









def Square_Triangulate(N, x0 = [0,0], x1 = [1,1]):
    """
    Inputs:
    N - Number of point along each axis
    x0,x1 - x,y coordinates of bottom left and top right corners of square.
    """

    x_coords = np.linspace(x0[0], x1[0], N, endpoint = True)
    y_coords = np.linspace(x0[1], x1[1], N, endpoint = True)

    # Put this into a meshgrid for easier access to coordinate values.

    [X,Y] = np.array(np.meshgrid(x_coords, y_coords))
    #Put this in a more convenient form:
    Nodes = np.zeros([N**2, 3])
    Nodes[:,0], Nodes[:,1], Nodes[:,2] = np.arange(0,int(N**2), dtype = int), X.reshape([N**2,]), Y.reshape([N**2,])

    # Label and create triangulated mesh data structure
    E_u1 = []
    E_u2 = []
    E_u3 = []
    for i in range(0, N-1):
        b = i*N  #beginning in nodes
        l_row = Nodes[b:b+N,0].copy()
        u_row = Nodes[b+N:b+2*N,0].copy()
        E_u1 += list(l_row[0:N-1])
        E_u2 += list(l_row[1:N])
        E_u3 += list(u_row[1:N])
        E_u1 += list(l_row[0:N-1])
        E_u2 += list(u_row[0:N-1])
        E_u3 += list(u_row[1:N])


    M = len(E_u1)
    E = np.zeros([M, 4], dtype = int)
    E[:,0] = np.arange(0, M, dtype = int) # "--------=----------"
    E[0:len(E_u1),1] = E_u1
    E[0:len(E_u2),2] = E_u2
    E[0:len(E_u3),3] = E_u3

    return E, Nodes, [X,Y]


# # Function to plot mesh
# def Mesh_Plot(E, Nodes, boundary = None):
#     """
#     Function to output plot of the mesh created with labelled elements
#     """
#     fig = plt.figure(figsize = (7,7))
#
#     #First create scatter plot with all the nodes
#
#     plt.scatter(Nodes[:,1], Nodes[:,2], c = "k", alpha = 0.5)
#
#     #Then plot lines and label elements
#     for row in E:
#         num = row[0]
#         xs = Nodes[row[1::],1]
#         ys = Nodes[row[1::], 2]
#         # calculate center of element
#         x_c, y_c = np.sum(xs)/3, np.sum(ys)/3
#         plt.text(x_c, y_c, s = "%d" %num, fontsize = 10)
#
#         # Add lines connecting the nodes for each element
#         plt.plot([xs[0], xs[1]], [ys[0], ys[1]], c= "k")
#         plt.plot([xs[1], xs[2]], [ys[1], ys[2]], c= "k")
#         plt.plot([xs[2], xs[0]], [ys[2], ys[0]], c= "k")
#
#     if boundary != None:
#         plt.scatter(Nodes[boundary,1], Nodes[boundary, 2], c = "b")
#
#     return
#


def red_refinement(N,num):
    """
    N = starting number of nodes, i  = number of refinements
    returns an array of # num of nodes along each axis at each stage
    """
    ref = [N]
    for n in range(num-1):
        ref.append(2*ref[n]-1)

    return ref

Ns = red_refinement(4, 2)

# E, Nodes, Mesh = Square_Triangulate(Ns[0])
# Mesh_Plot(E, Nodes)
#
# E, Nodes, Mesh = Square_Triangulate(Ns[1])
# Mesh_Plot(E, Nodes)
