from typing import List, Tuple

def dem_luot(a: List[int]) -> int:
    b, so_luot = a[:], 0
    n = len(b)
    for i in range(n - 1):
        da_swap = False
        for j in range(n - 1 - i):
            if b[j] > b[j + 1]:
                b[j], b[j + 1] = b[j + 1], b[j]
                da_swap = True
        so_luot += 1
        if not da_swap:
            break
    return so_luot

def sap_tri_tuyet_doi(a: List[int]) -> List[int]:
    b = a[:]
    n = len(b)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if abs(b[j]) > abs(b[j + 1]):
                b[j], b[j + 1] = b[j + 1], b[j]
    return b

def sap_chuoi_do_dai(a: List[str]) -> List[str]:
    b = a[:]
    n = len(b)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if len(b[j]) > len(b[j + 1]):
                b[j], b[j + 1] = b[j + 1], b[j]
    return b

def on_dinh(a: List[Tuple]) -> List[Tuple]:
    b = a[:]
    n = len(b)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if b[j][0] > b[j + 1][0]:
                b[j], b[j + 1] = b[j + 1], b[j]
    return b

def cocktail(a: List[int]) -> Tuple[List[int], int]:
    b, so_luot = a[:], 0
    trai, phai = 0, len(b) - 1
    while trai < phai:
        da_swap = False
        for i in range(trai, phai):
            if b[i] > b[i + 1]:
                b[i], b[i + 1] = b[i + 1], b[i]
                da_swap = True
        phai -= 1
        for i in range(phai, trai, -1):
            if b[i] < b[i - 1]:
                b[i], b[i - 1] = b[i - 1], b[i]
                da_swap = True
        trai += 1
        so_luot += 1
        if not da_swap:
            break
    return b, so_luot

def nhieu_khoa(ds: List[Tuple]) -> List[Tuple]:
    b = ds[:]
    n = len(b)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            ten_j, diem_j = b[j]
            ten_j1, diem_j1 = b[j + 1]
            if diem_j < diem_j1 or (diem_j == diem_j1 and ten_j > ten_j1):
                b[j], b[j + 1] = b[j + 1], b[j]
    return b

def nghich_the_va_swap(a: List[int]) -> Tuple[int, int]:
    nghich_the = sum(
        1 for i in range(len(a)) for j in range(i + 1, len(a)) if a[i] > a[j]
    )
    b, so_swap = a[:], 0
    n = len(b)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if b[j] > b[j + 1]:
                b[j], b[j + 1] = b[j + 1], b[j]
                so_swap += 1
    return nghich_the, so_swap

def k_lon_nhat(a: List[int], k: int) -> List[int]:
    b = a[:]
    n = len(b)
    for i in range(k):
        for j in range(n - 1 - i):
            if b[j] > b[j + 1]:
                b[j], b[j + 1] = b[j + 1], b[j]
    return b

class Node:
    def __init__(self, val):
        self.val = val
        self.ke = None

def tao_danh_sach(ds: List[int]) -> Node:
    dau = Node(ds[0])
    hien_tai = dau
    for v in ds[1:]:
        hien_tai.ke = Node(v)
        hien_tai = hien_tai.ke
    return dau

def in_danh_sach(dau: Node) -> List[int]:
    kq, hien_tai = [], dau
    while hien_tai:
        kq.append(hien_tai.val)
        hien_tai = hien_tai.ke
    return kq

def bubble_linked_list(dau: Node) -> Node:
    if not dau:
        return dau
    da_swap = True
    while da_swap:
        da_swap = False
        hien_tai = dau
        while hien_tai.ke:
            if hien_tai.val > hien_tai.ke.val:
                hien_tai.val, hien_tai.ke.val = hien_tai.ke.val, hien_tai.val
                da_swap = True
            hien_tai = hien_tai.ke
    return dau

Noidung = {
    '10': {
        'ten': 'BÀI 10: ĐẾM SỐ LƯỢT CẦN THIẾT',
        'du_lieu': {'a': [2, 1, 3, 4]},
        'mong_doi': 2,
        'ham': lambda d: dem_luot(d['a']),
        'format': lambda d, kq: (
            f"Mảng: {d['a']}\n"
            f"=> Số lượt cần thiết: {kq}"
        ),
    },
    '11': {
        'ten': 'BÀI 11: SẮP XẾP THEO TRỊ TUYỆT ĐỐI',
        'du_lieu': {'a': [-3, 1, -2, 2]},
        'mong_doi': [1, -2, 2, -3],
        'ham': lambda d: sap_tri_tuyet_doi(d['a']),
        'format': lambda d, kq: (
            f"Mảng gốc: {d['a']}\n"
            f"Theo |a[i]|: {kq}"
        ),
    },
    '12': {
        'ten': 'BÀI 12: SẮP XẾP CHUỖI THEO ĐỘ DÀI',
        'du_lieu': {'a': ['abc', 'a', 'ab']},
        'mong_doi': ['a', 'ab', 'abc'],
        'ham': lambda d: sap_chuoi_do_dai(d['a']),
        'format': lambda d, kq: (
            f"Mảng gốc: {d['a']}\n"
            f"Theo độ dài: {kq}"
        ),
    },
    '13': {
        'ten': 'BÀI 13: TÍNH ỔN ĐỊNH (STABILITY)',
        'du_lieu': {'a': [(2, 'a'), (1, 'b'), (2, 'c')]},
        'mong_doi': [(1, 'b'), (2, 'a'), (2, 'c')],
        'ham': lambda d: on_dinh(d['a']),
        'format': lambda d, kq: (
            f"Mảng gốc: {d['a']}\n"
            f"Sau sort:  {kq}\n"
            f"=> (2,'a') vẫn trước (2,'c') → ổn định: {kq.index((2,'a')) < kq.index((2,'c'))}"
        ),
    },
    '14': {
        'ten': 'BÀI 14: COCKTAIL SHAKER SORT',
        'du_lieu': {'a': [5, 1, 4, 2, 8]},
        'mong_doi': [1, 2, 4, 5, 8],
        'ham': lambda d: cocktail(d['a']),
        'format': lambda d, kq: (
            f"Mảng gốc: {d['a']}\n"
            f"Sau sort:  {kq[0]}\n"
            f"=> Số lượt cocktail: {kq[1]} | Bubble thường: {dem_luot(d['a'])} lượt"
        ),
    },
    '15': {
        'ten': 'BÀI 15: SẮP XẾP THEO NHIỀU KHÓA',
        'du_lieu': {'ds': [('An', 8), ('Ba', 9), ('Cu', 8)]},
        'mong_doi': [('Ba', 9), ('An', 8), ('Cu', 8)],
        'ham': lambda d: nhieu_khoa(d['ds']),
        'format': lambda d, kq: (
            f"Danh sách gốc: {d['ds']}\n"
            f"Sau sort (điểm giảm, tên tăng): {kq}"
        ),
    },
    '16': {
        'ten': 'BÀI 16: SỐ NGHỊCH THẾ = SỐ SWAP',
        'du_lieu': {'a': [2, 3, 1]},
        'mong_doi': 2,
        'ham': lambda d: nghich_the_va_swap(d['a']),
        'format': lambda d, kq: (
            f"Mảng: {d['a']}\n"
            f"=> Số nghịch thế: {kq[0]} | Số swap thực tế: {kq[1]}\n"
            f"=> Bằng nhau: {kq[0] == kq[1]}"
        ),
    },
    '17': {
        'ten': 'BÀI 17: SẮP XẾP MỘT PHẦN (K PHẦN TỬ LỚN NHẤT)',
        'du_lieu': {'a': [3, 1, 4, 1, 5], 'k': 2},
        'mong_doi': [1, 1, 3, 4, 5],
        'ham': lambda d: k_lon_nhat(d['a'], d['k']),
        'format': lambda d, kq: (
            f"Mảng: {d['a']}, k={d['k']}\n"
            f"Sau {d['k']} lượt: {kq}\n"
            f"=> {d['k']} phần tử lớn nhất cuối mảng: {kq[-d['k']:]}"
        ),
    },
    '18': {
        'ten': 'BÀI 18: BUBBLE SORT TRÊN DANH SÁCH LIÊN KẾT',
        'du_lieu': {'ds': [1, 3, 2]},
        'mong_doi': [1, 2, 3],
        'ham': lambda d: in_danh_sach(bubble_linked_list(tao_danh_sach(d['ds']))),
        'format': lambda d, kq: (
            f"Danh sách gốc: {' -> '.join(map(str, d['ds']))} -> null\n"
            f"Sau sort:      {' -> '.join(map(str, kq))} -> null"
        ),
    },
}

def chay_bai(cfg):
    print(f"\n{'='*50}\n {cfg['ten']}\n{'='*50}")
    kq = cfg['ham'](cfg['du_lieu'])
    print(cfg['format'](cfg['du_lieu'], kq))
    print(f"Kết quả mong đợi: {cfg['mong_doi']}")

if __name__ == '__main__':
    while True:
        print("\n" + "*"*50)
        print(" CHỌN BÀI (10-18) HOẶC 0 ĐỂ THOÁT | 'all' ĐỂ CHẠY HẾT")
        print("*"*50)
        for k, v in Noidung.items():
            print(f" {k}. {v['ten']}")
        chon = input("\nLựa chọn: ").strip()
        if chon == '0':
            print("Đã thoát.")
            break
        elif chon == 'all':
            for cfg in Noidung.values():
                chay_bai(cfg)
        elif chon in Noidung:
            chay_bai(Noidung[chon])
        else:
            print("Không hợp lệ, thử lại!")
