from simpleai.search import CspProblem, backtrack

def rang_buoc_an_chay(cac_bien, cac_gia_tri):
    """
    Ràng buộc thực đơn chay:
    - Nếu khai vị là rau -> món chính phải là cá hoặc gà.
    - Suy ra: Nếu món chính là bò (không chay) -> khai vị không được là rau.
    """
    khai_vi, mon_chinh = cac_gia_tri
    
    # Nếu khách chọn bò, thì không thể dùng rau làm khai vị (phá vỡ thực đơn chay)
    if mon_chinh == 'bo':
        return khai_vi != 'rau'
        
    # Nếu khách chọn rau làm khai vị, bắt buộc món chính phải là cá hoặc gà
    if khai_vi == 'rau':
        return mon_chinh in ['ca', 'ga']
        
    # Các trường hợp còn lại (ví dụ: khai vị salad, món chính cá/gà) đều hợp lệ
    return True

def rang_buoc_mon_ngot(cac_bien, cac_gia_tri):
    """Thực đơn phải có ít nhất một món ngọt: sữa, kem hoặc chè"""
    do_uong, trang_mieng = cac_gia_tri
    return do_uong == 'sua' or trang_mieng in ['kem', 'che']

def thiet_ke_thuc_don():
    tap_bien = ['Khai_Vi', 'Do_Uong', 'Mon_Chinh', 'Trang_Mieng']
    
    mien_gia_tri = {
        'Khai_Vi': ['rau', 'salad'],
        'Do_Uong': ['nuoc', 'soda', 'sua'],
        'Mon_Chinh': ['ca', 'bo', 'ga'],
        'Trang_Mieng': ['tao', 'kem', 'che']
    }
    
    tap_rang_buoc = [
        (('Khai_Vi', 'Mon_Chinh'), rang_buoc_an_chay),
        (('Do_Uong', 'Trang_Mieng'), rang_buoc_mon_ngot)
    ]
    
    bai_toan = CspProblem(tap_bien, mien_gia_tri, tap_rang_buoc)
    return backtrack(bai_toan)

if __name__ == "__main__":
    print("BÀI 2: KẾT QUẢ THIẾT KẾ THỰC ĐƠN SỰ KIỆN")
    ket_qua = thiet_ke_thuc_don()
    
    if ket_qua:
        danh_muc_hien_thi = {
            'Khai_Vi': 'Món khai vị',
            'Do_Uong': 'Đồ uống',
            'Mon_Chinh': 'Món chính',
            'Trang_Mieng': 'Tráng miệng'
        }
        
        print("-" * 40)
        # Thứ tự lên món tự nhiên
        thu_tu_an = ['Khai_Vi', 'Do_Uong', 'Mon_Chinh', 'Trang_Mieng']
        
        for bien in thu_tu_an:
            ten_mon = ket_qua[bien]
            print(f"{danh_muc_hien_thi[bien]:<15} : {ten_mon.capitalize()}")
        print("-" * 40)
    else:
        print("\n=> Không thể thiết kế thực đơn thỏa mãn các điều kiện.")