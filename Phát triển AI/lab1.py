import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

def ve_do_thi(ds_canh, ten_file="do_thi_bfs.png"):
    do_thi = nx.DiGraph()
    do_thi.add_edges_from(ds_canh)
    plt.figure(figsize=(7, 5))
    vi_tri = nx.spring_layout(do_thi, seed=42)

    nx.draw(
        do_thi,
        vi_tri,
        with_labels=True,
        node_color="#ADD8E6",
        node_size=1000,
        font_size=12,
        font_weight="bold",
        edge_color="gray",
        width=2,
        arrows=True
    )
    plt.savefig(ten_file, format="PNG", bbox_inches="tight")
    plt.close()
    print(f" Đã lưu hình đồ thị: {ten_file}\n")

def bfs_co_mo_ta(do_thi, dinh_bat_dau, dinh_dich):
    hang_doi = deque([dinh_bat_dau])
    da_tham = {dinh_bat_dau}
    cha = {dinh_bat_dau: None}

    print("MÔ TẢ QUÁ TRÌNH BFS")
    print("-" * 65)
    print(f"{'Đỉnh':<10} | {'Hàng đợi':<25} | {'Cha'}")
    print("-" * 65)
    print(f"{'':<10} | {str(list(hang_doi)):<25} | ")

    while hang_doi:
        dinh_hien_tai = hang_doi.popleft()
        dinh_moi = []
        danh_sach_ke = do_thi.get(dinh_hien_tai, [])
        for dinh_ke in danh_sach_ke:
            if dinh_ke not in da_tham:
                da_tham.add(dinh_ke)
                hang_doi.append(dinh_ke)
                cha[dinh_ke] = dinh_hien_tai
                dinh_moi.append(dinh_ke)
        chuoi_hang_doi = ", ".join(hang_doi)
        if dinh_moi:
            chuoi_cha = f"Cha[{', '.join(dinh_moi)}] = {dinh_hien_tai}"
        else:
            chuoi_cha = ""
        print(f"{dinh_hien_tai:<10} | {chuoi_hang_doi:<25} | {chuoi_cha}")
        if dinh_hien_tai == dinh_dich:
            print(f"\n🎯 Đã tìm thấy đỉnh đích: {dinh_dich}")
            break
    return cha
if __name__ == "__main__":
    do_thi = {
        'S': ['A', 'B', 'C'],
        'A': ['D', 'E'],
        'B': ['G'],
        'C': ['F'],
        'D': ['H'],
        'E': [],
        'F': [],
        'G': [],
        'H': []
    }
    ds_canh = []

    for dinh, danh_sach_ke in do_thi.items():
        for dinh_ke in danh_sach_ke:
            ds_canh.append((dinh, dinh_ke))
    ve_do_thi(ds_canh)
    bfs_co_mo_ta(
        do_thi=do_thi,
        dinh_bat_dau='S',
        dinh_dich='G'
    )
#
import networkx as nx
import matplotlib.pyplot as plt

def ve_do_thi(ds_ke, ten_file="ket_qua_dfs.png"):
    ds_canh = []
    for dinh, danh_sach_ke in ds_ke.items():
        for dinh_ke in danh_sach_ke:
            ds_canh.append((dinh, dinh_ke))
    do_thi = nx.DiGraph()
    do_thi.add_edges_from(ds_canh)
    plt.figure(figsize=(7, 6))
    vi_tri = {
        0: (1, 3),
        1: (0, 2),
        2: (2, 2),
        3: (0, 1),
        4: (2, 1),
        5: (1, 0)
    }
    nx.draw(
        do_thi,
        vi_tri,
        with_labels=True,
        node_color="#D1E8F7",
        edge_color="gray",
        width=1.5,
        node_size=1000,
        font_size=12,
        font_weight="bold",
        arrows=True
    )
    plt.title("Đồ thị DFS", fontsize=14)
    plt.savefig(ten_file, bbox_inches="tight")
    plt.close()
    print(f" Đã lưu hình đồ thị: {ten_file}")

def dfs_de_quy(do_thi, dinh_hien_tai, da_tham, ket_qua):
    if dinh_hien_tai in da_tham:
        return
    da_tham.add(dinh_hien_tai)
    ket_qua.append(dinh_hien_tai)
    for dinh_ke in do_thi.get(dinh_hien_tai, []):

        dfs_de_quy(
            do_thi,
            dinh_ke,
            da_tham,
            ket_qua
        )

if __name__ == "__main__":
    do_thi_lab = {
        0: [1, 2],
        1: [0, 4, 3],
        2: [0, 4],
        3: [1, 4, 5],
        4: [2, 1, 3, 5],
        5: [3, 4]
    }
    ve_do_thi(do_thi_lab)
    print("\n# --- Duyệt DFS ---")
    dinh_bat_dau = 0
    print(f"Bắt đầu từ đỉnh: {dinh_bat_dau}")
    da_tham = set()
    ket_qua_duyet = []

    dfs_de_quy(
        do_thi_lab,
        dinh_bat_dau,
        da_tham,
        ket_qua_duyet
    )
    print("\nThứ tự duyệt DFS:")
    print(" -> ".join(map(str, ket_qua_duyet)))
    ket_qua_mong_doi = [0, 1, 4, 2, 3, 5]
    print(f"\nKết quả mong đợi: {ket_qua_mong_doi}")

    if ket_qua_duyet == ket_qua_mong_doi:
        print(" Kết quả chính xác")
    else:
        print(" Kết quả khác mong đợi")
#
import networkx as nx
import matplotlib.pyplot as plt

def ve_cay_dfs(do_thi, ma_so_dinh, ten_file="dfs_stack_tree.png"):
    cay_dfs = nx.DiGraph()
    for dinh, danh_sach_ke in do_thi.items():
        for dinh_ke in danh_sach_ke:
            cay_dfs.add_edge(dinh, dinh_ke)
    plt.figure(figsize=(7, 5))
    vi_tri = {
        'S': (2, 4),
        'A': (1, 3),
        'B': (2, 3),
        'C': (3, 3),
        'D': (0.5, 2),
        'E': (1.5, 2),
        'H': (0.5, 1),
        'G': (1.5, 1)
    }
    nhan_hien_thi = {
        dinh: f"{dinh} ({ma_so_dinh[dinh]})"
        for dinh in cay_dfs.nodes()
    }
    nx.draw(
        cay_dfs,
        vi_tri,
        labels=nhan_hien_thi,
        with_labels=True,
        node_color="#66C2A5",
        node_size=1200,
        font_size=11,
        font_weight="bold",
        edge_color="gray",
        width=2,
        arrows=True
    )
    plt.savefig(
        ten_file,
        format="PNG",
        bbox_inches="tight"
    )
    plt.close()
    print(f" Đã lưu hình DFS: {ten_file}\n")

def dfs_stack_co_mo_ta(do_thi, dinh_bat_dau, ma_so_dinh):
    ngan_xep = [dinh_bat_dau]
    da_tham = set()
    cha = {
        dinh_bat_dau: None
    }
    thu_tu_duyet = []
    print("MÔ TẢ QUÁ TRÌNH DFS DÙNG STACK")
    print("-" * 65)
    print(f"{'Đỉnh':<10} | {'Stack':<25} | {'Cha'}")
    print("-" * 65)
    print(f"{'':<10} | {dinh_bat_dau:<25} | ")

    while ngan_xep:
        dinh_hien_tai = ngan_xep.pop()
        if dinh_hien_tai in da_tham:
            continue
        da_tham.add(dinh_hien_tai)
        thu_tu_duyet.append(dinh_hien_tai)
        danh_sach_ke = do_thi.get(
            dinh_hien_tai,
            []
        )
        dinh_moi = []

        for dinh_ke in reversed(danh_sach_ke):
            if dinh_ke not in da_tham:
                ngan_xep.append(dinh_ke)
                cha[dinh_ke] = dinh_hien_tai
                dinh_moi.append(dinh_ke)
        dinh_moi.reverse()

        hien_thi_stack = ", ".join(
            reversed(ngan_xep)
        )
        if dinh_moi:
            chuoi_cha = (
                f"Cha[{', '.join(dinh_moi)}]"
                f" = {dinh_hien_tai}"
            )
        else:
            chuoi_cha = ""
        print(
            f"{dinh_hien_tai:<10} | "
            f"{hien_thi_stack:<25} | "
            f"{chuoi_cha}"
        )
        if dinh_hien_tai == 'G':
            break
    ket_qua_so = [
        str(ma_so_dinh[dinh])
        for dinh in thu_tu_duyet
    ]
    print("\nKết quả DFS từ vertex 0:")
    print(" ".join(ket_qua_so))
if __name__ == "__main__":
    do_thi = {
        'S': ['A', 'B', 'C'],
        'A': ['D', 'E'],
        'B': [],
        'C': [],
        'D': ['H'],
        'E': ['G'],
        'H': [],
        'G': []
    }
    ma_so_dinh = {
        'S': 0,
        'A': 1,
        'B': 2,
        'C': 3,
        'D': 4,
        'E': 5,
        'H': 6,
        'G': 7
    }
    ve_cay_dfs(
        do_thi,
        ma_so_dinh
    )
    dfs_stack_co_mo_ta(
        do_thi,
        dinh_bat_dau='S',
        ma_so_dinh=ma_so_dinh
    )
#
import networkx as nx
import matplotlib.pyplot as plt
import heapq

def ve_do_thi_co_trong_so(do_thi, ten_file="a_star_graph.png"):
    do_thi_nx = nx.Graph()
    for dinh, danh_sach_ke in do_thi.items():
        for dinh_ke, trong_so in danh_sach_ke:
            do_thi_nx.add_edge(
                dinh,
                dinh_ke,
                weight=trong_so
            )

    plt.figure(figsize=(7, 5))
    vi_tri = nx.kamada_kawai_layout(do_thi_nx)
    nx.draw(
        do_thi_nx,
        vi_tri,
        with_labels=True,
        node_color="#FAD02E",
        node_size=1000,
        font_size=12,
        font_weight="bold",
        edge_color="gray",
        width=2
    )
    nhan_canh = nx.get_edge_attributes(
        do_thi_nx,
        "weight"
    )
    nx.draw_networkx_edge_labels(
        do_thi_nx,
        vi_tri,
        edge_labels=nhan_canh,
        font_size=10,
        font_color="red"
    )
    plt.savefig(
        ten_file,
        bbox_inches="tight"
    )
    plt.close()
    print(f" Đã lưu đồ thị: {ten_file}\n")
def heuristic(dinh):
    return 1
def truy_vet_duong_di(
    cha,
    dinh_bat_dau,
    dinh_dich
):
    duong_di = []
    dinh_hien_tai = dinh_dich
    while dinh_hien_tai != dinh_bat_dau:
        duong_di.append(dinh_hien_tai)
        dinh_hien_tai = cha[dinh_hien_tai]
    duong_di.append(dinh_bat_dau)
    duong_di.reverse()
    return duong_di
def a_star(do_thi, dinh_bat_dau, dinh_dich):
    hang_doi_uu_tien = []
    heapq.heappush(
        hang_doi_uu_tien,
        (
            heuristic(dinh_bat_dau),
            dinh_bat_dau
        )
    )
    chi_phi_g = {
        dinh_bat_dau: 0
    }
    cha = {
        dinh_bat_dau: None
    }
    da_xu_ly = set()
    print("MÔ TẢ QUÁ TRÌNH A* SEARCH")
    print("-" * 85)
    print(
        f"{'Đỉnh':<10} | "
        f"{'G-Cost':<10} | "
        f"{'F-Cost':<10} | "
        f"{'Open List'}"
    )
    print("-" * 85)
    while hang_doi_uu_tien:
        f_hien_tai, dinh_hien_tai = heapq.heappop(
            hang_doi_uu_tien
        )
        if dinh_hien_tai in da_xu_ly:
            continue
        hien_thi_open = [
            f"{dinh}(f={f})"
            for f, dinh in hang_doi_uu_tien
        ]
        print(
            f"{dinh_hien_tai:<10} | "
            f"{chi_phi_g[dinh_hien_tai]:<10} | "
            f"{f_hien_tai:<10} | "
            f"{', '.join(hien_thi_open)}"
        )
        if dinh_hien_tai == dinh_dich:
            duong_di = truy_vet_duong_di(
                cha,
                dinh_bat_dau,
                dinh_dich
            )
            print("\n Đã tìm thấy đường đi")
            print(f"Đường đi: {duong_di}")
            print(
                f"Tổng chi phí: "
                f"{chi_phi_g[dinh_dich]}"
            )
            return duong_di
        da_xu_ly.add(dinh_hien_tai)
        for dinh_ke, trong_so in do_thi.get(
            dinh_hien_tai,
            []
        ):
            g_moi = (
                chi_phi_g[dinh_hien_tai]
                + trong_so
            )
            if (
                dinh_ke not in chi_phi_g
                or
                g_moi < chi_phi_g[dinh_ke]
            ):
                chi_phi_g[dinh_ke] = g_moi
                f_moi = (
                    g_moi
                    + heuristic(dinh_ke)
                )
                cha[dinh_ke] = dinh_hien_tai
                heapq.heappush(
                    hang_doi_uu_tien,
                    (
                        f_moi,
                        dinh_ke
                    )
                )
    print("\n Không tồn tại đường đi")
    return None
if __name__ == "__main__":
    do_thi = {
        'A': [
            ('B', 4),
            ('C', 2)
        ],
        'B': [
            ('A', 4),
            ('D', 10),
            ('E', 12)
        ],
        'C': [
            ('A', 2),
            ('E', 7)
        ],
        'D': [
            ('B', 10),
            ('E', 6),
            ('Z', 15)
        ],
        'E': [
            ('B', 12),
            ('C', 7),
            ('D', 6),
            ('Z', 9)
        ],
        'Z': [
            ('D', 15),
            ('E', 9)
        ]
    }
    dinh_bat_dau = 'A'
    dinh_dich = 'Z'
    print(f"Đỉnh bắt đầu: {dinh_bat_dau}")
    print(f"Đỉnh đích: {dinh_dich}\n")
    ve_do_thi_co_trong_so(do_thi)
    a_star(
        do_thi,
        dinh_bat_dau,
        dinh_dich
    )
#