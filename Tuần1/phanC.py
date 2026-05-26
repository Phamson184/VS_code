from typing import List,Tuple,Dict,Any
#13
def tim_chuoi(ds:List[str],a:str)->int:
    a=a.lower()
    for i in range(len(ds)):
        if ds[i].lower()==a:
            return i
    return -1
#14
def chan_first(a:List[int])->int:
    for i in range(len(a)):
        if a[i]%2==0:
            return i
    return -1
#15
def ngto(n:int)->bool:
    if n<2: return False
    for i in range(2,int(n*0.5)+1):
        if n%i==0: return False
    return True
def ngto_first(a:List[int])->Tuple[Any,int]:
    for i in range(len(a)):
        if ngto(a[i]):
            return a[i],i
    return None,-1
#16
def near_x(a:List[int],x:int)->Tuple[Any,int]:
    if not a: return None, -1
    min_kc=abs(a[0]-x)
    i,gt=0,a[0]
    for i in range(1,len(a)):
        kc=abs(a[i]-x)
        if kc<min_kc:
            min_kc,i,gt=kc,i,a[i]
    return gt,i
#17
def tim_kiem(a:List[int],x:int)->int:
    n=len(a)
    if n==0: return -1
    cuoi=a[n-1]
    a[n-1]=x
    i=0
    while a[i]!=x:
        i+=1
    a[n-1]=cuoi
    if i<n-1 or a[n-1]==x:
        return i
    return -1
#18
def matran(M: List[List[int]],x:int)->Tuple[int,int]:
    for i in range(len(M)):
        for j in range(len(M[i])):
            if M[i][j]==x:
                return (i,j)
    return (-1,-1)
#19
def tim_sv(ds:List[Dict],ma:str):
    for sv in ds:
        if sv['ma']==ma:
            print(f"Tìm thấy: Mã: {sv['ma']}|Tên: {sv['ho_ten']}|ĐTB: {sv['dtb']}")
            return
    print("Không tìm thấy sinh viên")
#20
class Quanlydanhba:
    def __init__(self):
        self.danh_ba=[
            {'ten':'Nguyen Van A','sdt':'3456787654'},
            {'ten':'Tran thi B','sdt':'234543245'},
            {'ten':'Le Van C','sdt':'234565435'}
        ]
    def them_lien_he(self,ten:str,sdt:str):
        self.danh_ba.append({'ten':ten,'sdt':sdt})
        print("Đã thêm thành công")
    def tim_sdt_theo_ten(self,ten:str):
        for lh in self.danh_ba:
            if lh['ten'].lower()==ten.lower():
                return lh['sdt']
        return "không có"
    def tim_ten_theo_sdt(self,sdt:str):
        for lh in self.danh_ba:
            if lh['sdt']==sdt:
                return lh['ten']
        return "không có"
    def dem_theo_dau_so(self,dau_so:str)->int:
        return sum(1 for lh in self.danh_ba if str(lh['sdt']).startswith(dau_so))
    def menu(self):
        while True:
            print("\n"+"="*35)
            print("Quản lý danh bạ")
            print("="*35)
            print('1.Xem toàn bộ danh bạ')
            print('2.Thêm liên hệ mới')
            print('3.Tìm số điện thoại theo tên')
            print('4.Tìm tên theo số điện thoại')
            print('5. Đếm số liên hệ theo đầu số')
            print('0.Thoát Menu Danh Bạ')
            chon=input('Chọn chức năng(0-5):').strip()
            if chon=='0':
                print('Đã thoát danh bạ.\n')
                break
            elif chon=='1':
                for lh in self.danh_ba:
                    print(f"Tên:{lh['ten']}|SĐT: {lh['sdt']}")
            elif chon=='2':
                t=input("Nhập tên:")
                s=input("Nhập SĐT:")
                self.them_lien_he(t,s)
            elif chon=='3':
                t=input("Nhập tên cần tìm:")
                print(f"-> SĐT là: {self.tim_sdt_theo_ten(t)}")
            elif chon=='4':
                s=input("Nhập SĐT cần tìm: ")
                print(f"-> Tên là: {self.tim_ten_theo_sdt(s)}")
            elif chon=='5':
                d=input("Nhập đầu số:")
                print(f"-> Có {self.dem_theo_dau_so(d)} Liên hệ")
            else:
                print('Lựa chọn không hợp lệ')
def main():
        print("Chạy cá bài 13-19")
        ds_chuoi=["an","Bình","Châu"]
        print(f"\n Bài 13 Tìm 'an' trong {ds_chuoi}: Vị trí {tim_chuoi(ds_chuoi,'an')}") 
        mang_so=[3,7,11,8,5,4]
        print(f"\n Bài 14 Số chẵn đầu tiên trong {mang_so} ở vị trí: {chan_first(mang_so)}")
        mang_nt=[4,6,9,7,11]
        gt,i=ngto_first(mang_nt)
        mang_near=[10,22,28,29,40]
        gt_n,i_n=near_x(mang_near,26)
        print(f"Bài 16 Phần từ gần 26 nhất trong {mang_near}: {gt_n} tại vị trí (i_n)")
        print(f"Bài 17 Tìm 28: Vị trí {tim_kiem(mang_near,28)}")
        ma_tran=[[5,8,1],[3,9,7],[2,6,4]]
        print(f"\n Bài 18 Tìm 9 trong ma trận: Vị trí {matran(ma_tran,9)}")
        ds=[
            {'ma':'SV01','ho_ten':'Nguyen A','dtb':8.5},
            {'ma':'SV02','ho_ten':'Le B','dtb':7.0}
        ]
        print("\n Bài 19 Tìm sinh viên mã SV02:")
        tim_sv(ds,'SV02') 
        app= Quanlydanhba()
        app.menu()
if __name__=='__main__':
        main()       