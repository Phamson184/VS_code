def nam_nhuan(nam:int)->bool:
    return(nam%400==0) or (nam%4==0 and nam%100!=0)
def thang_co_may_ngay(thang:int,nam:int)->int:
    thang_31={1,3,5,7,8,10,12}
    thang_30={4,6,9,11}
    if thang in thang_31:
        return 31
    elif thang in thang_30:
        return 30
    elif thang ==2:
        return 29 if nam_nhuan(nam) else 28
    else:
        raise ValueError('Tháng không hợp lệ(1-12)')
thang=int(input('Nhập tháng(1-12): '))
nam=int(input('Nhập năm: '))
ngay=thang_co_may_ngay(thang,nam)
print(f'Tháng {thang} năm {nam} có {ngay} ngày.') 