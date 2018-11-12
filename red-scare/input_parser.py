from model import Edge, Vertex, Graph
from sys import stdin

def parse_input(file) -> Graph:
    number_red_vertex = 0
    vertexes = []
    edges = []
    first_last_vertex_split = ""
    for line in file:
        line_split = line.split()
        if(len(line_split)==1):
            vertexes.append(Vertex(line_split[0],False))
        elif(len(line_split)==2):
            if(line_split[1]=='*'):
                vertexes.append(Vertex(line_split[0], True))
            else:
                first_last_vertex_split = line_split
        elif(len(line_split)==3):
            if(line_split[1]=='--'):
                origin_v = next((x for x in vertexes if x.name == line_split[0]), None)
                end_v = next((y for y in vertexes if y.name == line_split[2]), None)
                edges.append(Edge(origin_v, end_v))
                edges.append(Edge(end_v, origin_v))
            elif(line_split[1]=='->'):
                edges.append(Edge(next((x for x in vertexes if x.name == line_split[0]), None), \
                                  next((y for y in vertexes if y.name == line_split[2]), None)))
            else:
                number_red_vertex = line.split()[2]

    start_vertex = next((x for x in vertexes if x.name == first_last_vertex_split[0]), None)
    end_vertex = next((y for y in vertexes if y.name == first_last_vertex_split[1]), None)
    return Graph(start_vertex, end_vertex, vertexes, edges, number_red_vertex)


#the_file = stdin
#print(parse_input(the_file))
