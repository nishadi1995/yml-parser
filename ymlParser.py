import networkx as nx
import matplotlib.pyplot as plt
import yaml

def extract_Vertices(docker_config):
   return list(docker_config['services'].keys())

#each_service equals to a service name
#service contains all the tags of a service
def extract_Edges(docker_config):
   edges=[]
   services = docker_config['services']
   for each_service in services:
       service= services[each_service]
       for tags in service:
           if tags == 'links':
              for i in service['links']:
                  edge=[each_service]
                  edge.append(i)
                  edges.append(tuple(edge))
           elif tags == 'depends_on':
              for i in service['depends_on']:
                  edge=[each_service]
                  edge.append(i)
                  edges.append(tuple(edge))
          
   return edges

def service_graph(nodes,edges):
   #G=nx.Graph() # undirected graph

   G=nx.DiGraph()  
   G.add_nodes_from(nodes)
   G.add_edges_from(edges)

   print("Nodes of graph: ")
   print(G.nodes())
   print("Edges of graph: ")
   print(G.edges())

   pos = nx.circular_layout(G)
   nx.draw(G,pos,with_labels=True,node_size=500,arrowsize=5, arrowstyle='->')
   plt.savefig("simple_path.png")
   plt.show() 

#******************************************************************#

with open("docker-compose.yml", 'r') as ymlfile:
    docker_config = yaml.load(ymlfile)

nodes = extract_Vertices(docker_config)
edges = extract_Edges(docker_config)

service_graph(nodes,edges)

