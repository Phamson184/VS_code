from typing import List

def tim_kiem(a: List[int], x: int) -> int:
    trai, phai = 0, len(a) - 1
    while trai <= phai:
        giua = (trai + phai) // 2
        if a[giua] == x:
            return giua
        elif a[giua] < x:
            trai = giua + 1
        else:
            phai = giua - 1
    return -1

def ton_tai(a: List[int], x: int) -> bool:
    return tim_kiem(a, x) != -1

def vi_tri_dau(a: List[int], x: int) -> int:
    trai, phai, kq = 0, len(a) - 1, -1
    while trai <= phai:
        giua = (trai + phai) // 2
        if a[giua] == x:
            kq = giua
            phai = giua - 1
        elif a[giua] < x:
            trai = giua + 1
        else:
            phai = giua - 1
    return kq

def vi_tri_cuoi(a: List[int], x: int) -> int:
    trai, phai, kq = 0, len(a) - 1, -1
    while trai <= phai:
        giua = (trai + phai) // 2
        if a[giua] == x:
            kq = giua
            trai = giua + 1
        elif a[giua] < x:
            trai = giua + 1
        else:
            phai = giua - 1
    return kq

def dem_xuat_hien(a: List[int], x: int) -> int:
    dau = vi_tri_dau(a, x)
    if dau == -1:
        return 0
    return vi_tri_cuoi(a, x) - dau + 1

def lower_bound(a: List[int], x: int) -> int:
    trai, phai = 0, len(a)
    while trai < phai:
        giua = (trai + phai) // 2
        if a[giua] < x:
            trai = giua + 1
        else:
            phai = giua
    return trai

def upper_bound(a: List[int], x: int) -> int:
    trai, phai = 0, len(a)
    while trai < phai:
        giua = (trai + phai) // 2
        if a[giua] <= x:
            trai = giua + 1
        else:
            phai = giua
    return trai

def can_bac_hai(n: int) -> int:
    if n < 2:
        return n
    trai, phai = 1, n // 2
    while trai <= phai:
        giua = (trai + phai) // 2
        if giua * giua == n:
            return giua
        elif giua * giua < n:
            trai = giua + 1
        else:
            phai = giua - 1
    return phai

def vi_tri_chen(a: List[int], x: int) -> int:
    trai, phai = 0, len(a)
    while trai < phai:
        giua = (trai + phai) // 2
        if a[giua] < x:
            trai = giua + 1
        else:
            phai = giua
    return trai

Noidung = {
    '1': {
        'ten': 'BÀI 1: TÌM KIẾM CƠ BẢN',
        'du_lieu': {'a': [1, 3, 5, 7, 9], 'x': 7},
        'mong_doi': 3,
        'ham': lambda d: tim_kiem(d['a'], d['x']),
        'format': lambda d, kq: (
            f"Mảng: {d['a']}, x={d['x']}\n"
            f"=> Tìm thấy tại chỉ số {kq}" if kq != -1
            else f"Mảng: {d['a']}, x={d['x']}\n=> Không tìm thấy"
        ),
    },
    '2': {
        'ten': 'BÀI 2: KIỂM TRA TỒN TẠI',
        'du_lieu': {'a': [2, 4, 6, 8], 'x': 5},
        'mong_doi': False,
        'ham': lambda d: ton_tai(d['a'], d['x']),
        'format': lambda d, kq: (
            f"Mảng: {d['a']}, x={d['x']}\n"
            f"=> {'Tồn tại' if kq else 'Không tồn tại'}"
        ),
    },
    '3': {
        'ten': 'BÀI 3: VỊ TRÍ XUẤT HIỆN ĐẦU TIÊN',
        'du_lieu': {'a': [1, 2, 2, 2, 3], 'x': 2},
        'mong_doi': 1,
        'ham': lambda d: vi_tri_dau(d['a'], d['x']),
        'format': lambda d, kq: (
            f"Mảng: {d['a']}, x={d['x']}\n"
            f"=> Vị trí đầu tiên: {kq}"
        ),
    },
    '4': {
        'ten': 'BÀI 4: VỊ TRÍ XUẤT HIỆN CUỐI CÙNG',
        'du_lieu': {'a': [1, 2, 2, 2, 3], 'x': 2},
        'mong_doi': 3,
        'ham': lambda d: vi_tri_cuoi(d['a'], d['x']),
        'format': lambda d, kq: (
            f"Mảng: {d['a']}, x={d['x']}\n"
            f"=> Vị trí cuối cùng: {kq}"
        ),
    },
    '5': {
        'ten': 'BÀI 5: ĐẾM SỐ LẦN XUẤT HIỆN',
        'du_lieu': {'a': [1, 2, 2, 2, 3], 'x': 2},
        'mong_doi': 3,
        'ham': lambda d: dem_xuat_hien(d['a'], d['x']),
        'format': lambda d, kq: (
            f"Mảng: {d['a']}, x={d['x']}\n"
            f"=> Xuất hiện {kq} lần"
        ),
    },
    '6': {
        'ten': 'BÀI 6: LOWER BOUND',
        'du_lieu': {'a': [1, 3, 5, 7], 'x': 4},
        'mong_doi': 2,
        'ham': lambda d: lower_bound(d['a'], d['x']),
        'format': lambda d, kq: (
            f"Mảng: {d['a']}, x={d['x']}\n"
            f"=> Chỉ số phần tử nhỏ nhất >= x: {kq} (giá trị: {d['a'][kq] if kq < len(d['a']) else 'không có'})"
        ),
    },
    '7': {
        'ten': 'BÀI 7: UPPER BOUND',
        'du_lieu': {'a': [1, 3, 5, 7], 'x': 5},
        'mong_doi': 3,
        'ham': lambda d: upper_bound(d['a'], d['x']),
        'format': lambda d, kq: (
            f"Mảng: {d['a']}, x={d['x']}\n"
            f"=> Chỉ số phần tử nhỏ nhất > x: {kq} (giá trị: {d['a'][kq] if kq < len(d['a']) else 'không có'})"
        ),
    },
    '8': {
        'ten': 'BÀI 8: CĂN BẬC HAI NGUYÊN',
        'du_lieu': {'n': 8},
        'mong_doi': 2,
        'ham': lambda d: can_bac_hai(d['n']),
        'format': lambda d, kq: (
            f"n={d['n']}\n=> floor(sqrt({d['n']})) = {kq}"
        ),
    },
    '9': {
        'ten': 'BÀI 9: VỊ TRÍ CHÈN',
        'du_lieu': {'a': [1, 3, 5, 6], 'x': 4},
        'mong_doi': 2,
        'ham': lambda d: vi_tri_chen(d['a'], d['x']),
        'format': lambda d, kq: (
            f"Mảng: {d['a']}, x={d['x']}\n"
            f"=> Nên chèn vào chỉ số {kq}"
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
