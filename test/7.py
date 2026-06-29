from simpleai.search import CspProblem, backtrack, \
    MOST_CONSTRAINED_VARIABLE, HIGHEST_DEGREE_VARIABLE, LEAST_CONSTRAINING_VALUE

# --- CÁC HÀM LOGIC RÀNG BUỘC ---
def rang_buoc_bang_nhau(cac_bien, cac_gia_tri): 
    return cac_gia_tri[0] == cac_gia_tri[1]
    
def rang_buoc_khac_nhau(cac_bien, cac_gia_tri): 
    return cac_gia_tri[0] != cac_gia_tri[1]
    
def rang_buoc_nho_hon(cac_bien, cac_gia_tri):   
    return cac_gia_tri[0] < cac_gia_tri[1]

def khoi_tao_do_thi_5_bien():
    tap_bien = ['A', 'B', 'C', 'D', 'E']
    mien_gia_tri = {
        'A': [1, 2, 3, 4], 'B': [1, 2, 4], 'C': [1, 3, 4],
        'D': [1, 2, 3, 4], 'E': [1, 2, 3, 4]
    }
    tap_rang_buoc = [
        (('A', 'B'), rang_buoc_khac_nhau), (('A', 'D'), rang_buoc_bang_nhau),
        (('E', 'A'), rang_buoc_nho_hon),   (('B', 'C'), rang_buoc_khac_nhau),
        (('B', 'D'), rang_buoc_khac_nhau), (('E', 'B'), rang_buoc_nho_hon),
        (('C', 'D'), rang_buoc_nho_hon),   (('E', 'C'), rang_buoc_nho_hon),
        (('E', 'D'), rang_buoc_nho_hon)    # Ràng buộc bổ sung để đồ thị đúng logic
    ]
    return CspProblem(tap_bien, mien_gia_tri, tap_rang_buoc)

# --- HÀM TRÌNH BÀY OUTPUT THEO STYLE CỦA BẠN ---
def in_ket_qua_csp(tieu_de, ket_qua):
    if ket_qua:
        # Nối kết quả thành chuỗi dạng A: 4 | B: 2 | C: 3...
        chuoi_kq = " | ".join(f"{bien}: {ket_qua[bien]}" for bien in sorted(ket_qua.keys()))
        print(f"{tieu_de:<30} => {chuoi_kq}")
    else:
        print(f"{tieu_de:<30} => Không tìm thấy giải pháp")

if __name__ == "__main__":
    bai_toan = khoi_tao_do_thi_5_bien()
    
    print("\n--- BÀI TOÁN MẪU 2: KẾT QUẢ TÌM KIẾM CSP ĐỒ THỊ 5 BIẾN ---")
    
    # Duyệt cơ bản (Normal)
    kq_normal = backtrack(bai_toan)
    in_ket_qua_csp("1. Duyệt cơ bản (Normal)", kq_normal)
    
    # Heuristic: MOST_CONSTRAINED_VARIABLE
    kq_mcv = backtrack(bai_toan, variable_heuristic=MOST_CONSTRAINED_VARIABLE)
    in_ket_qua_csp("2. Most Constrained Variable", kq_mcv)
    
    # Heuristic: HIGHEST_DEGREE_VARIABLE
    kq_hdv = backtrack(bai_toan, variable_heuristic=HIGHEST_DEGREE_VARIABLE)
    in_ket_qua_csp("3. Highest Degree Variable", kq_hdv)
    
    # Heuristic: LEAST_CONSTRAINING_VALUE
    kq_lcv = backtrack(bai_toan, value_heuristic=LEAST_CONSTRAINING_VALUE)
    in_ket_qua_csp("4. Least Constraining Value", kq_lcv)
    print("-" * 65)