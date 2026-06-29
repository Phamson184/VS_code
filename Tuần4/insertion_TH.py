<<<<<<< HEAD
from typing import List

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

Noidung = {
    '1': {
        'ten': 'THỰC HÀNH 02.1 & 02.2: INSERTION SORT',
        'du_lieu': {'a': [12, 11, 13, 58, 6, 90, 55]},
        'mong_doi': [6, 11, 12, 13, 55, 58, 90],
        'ham': lambda d: sap_xep_chen(d['a']),
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
            print(" MENU: INSERTION SORT ")
            print(" CHỌN BÀI (1) HOẶC 0 ĐỂ THOÁT | 'all' ĐỂ CHẠY HẾT")
            print("*"*50)
            for k, v in Noidung.items():
                print(f" {k}. {v['ten']}")
            chon = input("\nLựa chọn: ").strip()
            
            if chon == '0':
                break
            elif chon.lower() == 'all' or chon == '1':
                chay_bai(Noidung['1'])
            else:
                print("Lựa chọn không hợp lệ!")
    except KeyboardInterrupt:
=======
from typing import List

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

Noidung = {
    '1': {
        'ten': 'THỰC HÀNH 02.1 & 02.2: INSERTION SORT',
        'du_lieu': {'a': [12, 11, 13, 58, 6, 90, 55]},
        'mong_doi': [6, 11, 12, 13, 55, 58, 90],
        'ham': lambda d: sap_xep_chen(d['a']),
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
            print(" MENU: INSERTION SORT ")
            print(" CHỌN BÀI (1) HOẶC 0 ĐỂ THOÁT | 'all' ĐỂ CHẠY HẾT")
            print("*"*50)
            for k, v in Noidung.items():
                print(f" {k}. {v['ten']}")
            chon = input("\nLựa chọn: ").strip()
            
            if chon == '0':
                break
            elif chon.lower() == 'all' or chon == '1':
                chay_bai(Noidung['1'])
            else:
                print("Lựa chọn không hợp lệ!")
    except KeyboardInterrupt:
>>>>>>> 49361b57954c8d9e4f813d02dd285d26a9d59c11
        pass