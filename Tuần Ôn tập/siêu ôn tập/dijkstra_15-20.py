import heapq
from typing import List, Dict, Tuple, Any

# ==========================================
# CÁC HÀM THUẬT TOÁN (CORE LOGIC)
# ==========================================

def dijkstra_trace(graph: Dict[int, List[Tuple[int, int]]], start: int, end: int) -> Tuple[Dict[int, float], List[int]]:
    dist = {node: float('inf') for node in graph}
    parent = {node: None for node in graph}
    dist[start] = 0
    pq = [(0, start)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]: continue
        for v, weight in graph.get(u, []):
            if dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                parent[v] = u
                heapq.heappush(pq, (dist[v], v))
    path = []
    curr = end
    while curr is not None:
        path.append(curr)
        curr = parent[curr]
    return dist, path[::-1]

def bellman_ford(edges: List[Tuple[int, int, int]], n: int, start: int) -> List[float]:
    dist = [float('inf')] * n
    dist[start] = 0
    for _ in range(n - 1):
        for u, v, w in edges:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
    return dist

def dijkstra_grid(grid: List[List[int]]) -> int:
    rows, cols = len(grid), len(grid[0])
    dist = [[float('inf')] * cols for _ in range(rows)]
    dist[0][0] = grid[0][0]
    pq = [(grid[0][0], 0, 0)]
    while pq:
        d, r, c = heapq.heappop(pq)
        if r == rows-1 and c == cols-1: return d
        for dr, dc in [(0,1), (0,-1), (1,0), (-1,0)]:
            nr, nc = r+dr, c+dc
            if 0 <= nr < rows and 0 <= nc < cols:
                if d + grid[nr][nc] < dist[nr][nc]:
                    dist[nr][nc] = d + grid[nr][nc]
                    heapq.heappush(pq, (dist[nr][nc], nr, nc))
    return -1

# ==========================================
# CẤU HÌNH MENU DATA-DRIVEN
# ==========================================
Noidung = {
    '15': {
        'ten': 'CÂU 15: DIJKSTRA CƠ BẢN',
        'du_lieu': {'graph': {0: [(1, 4), (2, 1)], 1: [(3, 1)], 2: [(1, 2), (3, 5)], 3: []}, 's': 0, 't': 3},
        'ham': lambda d: dijkstra_trace(d['graph'], d['s'], d['t'])[0][d['t']],
        'format': lambda d, kq: f"Chi phí ngắn nhất từ {d['s']} tới {d['t']}: {kq}"
    },
    '16': {
        'ten': 'CÂU 16: TRUY VẾT ĐƯỜNG ĐI DIJKSTRA',
        'du_lieu': {'graph': {0: [(1, 4), (2, 1)], 1: [(3, 1)], 2: [(1, 2), (3, 5)], 3: []}, 's': 0, 't': 3},
        'ham': lambda d: dijkstra_trace(d['graph'], d['s'], d['t'])[1],
        'format': lambda d, kq: f"Đường đi từ {d['s']} tới {d['t']}: {' -> '.join(map(str, kq))}"
    },
    '17': {
        'ten': 'CÂU 17: DIJKSTRA VỚI HEAP (TỐI ƯU)',
        'du_lieu': {'graph': {0: [(1, 4), (2, 1)], 1: [(3, 1)], 2: [(1, 2), (3, 5)], 3: []}, 's': 0},
        'ham': lambda d: dijkstra_trace(d['graph'], d['s'], 3)[0],
        'format': lambda d, kq: f"Khoảng cách từ {d['s']} tới tất cả đỉnh: {kq}"
    },
    '18': {
        'ten': 'CÂU 18: BELLMAN-FORD (XỬ LÝ CẠNH ÂM)',
        'du_lieu': {'edges': [(0, 1, 4), (0, 2, 2), (2, 1, -5)], 'n': 3, 's': 0},
        'ham': lambda d: bellman_ford(d['edges'], d['n'], d['s']),
        'format': lambda d, kq: f"Khoảng cách từ nguồn 0: {kq} (Cạnh âm -5 được xử lý chính xác)"
    },
    '19': {
        'ten': 'CÂU 19: DIJKSTRA TRÊN LƯỚI',
        'du_lieu': {'grid': [[1, 3, 1], [1, 5, 1], [4, 2, 1]]},
        'ham': lambda d: dijkstra_grid(d['grid']),
        'format': lambda d, kq: f"Tổng chi phí nhỏ nhất từ góc trái trên xuống phải dưới: {kq}"
    },
    '20': {
        'ten': 'CÂU 20: SO SÁNH DIJKSTRA, BELLMAN-FORD & A*',
        'du_lieu': {},
        'ham': lambda d: "Lý thuyết",
        'format': lambda d, kq: (
            "So sánh:\n"
            "- Dijkstra: Nhanh O((V+E)logV), chỉ áp dụng cạnh >= 0 [cite: 372-373].\n"
            "- Bellman-Ford: Chậm hơn O(VE), nhưng xử lý được cạnh âm và phát hiện chu trình âm [cite: 372-373].\n"
            "- A*: Kết hợp Dijkstra + Heuristic, giúp tìm đích nhanh hơn bằng cách 'đoán' hướng [cite: 372-374]."
        )
    }
}

def chay_bai(cfg):
    print(f"\n{'='*70}\n {cfg['ten']}\n{'='*70}")
    print(f"Kết quả: {cfg['ham'](cfg['du_lieu'])}")

if __name__ == '__main__':
    try:
        while True:
            print("\n" + "*"*70 + "\n MENU: PHIÊN 2 (CÂU 15-20) \n" + "*"*70)
            for k in ['15', '16', '17', '18', '19', '20']:
                print(f" {k:>2}. {Noidung[k]['ten']}")
            chon = input("\nLựa chọn (0 để thoát): ").strip()
            if chon == '0': break
            elif chon in Noidung: chay_bai(Noidung[chon])
            else: print("Lựa chọn không hợp lệ!")
    except KeyboardInterrupt: pass