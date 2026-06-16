import copy

def get_board_str(board):
    res = "+---+---+---+---+\n"
    for row in board:
        # Thay thế ô trống bằng khoảng trắng để vẽ viền cho chuẩn
        row_str = " | ".join([cell if cell != "" else " " for cell in row])
        res += f"| {row_str} |\n"
        res += "+---+---+---+---+\n"
    return res

# Khởi tạo bàn cờ 4x4 trống hoàn toàn
state_0 = [["" for _ in range(4)] for _ in range(4)]

# Lấy danh sách 16 tọa độ trống ban đầu
empty_cells = [(r, c) for r in range(4) for c in range(4)]
# Mở file để ghi kết quả
with open("240_truong_hop_caro.txt", "w", encoding="utf-8") as f:
    f.write("TRẠNG THÁI GỐC (Bàn cờ trống)\n")
    f.write(get_board_str(state_0))
    
    # BƯỚC 1: Duyệt 16 trường hợp của Max (X)
    for i, (rx, cx) in enumerate(empty_cells, start=1):
        state_1 = copy.deepcopy(state_0)
        state_1[rx][cx] = "X"
        
        f.write(f"\n{'='*50}\n")
        f.write(f" BƯỚC 1 - NHÁNH {i}/16: MAX (X) ĐÁNH TẠI ({rx}, {cx})\n")
        f.write(f"{'='*50}\n")
        f.write(get_board_str(state_1))
        
        # BƯỚC 2: Duyệt 15 trường hợp của Min (O) tương ứng
        empty_for_o = [(r, c) for r in range(4) for c in range(4) if state_1[r][c] == ""]
        
        for j, (ro, co) in enumerate(empty_for_o, start=1):
            state_2 = copy.deepcopy(state_1)
            state_2[ro][co] = "O"
            
            f.write(f"\n  -> BƯỚC 2 (Nhánh {i}.{j}): MIN (O) ĐÁNH TẠI ({ro}, {co})\n")
            f.write(get_board_str(state_2))

print("Hoàn tất! Đã xuất đủ 240 trạng thái bàn cờ.")
#
class Sanpham:
    def __init__(self,ma,ten,gia,so_luong):
        self.__ma=ma
        self.__ten=ten
        self.set_gia(gia)
        self.set_so_luong(so_luong)
    def get_gia_ban(self):
        return self.__gia
    def set_gia_ban(self):
        return self.__gia
    def set_gia(self,gia):
        if gia<0:
            self.__gia=0
        else:
            self.__gia=gia
    def get_so_luong(self):
        return self.__so_luong
    def set_so_luong(self,so_luong):
        if so_luong<0:
            self.__so_luong=0
        else:
            self.__so_luong=so_luong
    def get_ten(self):
        return self.__ten
    def thanh_tien(self):
        return self.__gia*self.__so_luong
nhapma=input('Nhập mã:')
nhapten=input('Nhập tên:')
nhapgia=float(input('Nhập giá:'))
nhapsl=int(input('Nhập số lượng:'))
sp=Sanpham(nhapma,nhapten,nhapgia,nhapsl)
print(f'Tên sản phẩm: {{sp.get_ten()}}')
print(f'Tổng tiền: {sp.thanh_tien():,} VND')
#
class Sach:
    def __init__(self,ma,ten,gia,so_luong):
        self.ma=ma
        self.ten=ten
        self.gia=gia
        self.so_luong=so_luong
    def hien_thi(self):
        print(f'Mã:{self.ma}')
        print(f'Tên:{self.ten}')
        print(f'Giá:{self.gia:,.0f}VND')
        print(f'Số lượng:{self.so_luong}')
    def phan_loai(self):
        if self.gia<50_000:
            return'Sách giá rẻ'
        elif self.gia<=100_000:
            return'Sách trung bình'
        else:
            return'Sách cao cấp'
    def thanh_tien(self):
        loai=self.phan_loai()
        tong=self.self.gia*self.so_luong
        khuyen_mai={'Sách giá rẻ': 0.00,'Sách trung bình':0.05,'Sách cao cấp':0.10}
        giam_gia=tong*khuyen_mai[loai]
        thanh_tien=tong-giam_gia
        return thanh_tien
try:
    ma=int(input('Nhập mã sách:'))
    ten=input('Nhập tên sách:')
    gia=float(o=input('Nhập giá:'))
    sl=int(input('Nhập số lượng:'))
    new=Sach(ma,ten,gia,sl)
    print('Kết quả như sau:')
    new.hien_thi()
    print(f' Loại sách {new.phan_loai()}')
    print(f'Thành tiền(sau khuyến mãi):{new.thanh_tien():,.0f}VND')
except ValueError:
    print('Vui lòng nhập định dạnh số cho mã, giá và số lượng')
# ngan hàng
import random
class TaiKhoan:
    def __init__(self,ten,so_du=0,pin="0000"):
        if so_du<0: raise ValueError("Số dư không được âm")
        self.ten=ten
        self.so_du=so_du
        self.pin=pin
        self.id=f"VN{random.randint(100000,999999)}"
        self.lich_su=[f"Nạp ban đầu: {so_du:,}VND"] if so_du >0 else []
    def nap(self,tien):
        if tien<=0: return print("Số tiền nạp phải >0")
        self.so_du+=tien
        self.lich_su.append(f"Nạp: {tien:,}VND")
        print(f"Đã nạp {tien:,}VND. Số dư: {self.so_du:,}VND")
    def rut(self,tien,pin):
        if pin!=self.pin: return print("Sai mã Pin")
        if tien<=0 or tien>self.so_du: return print("Tiền không hợp lệ hoặc không")
        self.so_du-=tien
        self.lich_su.append(f"Rút: {tien:,}VND")
        print(f"Đã rút {tien:,}VND. Số dư: {self.so_du:,}VND")
        return True
    def ck(self,tk_nhan,tien,pin):
        if self.rut(tien,pin):
            tk_nhan.nap(tien)
            self.lich_su[-1]=f"Chuyển cho {tk_nhan.ten}: {tien:,}VND"
            tk_nhan.lich_su[-1]=f"Nhận từ {self.ten}: {tien:,}VND"
    def xem_ls(self):
        print(f"Lịch sử Giao dịch - {self.ten} [{self.id}]")
        print("\n".join(self.lichsu) if self.lich_su else "Chưa có giao dịch")
#Số học
class SoHoc:
    def __init__(self,so1=0,so2=0):
        self.so1,self.so2=so1,so2
    def nhap(self):
        self.so1=float(input("Nhập số 1:"))
        self.so2=float(input("Nhập số 2:"))
    def cong(self): return self.so1+self.so2
    def tru(self): return self.so1-self.so2
    def nhan(self): return self.so1*self.so2
    def chia(self): return self.so1/self.so2 if self.so2 !=0 else "Lỗi chia 0"
#Nhân viên
class NhanVien:
    def __init__(self,ten,tuoi,luong,gio_lam):
        self.ten,self.tuoi,self.luong,self.gio_lam=ten,tuoi,luong,gio_lam
    @property
    def tien_th(self):
        if self.gio_lam>=200: return self.luong*0.20
        if self.gio_lam>=100: return self.luong*0.10
        return 0
    def __str__(self):
        return f"Nhân viên: {self.ten}| Lương: {self.luong:,}|Thưởng: {self.tien_th:.0f}"
#Sinh viên
class Sinhvien:
    def __init__(self,ma_sv,diem_tb,tuoi,lop):
        self.ma_sv=ma_sv
        self.diem_tb=diem_tb
        self.tuoi=tuoi
        self.lop=lop
    @property
    def ma_sv(self): return self.ma_sv
    @ma_sv.setter
    def ma_sv(self,a):
        if len(a)!=8: raise ValueError("Mã SV phải đúng 8 ký tự")
        self._ma_sv=a
    @property
    def diem_tb(self): return self._diem_tb
    @diem_tb.setter
    def diem_tb(self,a):
        if not (0<=a<=10): raise ValueError("Điểm phải từ 0-10")
        self._diem_tb=a
    @property
    def hoc_bong(self):
        return self.diem_tb>8.0
    def __str__(self):
        hb="Có" if self.hoc_bong else "Không"
        return f"SV: {self.ma_sv}|Lớp: {self.lop}|ĐTB: {self.diemtb}|Học bổng:{hb}"
if __name__=="__main__":
    print("Test tài khoản")
    tk1=TaiKhoan("Nguyễn A",1_000_000,"1234")
    tk2=TaiKhoan("Trần B",500_000)
    tk1.chuyen_khoan(tk2,300_000,"1234")
    tk1.xem_ls()
    print('Test nhân viên')
    nv=NhanVien("Lê văn C",25,10_000_000,150)
    print(nv)
    print("test")
    try:
        sv_loi=Sinhvien("SV001",11.0,18,"A1")
    except ValueError as e:
        print(f"Bắt được lỗi: {e}")
# template
from datetime import datetime
from typing import List
class Person:
    gioi_tinh={'Nam','Nữ','Khac'}
    def __init__(self,ten:str,gioi_tinh:str,ngay_sinh:str,dia_chi:str):
        self.ten=self._validate_ten(ten)
        self.gioi_tinh=self._validate_gioi_tinh(gioi_tinh)
        self.ngay_sinh=self._validate_ngay_sinh(ngay_sinh)
        self.dia_chi=dia_chi
    @staticmethod
    def _validate_ten(ten:str)->str:
        ten=ten.strip()
        if len(ten)<2: raise ValueError("Tên phải có ít nhất 2 ký tự")
        return ten
    @staticmethod
    def _validate_gioi_tinh(gt:str)->str:
        gt=gt.strip().capitalize()
        if gt not in Person.gioi_tinh:
            raise ValueError(f"Giới tính không hợp lệ, chọn trong {Person.gioi_tinh}")
        return gt
    @staticmethod
    def _validate_ngay_sinh(ns:str)->str:
        dt=datetime.strptime(ns.strip(),"%d/%m/%Y")
        if dt>datetime.now() or dt.year<1900:
            raise ValueError("Ngày sinh không hợp lệ (từ 1900 - hiện tại)")
        return ns
    def __str__(self)->str:
        return f"{self.ten}|{self.gioi_tinh}|{self.ngay_sinh}|{self.dia_chi}"
class Student(Person):
    def __init__(self,ten:str,gioi_tinh:str,ngay_sinh:str,dia_chi:str,ma_sv:str,email:str,diem_tb:float):
        super().__init__(ten,gioi_tinh,ngay_sinh,dia_chi) 
        if len(ma_sv.strip())!=8: raise ValueError("Mã SV phải đúng 8 ký tự")
        if '@' not in email: raise ValueError("Email thiếu ký tự @")
        if not (0.0<=diem_tb<=10): raise ValueError("Điểm TB từ 0-10")
        
        self.ma_sv=ma_sv.strip()
        self.email=email.strip()
        self.diem_tb=diem_tb 
        
    @property
    def xet(self)->bool:
        return self.diem_tb>8.0
    def __str__(self)->str:
        hoc_bong="Học bổng" if self.xet else"Không"
        return super().__str__()+f"|{self.ma_sv}|{self.email}|ĐTB:{self.diem_tb}->{hoc_bong}"
def nhap_lieu()->Student:
    print("Nhập thông tin sinh viên")
    while True:
        try:
            ten=input("Tên: ")
            gt=input("Giới tính: ")
            ns=input("Ngày sinh:")
            dc=input("Địa chỉ:")
            ma=input("Mã SV(8 ký tự):")
            email=input("Email:")
            dtb=float(input("Điểm TB(0-10):"))
            return Student(ten,gt,ns,dc,ma,email,dtb)
        except ValueError as e:
            print(f"Dữ liệu lỗi: {e}. Vui lòng nhập lại toàn bộ")
if __name__=="__main__":
    sv1=Student("nguyễn Văn A","Nam","20/03/2000","Hà Nội","SV123456","a@gmail.com",8.5)
    print(sv1)
                