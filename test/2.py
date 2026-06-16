import copy
from collections import deque

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0] * vertices for _ in range(vertices)]
        self.nhan = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

    def them_canh(self, u, v, w):
        self.graph[u][v] = w

    def bfs(self, bat_dau):
        da_tham = [False] * self.V
        hang_doi = deque([bat_dau])
        da_tham[bat_dau] = True
        duong_di = []

        while hang_doi:
            u = hang_doi.popleft()
            duong_di.append(self.nhan[u])

            for v in range(self.V):
                if self.graph[u][v] > 0 and not da_tham[v]:
                    da_tham[v] = True
                    hang_doi.append(v)
        return duong_di

    def dfs_util(self, u, da_tham, duong_di):
        da_tham[u] = True
        duong_di.append(self.nhan[u])
        for v in range(self.V):
            if self.graph[u][v] > 0 and not da_tham[v]:
                self.dfs_util(v, da_tham, duong_di)

    def dfs(self, bat_dau):
        da_tham = [False] * self.V
        duong_di = []
        self.dfs_util(bat_dau, da_tham, duong_di)
        return duong_di

    def min_distance(self, dist, sptSet):
        min_val = float('inf')
        min_index = -1
        for v in range(self.V):
            if dist[v] < min_val and not sptSet[v]:
                min_val = dist[v]
                min_index = v
        return min_index

    def dijkstra(self, src):
        dist = [float('inf')] * self.V
        dist[src] = 0
        sptSet = [False] * self.V
        parent = [-1] * self.V  

        for _ in range(self.V):
            u = self.min_distance(dist, sptSet)
            if u == -1:
                break
            sptSet[u] = True

            for v in range(self.V):
                if self.graph[u][v] > 0 and not sptSet[v] and dist[v] > dist[u] + self.graph[u][v]:
                    dist[v] = dist[u] + self.graph[u][v]
                    parent[v] = u

        return dist, parent

    def lay_duong_di(self, parent, dist, dich):
        if parent[dich] == -1 and dist[dich] == float('inf'):
            return []
        path = []
        curr = dich
        while curr != -1:
            path.append(self.nhan[curr])
            curr = parent[curr]
        return path[::-1]

if __name__ == "__main__":
    g = Graph(10)
    g.them_canh(0, 1, 1)   
    g.them_canh(1, 2, 2)   
    g.them_canh(2, 3, 3)   
    g.them_canh(3, 0, 10)  
    g.them_canh(3, 4, 4)   
    g.them_canh(4, 5, 3)   
    g.them_canh(4, 6, 5)   
    g.them_canh(4, 7, 12)  
    g.them_canh(5, 7, 4)   
    g.them_canh(6, 7, 6)   
    g.them_canh(7, 9, 7)   
    g.them_canh(9, 8, 8)   
    g.them_canh(8, 3, 9)   

    print("YÊU CẦU A: BFS, DFS, DIJKSTRA TỪ ĐỈNH 'a'")
    print(f"BFS: {' -> '.join(g.bfs(0))}")
    print(f"DFS: {' -> '.join(g.dfs(0))}")
    
    dist, parent = g.dijkstra(0)
    print("\nDijkstra từ 'a':")
    for i in range(10):
        if dist[i] != float('inf'):
            path = g.lay_duong_di(parent, dist, i)
            print(f"Khoảng cách a -> {g.nhan[i]}: {dist[i]:<3} | Đường đi: {' -> '.join(path)}")

    print("\nYÊU CẦU B: DIJKSTRA TỪ 'a' TỚI 'i' PHẢI ĐI QUA 'g'")
    dist_a_g, parent_a_g = g.dijkstra(0)
    path_a_g = g.lay_duong_di(parent_a_g, dist_a_g, 6)
    
    dist_g_i, parent_g_i = g.dijkstra(6)
    path_g_i = g.lay_duong_di(parent_g_i, dist_g_i, 8)
    
    if dist_a_g[6] != float('inf') and dist_g_i[8] != float('inf'):
        tong_khoang_cach = dist_a_g[6] + dist_g_i[8]
        duong_di_tong = path_a_g[:-1] + path_g_i
        print(f"Tổng khoảng cách: {tong_khoang_cach}")
        print(f"Đường đi: {' -> '.join(duong_di_tong)}")
    else:
        print("Không tồn tại đường đi thỏa mãn.")

    print("\nYÊU CẦU C: DIJKSTRA TỪ 'a' NHƯNG KHÔNG ĐI QUA 'f'")
    ma_tran_goc = copy.deepcopy(g.graph)
    
    for i in range(10):
        g.graph[i][5] = 0
        g.graph[5][i] = 0
        
    dist_ko_f, parent_ko_f = g.dijkstra(0)
    
    print("Dijkstra từ 'a' (Không qua 'f'):")
    for i in range(10):
        if i == 5:
            print(f"Khoảng cách a -> f: Không thể đến (đã bị cô lập)")
            continue
        if dist_ko_f[i] != float('inf'):
            path = g.lay_duong_di(parent_ko_f, dist_ko_f, i)
            print(f"Khoảng cách a -> {g.nhan[i]}: {dist_ko_f[i]:<3} | Đường đi: {' -> '.join(path)}")
            
    g.graph = ma_tran_goc