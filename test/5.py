import itertools
from simpleai.search import CspProblem, backtrack

def tao_rang_buoc_giao_nhau(vi_tri_1, vi_tri_2):
    """
    Hàm closure sinh ra ràng buộc cho các điểm giao cắt ngã tư.
    Trả về True nếu ký tự tại vi_tri_1 của từ thứ nhất 
    khớp hoàn toàn với ký tự tại vi_tri_2 của từ thứ hai.
    """
    def rang_buoc(cac_bien, cac_gia_tri):
        tu_1, tu_2 = cac_gia_tri
        return tu_1[vi_tri_1] == tu_2[vi_tri_2]
    return rang_buoc

def rang_buoc_khac_nhau(cac_bien, cac_gia_tri):
    """Đảm bảo một từ không được sử dụng lặp lại ở hai vị trí khác nhau"""
    return cac_gia_tri[0] != cac_gia_tri[1]

def giai_o_chu():
    # Danh sách từ vựng (Đã bổ sung 'LASER' để khớp với hình kết quả mẫu của đề)
    danh_sach_tu = [
        'ALE', 'LEE', 'EEL', 'LINE', 'HEEL', 'SAILS', 'HIKE', 
        'SHEET', 'HOSES', 'STEER', 'KEEL', 'TIE', 'KNOT', 'LASER'
    ]
    
    # 1. Tập biến: Dựa vào các con số đánh dấu vị trí bắt đầu trên lưới
    tap_bien = [
        '1_Ngang', '2_Doc', '3_Doc', 
        '4_Ngang', '5_Doc', 
        '6_Doc', '7_Ngang', 
        '8_Ngang'
    ]
    
    # Độ dài tương ứng của từng vị trí trên lưới
    chieu_dai_slot = {
        '1_Ngang': 5, 
        '2_Doc': 5,   
        '3_Doc': 5,   
        '4_Ngang': 4, 
        '5_Doc': 4,   
        '6_Doc': 3,   
        '7_Ngang': 3, 
        '8_Ngang': 5  
    }
    
    # 2. Tập giá trị: Lọc từ vựng theo đúng độ dài của từng slot
    mien_gia_tri = {
        bien: [tu for tu in danh_sach_tu if len(tu) == chieu_dai_slot[bien]]
        for bien in tap_bien
    }
    
    # 3. Tập ràng buộc
    tap_rang_buoc = []
    
    # Tất cả các vị trí phải chứa các từ khác nhau
    for cap_bien in itertools.combinations(tap_bien, 2):
        tap_rang_buoc.append((cap_bien, rang_buoc_khac_nhau))
        
    # Khai báo các điểm giao nhau (Ngã tư) dựa trên tọa độ hình học
    # Quy tắc: ((Biến_1, Biến_2), tao_rang_buoc(index_chữ_cắt_của_biến_1, index_chữ_cắt_của_biến_2))
    giao_cat = [
        (('1_Ngang', '2_Doc'), 2, 0),  # Giao tại Hàng 1, Cột 3
        (('1_Ngang', '3_Doc'), 4, 0),  # Giao tại Hàng 1, Cột 5
        (('4_Ngang', '2_Doc'), 1, 2),  # Giao tại Hàng 3, Cột 3
        (('4_Ngang', '5_Doc'), 2, 0),  # Giao tại Hàng 3, Cột 4
        (('4_Ngang', '3_Doc'), 3, 2),  # Giao tại Hàng 3, Cột 5
        (('7_Ngang', '2_Doc'), 0, 3),  # Giao tại Hàng 4, Cột 3
        (('7_Ngang', '5_Doc'), 1, 1),  # Giao tại Hàng 4, Cột 4
        (('7_Ngang', '3_Doc'), 2, 3),  # Giao tại Hàng 4, Cột 5
        (('8_Ngang', '6_Doc'), 0, 1),  # Giao tại Hàng 5, Cột 1
        (('8_Ngang', '2_Doc'), 2, 4),  # Giao tại Hàng 5, Cột 3
        (('8_Ngang', '5_Doc'), 3, 2),  # Giao tại Hàng 5, Cột 4
        (('8_Ngang', '3_Doc'), 4, 4),  # Giao tại Hàng 5, Cột 5
    ]
    
    for (bien_1, bien_2), idx_1, idx_2 in giao_cat:
        tap_rang_buoc.append(((bien_1, bien_2), tao_rang_buoc_giao_nhau(idx_1, idx_2)))
    
    bai_toan = CspProblem(tap_bien, mien_gia_tri, tap_rang_buoc)
    return backtrack(bai_toan)


def in_luoi_kieu_ascii(ket_qua):
    """Hàm phụ trợ vẽ lại lưới ô chữ chính xác như tài liệu"""
    if not ket_qua:
        print("=> Không tìm thấy đáp án hợp lệ!")
        return
        
    # Tạo ma trận rỗng 6x5 chứa ký tự '#' (block)
    luoi = [['#' for _ in range(5)] for _ in range(6)]
    
    # Tọa độ (Hướng, Hàng_bắt_đầu, Cột_bắt_đầu) theo chuẩn index 0-based
    toa_do_bien = {
        '1_Ngang': ('ngang', 0, 0),
        '2_Doc':   ('doc',   0, 2),
        '3_Doc':   ('doc',   0, 4),
        '4_Ngang': ('ngang', 2, 1),
        '5_Doc':   ('doc',   2, 3),
        '6_Doc':   ('doc',   3, 0),
        '7_Ngang': ('ngang', 3, 2),
        '8_Ngang': ('ngang', 4, 0)
    }
    
    # Áp các chữ cái từ kết quả vào ma trận
    for bien, tu in ket_qua.items():
        huong, r, c = toa_do_bien[bien]
        for i, char in enumerate(tu):
            if huong == 'ngang':
                luoi[r][c + i] = char
            else:
                luoi[r + i][c] = char

    # In ra màn hình với viền ASCII
    print("    1   2   3   4   5")
    duong_vien = "  +---+---+---+---+---+"
    
    for i, hang in enumerate(luoi):
        print(duong_vien)
        row_str = f"{i+1} | " + " | ".join(hang) + " |"
        print(row_str)
    print(duong_vien)


if __name__ == "__main__":
    print("BÀI 5: KẾT QUẢ GIẢI ĐÁP Ô CHỮ")
    print("-" * 40)
    ket_qua_o_chu = giai_o_chu()
    in_luoi_kieu_ascii(ket_qua_o_chu)