class Union():
    
    def __init__(self, n):
        self.ls = list(range(n))
        
    def find(self, i):
        if self.ls[i] != i:
            self.ls[i] = self.find(self.ls[i])
        return self.ls[i]
    
    def union(self, i, j):
        self.ls[i] = self.ls[j]
        
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        # Sort the unique positions of all the edges.
        edges = sorted(list(set([x for building in buildings for x in building[:2]])))
        
        # Hast table 'edge_index_map' record every {position : index} pairs in 'edges'.
        edge_index_map = {x:idx for idx, x in enumerate(edges)} 
        
        # Sort buildings by descending order of heights.
        buildings.sort(key=lambda x: -x[2])
        
        # Initalize a disjoin set for all indexs, each index's 
        # root is itself. Since there is no building added yet, 
        # the height at each position is 0.
        n = len(edges)
        edge_UF = Union(n)
        heights = [0] * n
    
        # Iterate over all the buildings by descending height.
        for left_edge, right_edge, height in buildings:
            # For current x position, get the corresponding index.
            left_idx, right_idx = edge_index_map[left_edge], edge_index_map[right_edge]
            
            # While we haven't update the the root of 'left_idx':
            while left_idx < right_idx: 
                # Find the root of left index 'left_idx', that is:
                # The rightmost index having the same height as 'left_idx'.
                left_idx = edge_UF.find(left_idx)

                # If left_idx < right_idx, we have to update both the root and height
                # of left_idx, and move on to the next index towards right_idx.
                # That is: increment left_idx by 1.
                if left_idx < right_idx:
                    edge_UF.union(left_idx, right_idx)
                    heights[left_idx] = height
                    left_idx += 1
                    
        # Finally, we just need to iterate over updated heights, and
        # add every skyline key point to 'answer'.
        answer = []
        for i in range(n):
            if i == 0 or heights[i] != heights[i - 1]:
                answer.append([edges[i], heights[i]])
        return answer