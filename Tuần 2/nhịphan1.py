import random
def nhi_phan(ar,x,verbose=False):
    trai,phai,buoc=0,len(ar)-1,1
    while trai<=phai:
        mid=(trai+phai)//2
        if verbose:
            print(f"Bước {buoc}: trai={trai},phai={phai}=>mid={mid}.ar[{mid}]={ar[mid]}")
        if ar[mid]==x:
            if verbose: print(f" {ar[mid]}=={x}.Dừng")
            return mid, buoc
        if ar[mid]<x:
            if verbose: print(f"{ar[mid]}<{x}.Tìm nửa phải (trai={mid+1})")
            trai=mid+1
        else:
            if verbose: print(f" {ar[mid]}>{x}.Tìm nửa trái(phai={mid-1})")
            phai=mid-1
        buoc+=1
    return -1,buoc

def nhi_phan_e_rua(ar,x,trai=0,phai=None):
    if phai is None: phai=len(ar)-1
    if phai<trai:return -1
    mid=(trai+phai)//2
    if ar[mid]==x: return mid
    if ar[mid]>x: return nhi_phan_e_rua(ar,x,trai,mid-1)
    return nhi_phan_e_rua(ar,x,mid+1,phai)

Noidung={
    '1': {
        'ten': 'BÀI 2.1: TÌM KIẾM NHỊ PHÂN CƠ BẢN',
        'ar': [0, 4, 5, 9, 13, 15, 18, 24, 28, 29, 35],
        'goi_y': 28,
        'ham': lambda ar, x: nhi_phan(ar, x),
        'format': lambda x, kq: (
            f' => Tìm thấy {x} tại chỉ số {kq[0]}.' if kq[0] != -1
            else f' => Không tìm thấy {x} trong mảng.'
        ),
    },
    '2': {
        'ten': 'BÀI 2.2: NHỊ PHÂN (ĐẾM SỐ BƯỚC LẶP)',
        'ar': [0, 4, 5, 9, 13, 15, 18, 24, 28, 29, 35],
        'goi_y': 40,
        'ham': lambda ar, x: nhi_phan(ar, x),
        'format': lambda x, kq: (
            f' => Tìm thấy {x} tại chỉ số {kq[0]}. Số bước: {kq[1]}'
            if kq[0] != -1
            else f' => Không tìm thấy {x}. Tốn {kq[1]} bước.'
        ),
    },
    '3': {
        'ten': 'BÀI 2.3: NHỊ PHÂN (ĐỆ QUY)',
        'ar': [1, 3, 9, 10, 40, 52, 55, 180, 250, 350],
        'goi_y': 250,
        'ham': lambda ar, x: nhi_phan_e_rua(ar, x),
        'format': lambda x, kq: (
            f' => Tìm thấy {x} tại chỉ số {kq} (đệ quy).' if kq != -1
            else f' => Không tìm thấy {x} trong mảng.'
        ),
    },
    '4': {
        'ten': 'BÀI 2.4: MÔ PHỎNG TỪNG BƯỚC (DRY RUN)',
        'ar': [2, 5, 8, 12, 16, 23, 38, 56, 72, 91],
        'goi_y': '95 (không có) hoặc 5 (có)',
        'ham': lambda ar, x: nhi_phan(ar, x, verbose=True),
        'format': lambda x, kq: (
            f'\n => Tìm thấy {x} tại chỉ số {kq[0]}.' if kq[0] != -1
            else f'\n => Không tìm thấy {x}.'
        ),
        'pre_call': lambda: print("Quá trình duyệt mảng:"),
    },
}
#chay
def chay_bai(cfg):
    print(f"\n{'='*55}\n {cfg['ten']}\n{'='*55}")
    print(f"Mảng dữ liệu: {cfg['ar']}")
    try:
        x = int(input(f"\nNhập X cần tìm (gợi ý: {cfg['goi_y']}): "))
        if 'pre_call' in cfg: cfg['pre_call']()
        ket_qua = cfg['ham'](cfg['ar'], x)
        print(cfg['format'](x, ket_qua))
    except ValueError:
        print(" => Lỗi: Vui lòng nhập số nguyên!")

if __name__ == "__main__":
    while True:
        print("\n" + "*"*55)
        print(" CHỌN BÀI (1-4) HOẶC 0 ĐỂ THOÁT")
        print("*"*55)
        for k, v in Noidung.items():
            print(f" {k}. {v['ten']}")
        print(" 0. Thoát")

        chon = input("\nLựa chọn: ")
        if chon == '0':
            print("Đã thoát.")
            break
        elif chon in Noidung:
            chay_bai(Noidung[chon])
        else:
            print("Không hợp lệ, thử lại!")