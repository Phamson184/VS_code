import random 
from dataclasses import dataclass
#bài1
def tuyen_tinh1(ar,x):
    for i,a in enumerate(ar):
        if a==x:
            return i
    return -1

def main1():
    print("bài1: Tìm kiếm tuyến tính")
    n=15
    ar = [random.randint(-100,100) for _ in range(n)]
    print(f'Mảng ngẫu nhiên:')
    print(ar)
    x=int(input('Nhập giá trị x cần tìm: '))
    mot=tuyen_tinh1(ar,x)
    if mot!=-1:
        print(f'Tìm thấy {x} tại vị trí {mot}')
    else:
        print(f' Không tìm thấy {x}')
#bài2
@dataclass
class Sach:
    ma:str
    ten:str
    gia:int
def tuyen_tinh2(ds,x):
    for i,sach in enumerate(ds):
        if sach.ma==x:
            return i
    return -1
def main2():
    print('Bài2: Tìm Sách')
    ds=[
        Sach("S01", "Toan roi rac", 120000),
        Sach("S02", "Cau truc du lieu", 85000),
        Sach("S03", "Lap trinh Python", 150000),
        Sach("S04", "Co so du lieu", 95000),
        Sach("S05", "Tri tue nhan tao", 220000)
    ]
    print('Các loại sách hiện có:')
    for sach in ds:
        print(f' Mã: {sach.ma:<5}|Tên: {sach.ten:<20}|Giá: {sach.gia}')
    x=input('Nhập mã sách x cần tìm:').strip()
    a=tuyen_tinh2(ds,x)
    if a!=-1:
        print(f"Tìm thấy sách: '{ds[a].ten}'")
    else:
        print(f"Không tìm thấy mã {x}")
    
    g=int(input('Nhập mức giá G để lọc sách'))
    high=[s for s in ds if s.gia>g]
    print(f"các sách cso > {g}:")
    if high:
        for sach in high:
            print(f" {sach.ten}-(Giá: {sach.gia})")
    else:
        print("- không có cuốn sách nào")
    
    if ds:
        sach_max=max(ds,key=lambda s:s.gia)
        print(f"Sách có giá trị lớn nhất là: '{sach_max.ten}'với giá '{sach_max.gia}'")
if __name__=='__main__':
    main1()
    main2()