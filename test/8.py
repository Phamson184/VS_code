from simpleai.search import CspProblem, backtrack, \
    MOST_CONSTRAINED_VARIABLE, HIGHEST_DEGREE_VARIABLE, LEAST_CONSTRAINING_VALUE

# --- CÁC HÀM KIỂM TRA RÀNG BUỘC ---
def rang_buoc_bang_nhau(cac_bien, cac_gia_tri):
    return cac_gia_tri[0] == cac_gia_tri[1]

def rang_buoc_khac_nhau(cac_bien, cac_gia_tri):
    return cac_gia_tri[0] != cac_gia_tri[1]

def rang_buoc_nho_hon(cac_bien, cac_gia_tri):
    return cac_gia_tri[0] < cac_gia_tri[1]


def xay_dung_bai_toan_do_thi():
    # 1. Khai báo tập biến [cite: 461]
    tap_bien = ['A', 'B', 'C', 'D', 'E']
    
    # 2. Khai báo miền giá trị [cite: 463, 464, 470, 476, 482, 489]
    mien_gia_tri = {
        'A': [1, 2, 3, 4],
        'B': [1, 2, 4],
        'C': [1, 3, 4],
        'D': [1, 2, 3, 4],
        'E': [1, 2, 3, 4]
    }
    
    # 3. Khai báo tập ràng buộc [cite: 508]
    tap_rang_buoc = [
        (('A', 'B'), rang_buoc_khac_nhau),
        (('A', 'D'), rang_buoc_bang_nhau),
        (('E', 'A'), rang_buoc_nho_hon),
        (('B', 'C'), rang_buoc_khac_nhau),
        (('B', 'D'), rang_buoc_khac_nhau),
        (('E', 'B'), rang_buoc_nho_hon),
        (('C', 'D'), rang_buoc_nho_hon),
        (('E', 'C'), rang_buoc_nho_hon),
        # Đã bổ sung ràng buộc E < D (Có trên hình nhưng thiếu trong code mẫu tài liệu)
        (('E', 'D'), rang_buoc_nho_hon) 
    ]
    
    return CspProblem(tap_bien, mien_gia_tri, tap_rang_buoc)


if __name__ == "__main__":
    print("=============================================")
    print("BÀI TOÁN MẪU 2: TÌM KIẾM CSP - ĐỒ THỊ 5 BIẾN")
    print("=============================================\n")
    
    bai_toan = xay_dung_bai_toan_do_thi()
    
    print("Các kết quả theo từng chiến lược Heuristic:")
    print("-" * 65)
    
    # 1. Giải pháp thông thường (Duyệt cơ bản) [cite: 513, 514]
    kq_normal = backtrack(bai_toan)
    print(f"1. Normal (Không Heuristic):\n   {kq_normal}\n")
    
    # 2. Heuristic: Biến bị ràng buộc nhiều nhất [cite: 516]
    kq_most_constrained = backtrack(bai_toan, variable_heuristic=MOST_CONSTRAINED_VARIABLE)
    print(f"2. Most Constrained Variable:\n   {kq_most_constrained}\n")
    
    # 3. Heuristic: Biến có bậc cao nhất trên đồ thị [cite: 517]
    kq_highest_degree = backtrack(bai_toan, variable_heuristic=HIGHEST_DEGREE_VARIABLE)
    print(f"3. Highest Degree Variable:\n   {kq_highest_degree}\n")
    
    # 4. Heuristic: Giá trị ít ràng buộc nhất (Ít gây cản trở biến khác) [cite: 518]
    kq_least_constraining = backtrack(bai_toan, value_heuristic=LEAST_CONSTRAINING_VALUE)
    print(f"4. Least Constraining Value:\n   {kq_least_constraining}")
    print("-" * 65)