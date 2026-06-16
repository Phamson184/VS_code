# nguyên dương
while True:
    a=input('Nhập số nguyên dương a:')
    try:
        if not a:
            print('Vui lòng nhập số')
        elif int(a) <=0:
            print('a phải là số nguyên dương')
        else:
            print(f'Số nguyên dương a là: {a}')
            break
    except ValueError:
        print('a phải là số nguyên')
# số nguyên tố
while True:
    a=input('Nhập số a: ')
    try:
        if not a:
            print('Vui lòng nhập số')
            continue
        n=int(a)
        if n<=0:
            print('Phải là số nguyên dương')
            continue
        break
    except ValueError:
        print('Vui lòng nhập số nguyên')        
n=int(a)
if n<2:
    print('Không phải số nguyên tố')
else:
    ngto=True
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            ngto=False
            break
    if ngto:
        print(f'{n} là số nguyên tố')
    else:
        print(f'{n} không phải số nguyên tố')
# độ F->C
while True:
    try:
        f=input('Nhập độ F: ')
        if not f:
            print('Vui lòng nhập só')
            continue
        f=float(f)
        c=5*(f-32)/9
        print(f'Với độ F là {f} sang độ C là: {c:2.f}')
        break
    except ValueError:
        print('Vui lòng nhập số hợp lệ')
#Xác định mùa
while True:
    try:
        a=int(input('Nhập số tháng:'))
        if a<1 or a>12:
            print('Tháng không hợp lệ (1-12)')
            continue
        break
    except ValueError:
        print('Vui lòng nhập số nguyên')
if 1<=a<+3:
    print('Mùa xuân')
elif 4<=a<=6:
    print('Mùa hạ')
elif 7<=a<=9:
    print('Mùa thu')
elif 10<=a<=12:
    print('Mùa đông')
#Chu vi và S tròn
import math
while True:
    try:
        r=float(input('Nhập bán kính hình tròn:'))
        if r<=0:
            print('Số phải lớn hơn 0')
            continue
        break
    except ValueError:
        print('Vui lòng nhập số hợp lệ')
s=math.pi*r*r
c=2*math.pi*r
print(f' Với r là {r}: Chu vi là {c:.2f} và diện tích là {s:.2f}')
#Năm nhuận
while True:
    try:
        y=int(input('Nhập số năm:'))
        if y<=0:
            print('Số năm phải lớn hơn 0')
            continue
        break
    except ValueError:
        print('Phải nhập số nguyên')
if y%400==0 or (y%4 and y%100!=0):
    print(f'{y} là năm nhuận')
else:
    print(f'{y} không phải năm nhuận')
# Trung bình cộng trên đoạn
while True:
    try:
        a,b=map(int,input('Nhập đoạn a và b (cách nhau bằng dấu cách) :').split())
        if b<a:
            print('b phải >=a')
            continue
        break
    except ValueError:
        print('Phải nhập số nguyên')
tong=0
n=b-a+1
for i in range(a,b+1):
    tong+=i 
tbc=tong/n 
print(f' trên đoạn [{a},{b}] trung bình cộng là: {tbc:.2f}')
#số nguyên tố trên đoạn      
while True:
    try:
        a,b =map(int, input('Nhập đoạn a và b (cách nhau bằng dấu cách):').split())
        if b<a:
            print('b phải >=a')
            continue
        break
    except ValueError:
        print('Phải nhập số nguyên')
def so_ngto(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
ngto=[]
for i in range(a,b+1):
    if so_ngto(i):
        ngto.append(i)
print(f'Danh sách số nguyên tố là:{ngto}')
# max trong 3 số
a,b,c=map(int,input('Nhập 3 số nguyên (cách nhau bởi dấu cách):').split())
nhat=a
if b>nhat:
    nhat=b
if c>nhat:
    nhat=c
print(f'Số lớn nhất là {nhat}')
# Tìm trong list
ds=input('Nhập các phần từ cách nhau bằng dấu cách:').split()
x=input('Nhập thành phần cần tìm:').split()
a=[]
b=[]
for i in ds:
    if i in x:
        a.append(i)
    else:
        b.append(i)
print(f'Các thành phần có trong danh sách là:{a}')
print(f'Các thành phần không có danh sách:{b}')
# Sắp list tăng dần
def sap_xep(data):
    n=len(data)
    def hoan_doi(i,j):
        data[i],data[j]=data[j],data[i]
    for i in range(n-1):
        for j in range(i+1,n):
            if data[i]>data[j]:
                hoan_doi(i,j)
    return data
data=list(map(int,input('Nhập các số cashc nhau bằng dấu cách:').split()))
print(f'List sau khi sắp xếp: {sap_xep(data)}')
# mymap()
def mymap(a,data):
    return [a(x) for x in data]
def big_mymap(a,data):
    return (a(x) for x in data)
data=list(map(int,input('Nhập các số cashc nhau bằng dấu cách:').split()))
bp=mymap(lambda x: x**2,data)
lp=mymap(lambda x: x**3,data)
gap_doi=mymap(lambda x: x*2,data)
print(f'Bình phương :{bp}, Lập phương :{lp}, Gấp đôi :{gap_doi}')
#tính thống kê()
def tinh_thong_ke(data:list)->list:
    if not data:
        raise ValueError('Data không được rỗng')
    tong=be=lon=data[0]
    for x in data[1:]:
        tong+=x
        if x<be:be=x
        if x>lon:lon=x
    return{
        'sum':tong,
        'average':tong/len(data),
        'min':be,
        'max':lon,
    }
data=list(map(int,input('Nhập các số cách nhau bằng dấu cách:').split()))
kq=tinh_thong_ke(data)
print(kq)
#sap_xep()
def sap_xep(data: list)->list:
    data=data.copy()
    n=len(data)
    def hoan_doi(i:int,j:int)->None:
        data[i],data[j]=data[j],data[i]
    for i in range(n-1):
        for j in range(i+1,n):
            if data[i]>data[j]:
                hoan_doi(i,j)
    return data
a=list(map(int,input('Nhập các số cách nhau bằng dấu cách; ').split()))
print(f'List gốc: {a}')
print(f'Sau sắp xếp: {sap_xep(a)}')
#
def tien_dien(so_kwh):
    if so_kwh<=50:
        return so_kwh*1600
    elif so_kwh<=100:
        return (50*1600)+((so_kwh-50)*1700)
    else:
        return (50*1600)+(50*1700)+((so_kwh-100)*2000)
so_kwh=int(input('Nhập số kwh: '))
print(f'Số tiền điện phải trả: {tien_dien(so_kwh):,}VNĐ')
#