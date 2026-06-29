<<<<<<< HEAD
from typing import List, Tuple, Any

def bai11_khong_on_dinh(a: List[Tuple[int, str]]) -> List[Tuple[int, str]]:
    b = a[:]
    n = len(b)
    for i in range(n - 1):
        vt_min = i
        for j in range(i + 1, n):
            if b[j][0] < b[vt_min][0]:
                vt_min = j
        b[i], b[vt_min] = b[vt_min], b[i]
    return b

def bai12_on_dinh(a: List[Tuple[int, str]]) -> List[Tuple[int, str]]:
    b = a[:]
    n = len(b)
    for i in range(n - 1):
        vt_min = i
        for j in range(i + 1, n):
            if b[j][0] < b[vt_min][0]:
                vt_min = j
        gia_tri_min = b[vt_min]
        while vt_min > i:
            b[vt_min] = b[vt_min - 1]
            vt_min -= 1
        b[i] = gia_tri_min
    return b

def bai13_sap_xep_doi_tuong(a: List[Tuple[str, int]]) -> List[Tuple[str, int]]:
    b = a[:]
    n = len(b)
    for i in range(n - 1):
        vt_min = i
        for j in range(i + 1, n):
            if b[j][1] < b[vt_min][1]:
                vt_min = j
        b[i], b[vt_min] = b[vt_min], b[i]
    return b

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def bai14_dslk(a: List[int]) -> List[int]:
    if not a:
        return []
    
    head = Node(a[0])
    curr = head
    for val in a[1:]:
        curr.next = Node(val)
        curr = curr.next

    dummy_ket_qua = Node(0)
    curr_ket_qua = dummy_ket_qua

    while head:
        prev_min = None
        curr_min = head
        min_val = head.val
        
        prev = None
        curr_node = head
        while curr_node:
            if curr_node.val < min_val:
                min_val = curr_node.val
                curr_min = curr_node
                prev_min = prev
            prev = curr_node
            curr_node = curr_node.next
            
        if prev_min:
            prev_min.next = curr_min.next
        else:
            head = head.next
            
        curr_min.next = None
        curr_ket_qua.next = curr_min
        curr_ket_qua = curr_ket_qua.next
        
    ket_qua = []
    curr_ket_qua = dummy_ket_qua.next
    while curr_ket_qua:
        ket_qua.append(curr_ket_qua.val)
        curr_ket_qua = curr_ket_qua.next
    return ket_qua

def bai15_sap_xep_k_phan_tu(a: List[int], k: int) -> List[int]:
    b = a[:]
    n = len(b)
    so_vong = min(k, n)
    for i in range(so_vong):
        vt_min = i
        for j in range(i + 1, n):
            if b[j] < b[vt_min]:
                vt_min = j
        b[i], b[vt_min] = b[vt_min], b[i]
    return b

def bai16_tri_tuyet_doi(a: List[int]) -> List[int]:
    b = a[:]
    n = len(b)
    for i in range(n - 1):
        vt_min = i
        for j in range(i + 1, n):
            if abs(b[j]) < abs(b[vt_min]):
                vt_min = j
        b[i], b[vt_min] = b[vt_min], b[i]
    return b

def bai17_nho_thu_k(a: List[int], k: int) -> int:
    b = a[:]
    n = len(b)
    so_vong = min(k, n)
    for i in range(so_vong):
        vt_min = i
        for j in range(i + 1, n):
            if b[j] < b[vt_min]:
                vt_min = j
        b[i], b[vt_min] = b[vt_min], b[i]
    return b[k - 1]

Noidung = {
    '11': {
        'ten': 'BÀI 11: TÍNH KHÔNG ỔN ĐỊNH',
        'du_lieu': {'a': [(2, 'a'), (2, 'b'), (1, 'c')]},
        'mong_doi': [(1, 'c'), (2, 'b'), (2, 'a')],
        'ham': lambda d: bai11_khong_on_dinh(d['a']),
        'format': lambda d, kq: f"Mảng gốc: {d['a']}\nSau sắp xếp: {kq}\nNhận xét: 'a' và 'b' bị đảo thứ tự"
    },
    '12': {
        'ten': 'BÀI 12: SELECTION SORT ỔN ĐỊNH',
        'du_lieu': {'a': [(2, 'a'), (2, 'b'), (1, 'c')]},
        'mong_doi': [(1, 'c'), (2, 'a'), (2, 'b')],
        'ham': lambda d: bai12_on_dinh(d['a']),
        'format': lambda d, kq: f"Mảng gốc: {d['a']}\nSau sắp xếp: {kq}\nNhận xét: Ban đầu 'a' trước 'b', sau sắp xếp 'b' lại trước 'a' -> KHÔNG ỔN ĐỊNH"
    },
    '13': {
        'ten': 'BÀI 13: SẮP XẾP ĐỐI TƯỢNG THEO KHÓA (ĐIỂM SỐ)',
        'du_lieu': {'a': [('An', 8), ('Ba', 5)]},
        'mong_doi': [('Ba', 5), ('An', 8)],
        'ham': lambda d: bai13_sap_xep_doi_tuong(d['a']),
        'format': lambda d, kq: f"Mảng gốc: {d['a']}\nSau sắp xếp: {kq}"
    },
    '14': {
        'ten': 'BÀI 14: SELECTION SORT TRÊN DANH SÁCH LIÊN KẾT',
        'du_lieu': {'a': [3, 1, 2]},
        'mong_doi': [1, 2, 3],
        'ham': lambda d: bai14_dslk(d['a']),
        'format': lambda d, kq: f"Mảng gốc: {d['a']} (mô phỏng Linked List)\nSau sắp xếp: {kq}"
    },
    '15': {
        'ten': 'BÀI 15: SẮP XẾP MỘT PHẦN (K NHỎ NHẤT)',
        'du_lieu': {'a': [5, 3, 1, 4, 2], 'k': 2},
        'mong_doi': [1, 2, 5, 4, 3],
        'ham': lambda d: bai15_sap_xep_k_phan_tu(d['a'], d['k']),
        'format': lambda d, kq: f"Mảng gốc: {d['a']}\nSắp xếp {d['k']} vòng: {kq}"
    },
    '16': {
        'ten': 'BÀI 16: SẮP XẾP THEO TRỊ TUYỆT ĐỐI',
        'du_lieu': {'a': [-3, 1, -2, 2]},
        'mong_doi': [1, -2, 2, -3],
        'ham': lambda d: bai16_tri_tuyet_doi(d['a']),
        'format': lambda d, kq: f"Mảng gốc: {d['a']}\nSau sắp xếp: {kq}"
    },
    '17': {
        'ten': 'BÀI 17: TÌM PHẦN TỬ NHỎ THỨ K',
        'du_lieu': {'a': [7, 2, 5, 1, 9], 'k': 3},
        'mong_doi': 5,
        'ham': lambda d: bai17_nho_thu_k(d['a'], d['k']),
        'format': lambda d, kq: f"Mảng gốc: {d['a']}\nPhần tử nhỏ thứ {d['k']}: {kq}\nĐộ phức tạp: O(n·k) = O({len(d['a'])}·{d['k']}) = O({len(d['a'])*d['k']})"
    }
}

def chay_bai(cfg):
    print(f"\n{'='*50}\n {cfg['ten']}\n{'='*50}")
    kq = cfg['ham'](cfg['du_lieu'])
    print(cfg['format'](cfg['du_lieu'], kq))
    
    if isinstance(cfg['mong_doi'], list) and len(cfg['mong_doi']) > 0 and isinstance(cfg['mong_doi'][0], list):
        print("Kết quả mong đợi: \n          " + "\n          ".join(str(x) for x in cfg['mong_doi']))
    else:
        print(f"Kết quả mong đợi: {cfg['mong_doi']}")
        
    if kq == cfg['mong_doi']:
        print("Trạng thái: THÀNH CÔNG")
    else:
        print("Trạng thái: THẤT BẠI")

if __name__ == '__main__':
    try:
        while True:
            print("\n" + "*"*50)
            print(" MENU SELECTION SORT: PHẦN 3 (BÀI 11 - 17) ")
            print(" CHỌN BÀI (11-17) HOẶC 0 ĐỂ THOÁT | 'all' ĐỂ CHẠY HẾT")
            print("*"*50)
            for k, v in Noidung.items():
                print(f" {k:>6}. {v['ten']}")
            chon = input("\nLựa chọn: ").strip()
            
            if chon == '0':
                break
            elif chon.lower() == 'all':
                for cfg in Noidung.values():
                    chay_bai(cfg)
            elif chon in Noidung:
                chay_bai(Noidung[chon])
            else:
                print("Lựa chọn không hợp lệ, vui lòng thử lại!")
    except KeyboardInterrupt:
=======
from typing import List, Tuple, Any

def bai11_khong_on_dinh(a: List[Tuple[int, str]]) -> List[Tuple[int, str]]:
    b = a[:]
    n = len(b)
    for i in range(n - 1):
        vt_min = i
        for j in range(i + 1, n):
            if b[j][0] < b[vt_min][0]:
                vt_min = j
        b[i], b[vt_min] = b[vt_min], b[i]
    return b

def bai12_on_dinh(a: List[Tuple[int, str]]) -> List[Tuple[int, str]]:
    b = a[:]
    n = len(b)
    for i in range(n - 1):
        vt_min = i
        for j in range(i + 1, n):
            if b[j][0] < b[vt_min][0]:
                vt_min = j
        gia_tri_min = b[vt_min]
        while vt_min > i:
            b[vt_min] = b[vt_min - 1]
            vt_min -= 1
        b[i] = gia_tri_min
    return b

def bai13_sap_xep_doi_tuong(a: List[Tuple[str, int]]) -> List[Tuple[str, int]]:
    b = a[:]
    n = len(b)
    for i in range(n - 1):
        vt_min = i
        for j in range(i + 1, n):
            if b[j][1] < b[vt_min][1]:
                vt_min = j
        b[i], b[vt_min] = b[vt_min], b[i]
    return b

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def bai14_dslk(a: List[int]) -> List[int]:
    if not a:
        return []
    
    head = Node(a[0])
    curr = head
    for val in a[1:]:
        curr.next = Node(val)
        curr = curr.next

    dummy_ket_qua = Node(0)
    curr_ket_qua = dummy_ket_qua

    while head:
        prev_min = None
        curr_min = head
        min_val = head.val
        
        prev = None
        curr_node = head
        while curr_node:
            if curr_node.val < min_val:
                min_val = curr_node.val
                curr_min = curr_node
                prev_min = prev
            prev = curr_node
            curr_node = curr_node.next
            
        if prev_min:
            prev_min.next = curr_min.next
        else:
            head = head.next
            
        curr_min.next = None
        curr_ket_qua.next = curr_min
        curr_ket_qua = curr_ket_qua.next
        
    ket_qua = []
    curr_ket_qua = dummy_ket_qua.next
    while curr_ket_qua:
        ket_qua.append(curr_ket_qua.val)
        curr_ket_qua = curr_ket_qua.next
    return ket_qua

def bai15_sap_xep_k_phan_tu(a: List[int], k: int) -> List[int]:
    b = a[:]
    n = len(b)
    so_vong = min(k, n)
    for i in range(so_vong):
        vt_min = i
        for j in range(i + 1, n):
            if b[j] < b[vt_min]:
                vt_min = j
        b[i], b[vt_min] = b[vt_min], b[i]
    return b

def bai16_tri_tuyet_doi(a: List[int]) -> List[int]:
    b = a[:]
    n = len(b)
    for i in range(n - 1):
        vt_min = i
        for j in range(i + 1, n):
            if abs(b[j]) < abs(b[vt_min]):
                vt_min = j
        b[i], b[vt_min] = b[vt_min], b[i]
    return b

def bai17_nho_thu_k(a: List[int], k: int) -> int:
    b = a[:]
    n = len(b)
    so_vong = min(k, n)
    for i in range(so_vong):
        vt_min = i
        for j in range(i + 1, n):
            if b[j] < b[vt_min]:
                vt_min = j
        b[i], b[vt_min] = b[vt_min], b[i]
    return b[k - 1]

Noidung = {
    '11': {
        'ten': 'BÀI 11: TÍNH KHÔNG ỔN ĐỊNH',
        'du_lieu': {'a': [(2, 'a'), (2, 'b'), (1, 'c')]},
        'mong_doi': [(1, 'c'), (2, 'b'), (2, 'a')],
        'ham': lambda d: bai11_khong_on_dinh(d['a']),
        'format': lambda d, kq: f"Mảng gốc: {d['a']}\nSau sắp xếp: {kq}\nNhận xét: 'a' và 'b' bị đảo thứ tự"
    },
    '12': {
        'ten': 'BÀI 12: SELECTION SORT ỔN ĐỊNH',
        'du_lieu': {'a': [(2, 'a'), (2, 'b'), (1, 'c')]},
        'mong_doi': [(1, 'c'), (2, 'a'), (2, 'b')],
        'ham': lambda d: bai12_on_dinh(d['a']),
        'format': lambda d, kq: f"Mảng gốc: {d['a']}\nSau sắp xếp: {kq}\nNhận xét: Ban đầu 'a' trước 'b', sau sắp xếp 'b' lại trước 'a' -> KHÔNG ỔN ĐỊNH"
    },
    '13': {
        'ten': 'BÀI 13: SẮP XẾP ĐỐI TƯỢNG THEO KHÓA (ĐIỂM SỐ)',
        'du_lieu': {'a': [('An', 8), ('Ba', 5)]},
        'mong_doi': [('Ba', 5), ('An', 8)],
        'ham': lambda d: bai13_sap_xep_doi_tuong(d['a']),
        'format': lambda d, kq: f"Mảng gốc: {d['a']}\nSau sắp xếp: {kq}"
    },
    '14': {
        'ten': 'BÀI 14: SELECTION SORT TRÊN DANH SÁCH LIÊN KẾT',
        'du_lieu': {'a': [3, 1, 2]},
        'mong_doi': [1, 2, 3],
        'ham': lambda d: bai14_dslk(d['a']),
        'format': lambda d, kq: f"Mảng gốc: {d['a']} (mô phỏng Linked List)\nSau sắp xếp: {kq}"
    },
    '15': {
        'ten': 'BÀI 15: SẮP XẾP MỘT PHẦN (K NHỎ NHẤT)',
        'du_lieu': {'a': [5, 3, 1, 4, 2], 'k': 2},
        'mong_doi': [1, 2, 5, 4, 3],
        'ham': lambda d: bai15_sap_xep_k_phan_tu(d['a'], d['k']),
        'format': lambda d, kq: f"Mảng gốc: {d['a']}\nSắp xếp {d['k']} vòng: {kq}"
    },
    '16': {
        'ten': 'BÀI 16: SẮP XẾP THEO TRỊ TUYỆT ĐỐI',
        'du_lieu': {'a': [-3, 1, -2, 2]},
        'mong_doi': [1, -2, 2, -3],
        'ham': lambda d: bai16_tri_tuyet_doi(d['a']),
        'format': lambda d, kq: f"Mảng gốc: {d['a']}\nSau sắp xếp: {kq}"
    },
    '17': {
        'ten': 'BÀI 17: TÌM PHẦN TỬ NHỎ THỨ K',
        'du_lieu': {'a': [7, 2, 5, 1, 9], 'k': 3},
        'mong_doi': 5,
        'ham': lambda d: bai17_nho_thu_k(d['a'], d['k']),
        'format': lambda d, kq: f"Mảng gốc: {d['a']}\nPhần tử nhỏ thứ {d['k']}: {kq}\nĐộ phức tạp: O(n·k) = O({len(d['a'])}·{d['k']}) = O({len(d['a'])*d['k']})"
    }
}

def chay_bai(cfg):
    print(f"\n{'='*50}\n {cfg['ten']}\n{'='*50}")
    kq = cfg['ham'](cfg['du_lieu'])
    print(cfg['format'](cfg['du_lieu'], kq))
    
    if isinstance(cfg['mong_doi'], list) and len(cfg['mong_doi']) > 0 and isinstance(cfg['mong_doi'][0], list):
        print("Kết quả mong đợi: \n          " + "\n          ".join(str(x) for x in cfg['mong_doi']))
    else:
        print(f"Kết quả mong đợi: {cfg['mong_doi']}")
        
    if kq == cfg['mong_doi']:
        print("Trạng thái: THÀNH CÔNG")
    else:
        print("Trạng thái: THẤT BẠI")

if __name__ == '__main__':
    try:
        while True:
            print("\n" + "*"*50)
            print(" MENU SELECTION SORT: PHẦN 3 (BÀI 11 - 17) ")
            print(" CHỌN BÀI (11-17) HOẶC 0 ĐỂ THOÁT | 'all' ĐỂ CHẠY HẾT")
            print("*"*50)
            for k, v in Noidung.items():
                print(f" {k:>6}. {v['ten']}")
            chon = input("\nLựa chọn: ").strip()
            
            if chon == '0':
                break
            elif chon.lower() == 'all':
                for cfg in Noidung.values():
                    chay_bai(cfg)
            elif chon in Noidung:
                chay_bai(Noidung[chon])
            else:
                print("Lựa chọn không hợp lệ, vui lòng thử lại!")
    except KeyboardInterrupt:
>>>>>>> 49361b57954c8d9e4f813d02dd285d26a9d59c11
        pass