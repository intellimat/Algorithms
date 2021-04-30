class DisjointSets():
    # not efficient implementation
    def __init__(self, max_value):
        self.smallest = []
        self.makeSet(max_value)
    
    def makeSet(self, max_value):
        for i in range(max_value + 1):
            self.smallest.append(i)

    def find(self, i):
        return self.smallest[i]

    def union(self, i, j):
        i_id = self.find(i)
        j_id = self.find(j)

        if i_id == j_id: return
        
        m = min(i_id,j_id)

        for k in range(0, len(self.smallest)):
            if self.smallest[k] in [i_id, j_id]:
                self.smallest[k] = m


class EfficientDisjointSets():
    # with union by ranking heuristic (and path compression heuristic)
    def __init__(self, max_value):
        self.parent = []
        self.rank = []
        self.__makeSets(max_value)
    
    def __makeSets(self, max_value):
        for i in range(max_value + 1):
            self.parent.append(i)
            self.rank.append(0)
    '''
    # without path compression
    def find(self, i):
        while i != self.parent[i]:
            i = self.parent[i]
        return i
    '''
    # with path compression
    def find(self, i):
        if i != self.parent[i]:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        i_id = self.find(i)
        j_id = self.find(j)

        if i_id == j_id: return

        if self.rank[i_id] > self.rank[j_id]:
            self.parent[j_id] = i_id
        else:
            self.parent[i_id] = j_id
            if self.rank[i_id] == self.rank[j_id]:
                self.rank[j_id] += 1
        
        assert(self.find(i) == self.find(j))
