from typing import List

def noi_bot_co_ban(a: List[int]) -> List[int]:
    b = a[:]
    n = len(b)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if b[j] > b[j + 1]:
                b[j], b[j + 1] = b[j + 1], b[j]
    return b

def sap_xep_chon(a: List[int]) -> List[int]:
    b = a[:]
    n = len(b)
    for i in range(n):
        vt_min = i
        for j in range(i + 1, n):
            if b[j] < b[vt_min]:
                vt_min = j
        b[i], b[vt_min] = b[vt_min], b[i]
    return b

def noi_bot_toi_uu(a: List[int]) -> List[int]:
    b = a[:]
    n = len(b)
    for i in range(n - 1):
        da_doi_cho = False
        for j in range(0, n - i - 1):
            if b[j] > b[j + 1]:
                da_doi_cho = True
                b[j], b[j + 1] = b[j + 1], b[j]
        if not da_doi_cho:
            break
    return b

def noi_bot_dung_temp(a: List[int]) -> List[int]:
    b = a[:]
    n = len(b)
    for i in range(n):
        for j in range(0, n - i - 1):
            if b[j] > b[j + 1]:
                bien_tam = b[j]
                b[j] = b[j + 1]
                b[j + 1] = bien_tam
    return b

def noi_bot_giam_dan(a: List[int]) -> List[int]:
    b = a[:]
    n = len(b)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if b[j] < b[j + 1]:
                b[j], b[j + 1] = b[j + 1], b[j]
    return b

def sap_xep_chen(a: List[int]) -> List[int]:
    b = a[:]
    n = len(b)
    if n <= 1:
        return b
    for i in range(1, n):
        gia_tri_chen = b[i]
        j = i - 1
        while j >= 0 and gia_tri_chen < b[j]:
            b[j + 1] = b[j]
            j -= 1
        b[j + 1] = gia_tri_chen
    return b

def chon_dung_pop_insert(a: List[int]) -> List[int]:
    b = a[:]
    n = len(b)
    for i in range(n - 1):
        vt_min = i
        for j in range(i + 1, n):
            if b[j] < b[vt_min]:
                vt_min = j
        gt_nho_nhat = b.pop(vt_min)
        b.insert(i, gt_nho_nhat)
    return b

def sap_xep_chuoi(a: List[str]) -> List[str]:
    b = a[:]
    n = len(b)
    for i in range(n):
        vt_min = i
        for j in range(i + 1, n):
            if b[j] < b[vt_min]:
                vt_min = j
        b[i], b[vt_min] = b[vt_min], b[i]
    return b


Noidung = {
    '1': {
        'ten': 'CÂU A: BUBBLE SORT CƠ BẢN',
        'du_lieu': {'a': [400, 250, 30, 55]},
        'mong_doi': [30, 55, 250, 400],
        'ham': lambda d: noi_bot_co_ban(d['a']),
        'format': lambda d, kq: (
            f"Mảng gốc:   {d['a']}\n"
            f"Sau sắp xếp: {kq}"
        ),
    },
    '2': {
        'ten': 'CÂU B: SELECTION SORT CƠ BẢN',
        'du_lieu': {'a': [260, 95, 40, 49, 35, 45, 36, 18]},
        'mong_doi': [18, 35, 36, 40, 45, 49, 95, 260],
        'ham': lambda d: sap_xep_chon(d['a']),
        'format': lambda d, kq: (
            f"Mảng gốc:   {d['a']}\n"
            f"Sau sắp xếp: {kq}"
        ),
    },
    '3': {
        'ten': 'THỰC HÀNH 01.1: BUBBLE SORT',
        'du_lieu': {'a': [120, 35, 60, 42, 280, 7, 15, 19]},
        'mong_doi': [7, 15, 19, 35, 42, 60, 120, 280],
        'ham': lambda d: noi_bot_co_ban(d['a']),
        'format': lambda d, kq: (
            f"Mảng gốc:   {d['a']}\n"
            f"Sau sắp xếp: {kq}"
        ),
    },
    '4': {
        'ten': 'THỰC HÀNH 01.2: BUBBLE SORT TỐI ƯU (CỜ ĐÃ ĐỔI CHỖ)',
        'du_lieu': {'a': [60, 32, 15, 12, 52, 71, 90, -1, -10, -30, -155, 75]},
        'mong_doi': [-155, -30, -10, -1, 12, 15, 32, 52, 60, 71, 75, 90],
        'ham': lambda d: noi_bot_toi_uu(d['a']),
        'format': lambda d, kq: (
            f"Mảng gốc:   {d['a']}\n"
            f"Sau sắp xếp: {kq}"
        ),
    },
    '5': {
        'ten': 'THỰC HÀNH 01.3: BUBBLE SORT DÙNG BIẾN TẠM (TEMP)',
        'du_lieu': {'a': [25, 17, 7, 14, 6, 3, 100, -2, -10, -50]},
        'mong_doi': [-50, -10, -2, 3, 6, 7, 14, 17, 25, 100],
        'ham': lambda d: noi_bot_dung_temp(d['a']),
        'format': lambda d, kq: (
            f"Mảng gốc:   {d['a']}\n"
            f"Sau sắp xếp: {kq}"
        ),
    },
    '6': {
        'ten': 'THỰC HÀNH 01.4: BUBBLE SORT GIẢM DẦN',
        'du_lieu': {'a': [25, 17, 7, 14, 6, 3, 100, -2, -10, -50]},
        'mong_doi': [100, 25, 17, 14, 7, 6, 3, -2, -10, -50],
        'ham': lambda d: noi_bot_giam_dan(d['a']),
        'format': lambda d, kq: (
            f"Mảng gốc: {d['a']}\n"
            f"Giảm dần:  {kq}"
        ),
    },
    '7': {
        'ten': 'THỰC HÀNH 02.1 & 02.2: INSERTION SORT',
        'du_lieu': {'a': [12, 11, 13, 58, 6, 90, 55]},
        'mong_doi': [6, 11, 12, 13, 55, 58, 90],
        'ham': lambda d: sap_xep_chen(d['a']),
        'format': lambda d, kq: (
            f"Mảng gốc:   {d['a']}\n"
            f"Sau sắp xếp: {kq}"
        ),
    },
    '8': {
        'ten': 'THỰC HÀNH 03.1 & 03.2: SELECTION SORT',
        'du_lieu': {'a': [-25, 40, 0, 15, -90, 80, -92, -210, 747, 500, 1050, 999]},
        'mong_doi': [-210, -92, -90, -25, 0, 15, 40, 80, 500, 747, 999, 1050],
        'ham': lambda d: sap_xep_chon(d['a']),
        'format': lambda d, kq: (
            f"Mảng gốc:   {d['a']}\n"
            f"Sau sắp xếp: {kq}"
        ),
    },
    '9': {
        'ten': 'THỰC HÀNH 03.3: SELECTION SORT DÙNG POP & INSERT',
        'du_lieu': {'a': [64, 34, 25, 5, 22, 11, 90, 12, -15, -50, 100]},
        'mong_doi': [-50, -15, 5, 11, 12, 22, 25, 34, 64, 90, 100],
        'ham': lambda d: chon_dung_pop_insert(d['a']),
        'format': lambda d, kq: (
            f"Mảng gốc:   {d['a']}\n"
            f"Sau sắp xếp: {kq}"
        ),
    },
    '10': {
        'ten': 'THỰC HÀNH 03.4: SELECTION SORT MẢNG CHUỖI',
        'du_lieu': {'a': ['cam', 'tao', 'xoai', 'buoi', 'le']},
        'mong_doi': ['buoi', 'cam', 'le', 'tao', 'xoai'],
        'ham': lambda d: sap_xep_chuoi(d['a']),
        'format': lambda d, kq: (
            f"Mảng gốc:   {d['a']}\n"
            f"Sau sắp xếp: {kq}"
        ),
    }
}

def chay_bai(cfg):
    print(f"\n{'='*50}\n {cfg['ten']}\n{'='*50}")
    kq = cfg['ham'](cfg['du_lieu'])
    print(cfg['format'](cfg['du_lieu'], kq))
    print(f"Kết quả mong đợi: {cfg['mong_doi']}")
    if kq == cfg['mong_doi']:
        print("Trạng thái: THÀNH CÔNG")
    else:
        print("Trạng thái: THẤT BẠI")

if __name__ == '__main__':
    try:
        while True:
            print("\n" + "*"*50)
            print(" CHỌN BÀI (1-10) HOẶC 0 ĐỂ THOÁT | 'all' ĐỂ CHẠY HẾT")
            print("*"*50)
            for k, v in Noidung.items():
                print(f" {k}. {v['ten']}")
            chon = input("\nLựa chọn: ").strip()
            
            if chon == '0':
                print("Đã thoát.")
                break
            elif chon.lower() == 'all':
                for cfg in Noidung.values():
                    chay_bai(cfg)
            elif chon in Noidung:
                chay_bai(Noidung[chon])
            else:
                print("Lựa chọn không hợp lệ, vui lòng thử lại!")
    except KeyboardInterrupt:
        print("\n\nĐã dừng chương trình an toàn. Hẹn gặp lại!")