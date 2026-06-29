from typing import List

def mot_luot(a: List[int]) -> List[int]:
    b = a[:]
    for i in range(len(b) - 1):
        if b[i] > b[i + 1]:
            b[i], b[i + 1] = b[i + 1], b[i]
    return b

def tang_dan(a: List[int]) -> List[int]:
    b = a[:]
    n = len(b)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if b[j] > b[j + 1]:
                b[j], b[j + 1] = b[j + 1], b[j]
    return b

def giam_dan(a: List[int]) -> List[int]:
    b = a[:]
    n = len(b)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if b[j] < b[j + 1]:
                b[j], b[j + 1] = b[j + 1], b[j]
    return b

def dem_swap(a: List[int]) -> int:
    b, so_swap = a[:], 0
    n = len(b)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if b[j] > b[j + 1]:
                b[j], b[j + 1] = b[j + 1], b[j]
                so_swap += 1
    return so_swap

def dem_so_sanh(a: List[int]) -> int:
    b, so_ss = a[:], 0
    n = len(b)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            so_ss += 1
            if b[j] > b[j + 1]:
                b[j], b[j + 1] = b[j + 1], b[j]
    return so_ss

def cuoi_sau_mot_luot(a: List[int]) -> int:
    b = mot_luot(a)
    return b[-1]

def sap_ky_tu(a: List[str]) -> List[str]:
    b = a[:]
    n = len(b)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if b[j] > b[j + 1]:
                b[j], b[j + 1] = b[j + 1], b[j]
    return b

def kiem_tra_k_luot(a: List[int], k: int) -> bool:
    b = a[:]
    n = len(b)
    for i in range(k):
        for j in range(n - 1 - i):
            if b[j] > b[j + 1]:
                b[j], b[j + 1] = b[j + 1], b[j]
    return b == sorted(b)

def toi_uu_early_exit(a: List[int]):
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
    return b, so_luot

Noidung = {
    '1': {
        'ten': 'BÀI 1: THỰC HIỆN MỘT LƯỢT (ONE PASS)',
        'du_lieu': {'a': [5, 1, 4, 2, 8]},
        'mong_doi': [1, 4, 2, 5, 8],
        'ham': lambda d: mot_luot(d['a']),
        'format': lambda d, kq: (
            f"Mảng gốc:  {d['a']}\n"
            f"Sau 1 lượt: {kq}"
        ),
    },
    '2': {
        'ten': 'BÀI 2: SẮP XẾP TĂNG DẦN CƠ BẢN',
        'du_lieu': {'a': [5, 1, 4, 2, 8]},
        'mong_doi': [1, 2, 4, 5, 8],
        'ham': lambda d: tang_dan(d['a']),
        'format': lambda d, kq: (
            f"Mảng gốc: {d['a']}\n"
            f"Tăng dần: {kq}"
        ),
    },
    '3': {
        'ten': 'BÀI 3: SẮP XẾP GIẢM DẦN',
        'du_lieu': {'a': [5, 1, 4, 2, 8]},
        'mong_doi': [8, 5, 4, 2, 1],
        'ham': lambda d: giam_dan(d['a']),
        'format': lambda d, kq: (
            f"Mảng gốc: {d['a']}\n"
            f"Giảm dần: {kq}"
        ),
    },
    '4': {
        'ten': 'BÀI 4: ĐẾM SỐ LẦN HOÁN ĐỔI',
        'du_lieu': {'a': [3, 2, 1]},
        'mong_doi': 3,
        'ham': lambda d: dem_swap(d['a']),
        'format': lambda d, kq: (
            f"Mảng: {d['a']}\n"
            f"=> Số lần hoán đổi: {kq}"
        ),
    },
    '5': {
        'ten': 'BÀI 5: ĐẾM SỐ LẦN SO SÁNH',
        'du_lieu': {'a': [1, 2, 3]},
        'mong_doi': 3,
        'ham': lambda d: dem_so_sanh(d['a']),
        'format': lambda d, kq: (
            f"Mảng: {d['a']}\n"
            f"=> Số lần so sánh: {kq}"
        ),
    },
    '6': {
        'ten': 'BÀI 6: PHẦN TỬ VỀ ĐÚNG CHỖ SAU 1 LƯỢT',
        'du_lieu': {'a': [4, 2, 7, 1, 3]},
        'mong_doi': 7,
        'ham': lambda d: cuoi_sau_mot_luot(d['a']),
        'format': lambda d, kq: (
            f"Mảng: {d['a']}\n"
            f"=> Phần tử cuối sau 1 lượt: {kq}"
        ),
    },
    '7': {
        'ten': 'BÀI 7: SẮP XẾP MẢNG KÝ TỰ',
        'du_lieu': {'a': ['d', 'a', 'c', 'b']},
        'mong_doi': ['a', 'b', 'c', 'd'],
        'ham': lambda d: sap_ky_tu(d['a']),
        'format': lambda d, kq: (
            f"Mảng gốc: {d['a']}\n"
            f"Sau sort:  {kq}"
        ),
    },
    '8': {
        'ten': 'BÀI 8: KIỂM TRA ĐÃ SẮP XẾP SAU K LƯỢT',
        'du_lieu': {'a': [3, 2, 1], 'k': 1},
        'mong_doi': False,
        'ham': lambda d: kiem_tra_k_luot(d['a'], d['k']),
        'format': lambda d, kq: (
            f"Mảng: {d['a']}, k={d['k']} lượt\n"
            f"=> Đã sắp xếp hoàn toàn: {kq}"
        ),
    },
    '9': {
        'ten': 'BÀI 9: BUBBLE SORT TỐI ƯU (EARLY EXIT)',
        'du_lieu': {'a': [1, 2, 3, 4]},
        'mong_doi': 1,
        'ham': lambda d: toi_uu_early_exit(d['a']),
        'format': lambda d, kq: (
            f"Mảng: {d['a']}\n"
            f"Kết quả: {kq[0]}\n"
            f"=> Số lượt chạy: {kq[1]}"
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
        print(" CHỌN BÀI (1-9) HOẶC 0 ĐỂ THOÁT | 'all' ĐỂ CHẠY HẾT")
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
