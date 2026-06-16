from typing import List

def noi_bot_co_ban(a: List[int]) -> List[int]:
    b = a[:]
    n = len(b)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if b[j] > b[j + 1]:
                b[j], b[j + 1] = b[j + 1], b[j]
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

Noidung = {
    '1': {
        'ten': 'CÂU A: BUBBLE SORT CƠ BẢN',
        'du_lieu': {'a': [400, 250, 30, 55]},
        'mong_doi': [30, 55, 250, 400],
        'ham': lambda d: noi_bot_co_ban(d['a']),
        'format': lambda d, kq: f"Mảng gốc:   {d['a']}\nSau sắp xếp: {kq}",
    },
    '2': {
        'ten': 'THỰC HÀNH 01.1: BUBBLE SORT',
        'du_lieu': {'a': [120, 35, 60, 42, 280, 7, 15, 19]},
        'mong_doi': [7, 15, 19, 35, 42, 60, 120, 280],
        'ham': lambda d: noi_bot_co_ban(d['a']),
        'format': lambda d, kq: f"Mảng gốc:   {d['a']}\nSau sắp xếp: {kq}",
    },
    '3': {
        'ten': 'THỰC HÀNH 01.2: BUBBLE SORT TỐI ƯU',
        'du_lieu': {'a': [60, 32, 15, 12, 52, 71, 90, -1, -10, -30, -155, 75]},
        'mong_doi': [-155, -30, -10, -1, 12, 15, 32, 52, 60, 71, 75, 90],
        'ham': lambda d: noi_bot_toi_uu(d['a']),
        'format': lambda d, kq: f"Mảng gốc:   {d['a']}\nSau sắp xếp: {kq}",
    },
    '4': {
        'ten': 'THỰC HÀNH 01.3: BUBBLE SORT DÙNG BIẾN TẠM',
        'du_lieu': {'a': [25, 17, 7, 14, 6, 3, 100, -2, -10, -50]},
        'mong_doi': [-50, -10, -2, 3, 6, 7, 14, 17, 25, 100],
        'ham': lambda d: noi_bot_dung_temp(d['a']),
        'format': lambda d, kq: f"Mảng gốc:   {d['a']}\nSau sắp xếp: {kq}",
    },
    '5': {
        'ten': 'THỰC HÀNH 01.4: BUBBLE SORT GIẢM DẦN',
        'du_lieu': {'a': [25, 17, 7, 14, 6, 3, 100, -2, -10, -50]},
        'mong_doi': [100, 25, 17, 14, 7, 6, 3, -2, -10, -50],
        'ham': lambda d: noi_bot_giam_dan(d['a']),
        'format': lambda d, kq: f"Mảng gốc: {d['a']}\nGiảm dần:  {kq}",
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
            print(" MENU: BUBBLE SORT ")
            print(" CHỌN BÀI (1-5) HOẶC 0 ĐỂ THOÁT | 'all' ĐỂ CHẠY HẾT")
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
<<<<<<< HEAD
        pass
=======
        pass
>>>>>>> 54b73f1f0efd8c94226d82a1874594e5ef3789c8
