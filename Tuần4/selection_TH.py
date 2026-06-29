<<<<<<< HEAD
from typing import List

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
        'ten': 'CÂU B: SELECTION SORT CƠ BẢN',
        'du_lieu': {'a': [260, 95, 40, 49, 35, 45, 36, 18]},
        'mong_doi': [18, 35, 36, 40, 45, 49, 95, 260],
        'ham': lambda d: sap_xep_chon(d['a']),
        'format': lambda d, kq: f"Mảng gốc:   {d['a']}\nSau sắp xếp: {kq}",
    },
    '2': {
        'ten': 'THỰC HÀNH 03.1 & 03.2: SELECTION SORT',
        'du_lieu': {'a': [-25, 40, 0, 15, -90, 80, -92, -210, 747, 500, 1050, 999]},
        'mong_doi': [-210, -92, -90, -25, 0, 15, 40, 80, 500, 747, 999, 1050],
        'ham': lambda d: sap_xep_chon(d['a']),
        'format': lambda d, kq: f"Mảng gốc:   {d['a']}\nSau sắp xếp: {kq}",
    },
    '3': {
        'ten': 'THỰC HÀNH 03.3: SELECTION SORT DÙNG POP & INSERT',
        'du_lieu': {'a': [64, 34, 25, 5, 22, 11, 90, 12, -15, -50, 100]},
        'mong_doi': [-50, -15, 5, 11, 12, 22, 25, 34, 64, 90, 100],
        'ham': lambda d: chon_dung_pop_insert(d['a']),
        'format': lambda d, kq: f"Mảng gốc:   {d['a']}\nSau sắp xếp: {kq}",
    },
    '4': {
        'ten': 'THỰC HÀNH 03.4: SELECTION SORT MẢNG CHUỖI',
        'du_lieu': {'a': ['cam', 'tao', 'xoai', 'buoi', 'le']},
        'mong_doi': ['buoi', 'cam', 'le', 'tao', 'xoai'],
        'ham': lambda d: sap_xep_chuoi(d['a']),
        'format': lambda d, kq: f"Mảng gốc:   {d['a']}\nSau sắp xếp: {kq}",
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
            print(" MENU: SELECTION SORT ")
            print(" CHỌN BÀI (1-4) HOẶC 0 ĐỂ THOÁT | 'all' ĐỂ CHẠY HẾT")
            print("*"*50)
            for k, v in Noidung.items():
                print(f" {k}. {v['ten']}")
            chon = input("\nLựa chọn: ").strip()
            
            if chon == '0':
                break
            elif chon.lower() == 'all':
                for cfg in Noidung.values():
                    chay_bai(cfg)
            elif chon in Noidung:
                chay_bai(Noidung[chon])
            else:
                print("Lựa chọn không hợp lệ!")
    except KeyboardInterrupt:
=======
from typing import List

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
        'ten': 'CÂU B: SELECTION SORT CƠ BẢN',
        'du_lieu': {'a': [260, 95, 40, 49, 35, 45, 36, 18]},
        'mong_doi': [18, 35, 36, 40, 45, 49, 95, 260],
        'ham': lambda d: sap_xep_chon(d['a']),
        'format': lambda d, kq: f"Mảng gốc:   {d['a']}\nSau sắp xếp: {kq}",
    },
    '2': {
        'ten': 'THỰC HÀNH 03.1 & 03.2: SELECTION SORT',
        'du_lieu': {'a': [-25, 40, 0, 15, -90, 80, -92, -210, 747, 500, 1050, 999]},
        'mong_doi': [-210, -92, -90, -25, 0, 15, 40, 80, 500, 747, 999, 1050],
        'ham': lambda d: sap_xep_chon(d['a']),
        'format': lambda d, kq: f"Mảng gốc:   {d['a']}\nSau sắp xếp: {kq}",
    },
    '3': {
        'ten': 'THỰC HÀNH 03.3: SELECTION SORT DÙNG POP & INSERT',
        'du_lieu': {'a': [64, 34, 25, 5, 22, 11, 90, 12, -15, -50, 100]},
        'mong_doi': [-50, -15, 5, 11, 12, 22, 25, 34, 64, 90, 100],
        'ham': lambda d: chon_dung_pop_insert(d['a']),
        'format': lambda d, kq: f"Mảng gốc:   {d['a']}\nSau sắp xếp: {kq}",
    },
    '4': {
        'ten': 'THỰC HÀNH 03.4: SELECTION SORT MẢNG CHUỖI',
        'du_lieu': {'a': ['cam', 'tao', 'xoai', 'buoi', 'le']},
        'mong_doi': ['buoi', 'cam', 'le', 'tao', 'xoai'],
        'ham': lambda d: sap_xep_chuoi(d['a']),
        'format': lambda d, kq: f"Mảng gốc:   {d['a']}\nSau sắp xếp: {kq}",
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
            print(" MENU: SELECTION SORT ")
            print(" CHỌN BÀI (1-4) HOẶC 0 ĐỂ THOÁT | 'all' ĐỂ CHẠY HẾT")
            print("*"*50)
            for k, v in Noidung.items():
                print(f" {k}. {v['ten']}")
            chon = input("\nLựa chọn: ").strip()
            
            if chon == '0':
                break
            elif chon.lower() == 'all':
                for cfg in Noidung.values():
                    chay_bai(cfg)
            elif chon in Noidung:
                chay_bai(Noidung[chon])
            else:
                print("Lựa chọn không hợp lệ!")
    except KeyboardInterrupt:
>>>>>>> 49361b57954c8d9e4f813d02dd285d26a9d59c11
        pass