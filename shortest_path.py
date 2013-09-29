# Simple shortest-path first algorithm
# by Stephen Clark Jr. (sclarkjr@gmail.com)
# Updated: September 29, 
__version__ = '0.1.0'

class Distance(object):
	def __init__(self):
		self.origin = None
		self.distance = None

class Node(object):
	def __init__(self, name, inbound, outbound):
		self.name = name
		self.inbound = inbound
		self.outbound = outbound
		
class Node2(object):
	def __init__(self, name, edges):
		self.name = name
		self.edges = edges

class Graph(object):
	""" main class for finding shorest path """
	def __init__(self, nodes):
		self.nodes = self.load_dict(nodes)
		
	def load_dict(self, graph):
		""" maps a dictionary-based graph """
		map = {}
		
		# populate the dict from graph with empty values
		for node in graph:
			map[node] = Node(node, {}, {})
			
		# map links
		for node in graph:
			print '*----> ' + node
			for neighbor in graph[node]:
				print '\t' + neighbor + ' => ' + str(graph[node][neighbor])
				if not map[node].outbound.has_key(neighbor): # check to see if neigor distance exists (in case of multiple entries)
					map[neighbor].outbound.update({node: graph[node][neighbor]}) #auto generate reverse outbound links
					map[node].outbound.update({neighbor: graph[node][neighbor]}) #outbound links
				else:
					print '##### multiiple values in graph, using shortest value'
					if map[node].outbound[neighbor] > graph[node][neighbor]:
						map[node].outbound.update({neighbor: graph[node][neighbor]}) #outbound links
						map[neighbor].outbound.update({node: graph[node][neighbor]}) #auto generate reverse outbound links
		print '>>>> map <<<<'
		for i in map:
			print str(i) + ' >> ' + str(map[i].outbound)
		return map
		
	def find_path(self, starting_node, target_node):
		""" explore nodes (shortest first) until target is found """
		c = starting_node #current node
		d = [(starting_node, 0),] #queue
		v = [] #visited
		shortest_path = {}
		for i in self.nodes:
			shortest_path[i] = Distance()
		shortest_path[c].distance = 0
		
		while d:
			curr = d[0]
			c = curr[0]

			for i in self.nodes[c].outbound:
				if i not in v:
					d.append((i, self.nodes[c].outbound[i] + curr[1]),) # the 'cuur[0]' add the current dist to start

					if shortest_path[i].distance == None:
						shortest_path[i].distance = self.nodes[c].outbound[i] + curr[1]
						shortest_path[i].origin = c
					elif shortest_path[i].distance > self.nodes[c].outbound[i] + curr[1]:
						shortest_path[i].distance = self.nodes[c].outbound[i] + curr[1]
						shortest_path[i].origin = c
				else:
					pass

					d.sort(lambda x, y: cmp(x[1], y[1])) #sort the queue stack
			d.pop(0) #remove curr from stack
			v.append(curr[0]) #add curr to visited list (no more checking)

			if c == target_node: #stop the loop if target reached
				break
		print 'shortest routes found:'
		for i in shortest_path:
			print i + ': ' + str(shortest_path[i].distance) + ' via ' + str(shortest_path[i].origin)
			
		a = []
		step = target_node
		print "\n"
		print('=> Distance from ' + starting_node + ' to ' + target_node + ': ' + str(shortest_path[step].distance))
		if shortest_path[step].distance != None:
			a = []
			while step != starting_node:
				a.append(step)
				step = shortest_path[step].origin
			a.append(step)
			a.reverse() #reverse since we got steps in reverse order
			print '=> ' + str(a)
		else:
			print '=> No route to %s to %s found' % (target_node, starting_node)
		return
		

def find_shortest_path(starting_node, target_node, graph):
	"""
	function to find shortest path
	usage example:

	shortest_path.find_shortest_path('PHI', 'HOU', shortest_path.USA)
	"""
	g = Graph(graph)
	g.find_path(starting_node, target_node)
	return
	
USA = 	{
			'AUS': {'SA': 35},
			'ATL': {'BIR': 66, 'NAS': 111, 'SAV': 115},
			'BAL': {},
			'BIR': {'BIR': 66, 'JAC': 107, 'NAS': 87, 'NO': 154},
			'BOS': {'NYC': 94},
			'CHI': {'CLE': 157, 'DET': 126, 'IND': 79, 'MEM': 230, 'MIL': 40, 'SPR': 83},
			'CLE': {'PIT': 61},
			'DAL': {'AUS': 86, 'HOU': 110, 'JAC': 185, 'LR': 141, 'NO': 237},
			'DC': {'BAL': 16, 'KNX': 220, 'RIC': 50},
			'DET': {'CLE': 77},
			'DM': {'CHI': 145, 'MIN': 112, 'OMA': 59},
			'FAR': {'SIF': 109},
			'HOU': {'NO': 162, 'SA': 90},
			'IND': {},
			'JAC': {'NO': 84},
			'JAK': {'MIA': 157},
			'KC': {'DM': 85, 'OMA': 78, 'SPR': 126, 'STL': 110, 'TOP': 28},
			'KNX': {'NAS': 82},
			'LA': {},
			'LOU': {'NAS': 77},
			'LR': {'MEM': 63},
			'MEM': {'NAS': 92, 'JAC': 96},
			'MIA': {},
			'MIL': {},
			'MIN': {'MIL': 150, 'FAR': 108},
			'NAS': {},
			'NO': {},
			'NYC': {},
			'OKC': {'DAL': 90, 'KC': 160, 'LR': 146, 'STL': 216},
			'OMA': {},
			'PHI': {'BAL': 43, 'NYC': 39, 'PIT': 129},
			'PHX': {'LA': 169},
			'PIT': {},
			'POR': {},
			'RIC': {},
			'SA': {},
			'SAV': {'JAK': 59, 'RIC': 187},
			'SEA': {'POR': 76},
			'SIF': {},
			'SF': {'LA': 171},
			'SPR': {},
			'STL': {'IND': 110, 'LOU': 118, 'MEM': 125, 'NAS': 137, 'OKC': 216, 'SPR': 44},
			'TOP': {},
		}

