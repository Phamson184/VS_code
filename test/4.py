import itertools
from simpleai.search import CspProblem, backtrack

def rang_buoc_quan_hau(cac_bien, cac_gia_tri):
    """
    Ràng buộc đảm bảo hai quân hậu bất kỳ:
    - Không nằm cùng một hàng.
    - Không nằm cùng một đường chéo.
    """
    bien_1, bien_2 = cac_bien
    hang_1, hang_2 = cac_gia_tri
    
    # Lấy chỉ số cột từ tên biến (Ví dụ: 'X1' -> chỉ số cột là 1)
    cot_1 = int(bien_1[1:])
    cot_2 = int(bien_2[1:])
    
    # Kiểm tra ràng buộc cùng hàng
    if hang_1 == hang_2:
        return False
        
    # Kiểm tra ràng buộc cùng đường chéo
    if abs(hang_1 - hang_2) == abs(cot_1 - cot_2):
        return False
        
    return True

def giai_8_quan_hau():
    # 1. Tập biến tương ứng với 8 cột: X1 đến X8
    tap_bien = [f'X{i}' for i in range(1, 9)]
    
    # 2. Tập giá trị: Mỗi cột tương ứng với các vị trí hàng từ 1 đến 8
    mien_gia_tri = {bien: list(range(1, 9)) for bien in tap_bien}
    
    # 3. Thiết lập ràng buộc cho tất cả các cặp cột (Tổ hợp chập 2)
    tap_rang_buoc = []
    for cap_bien in itertools.combinations(tap_bien, 2):
        tap_rang_buoc.append((cap_bien, rang_buoc_quan_hau))
        
    bai_toan = CspProblem(tap_bien, mien_gia_tri, tap_rang_buoc)
    return backtrack(bai_toan)

def in_ban_co_8x8(ket_qua):
    if not ket_qua:
        print("\n=> Không tìm thấy giải pháp hợp lệ.")
        return
        
    print(f"\nTọa độ tìm được (Cột: Hàng) -> {ket_qua}\n")
    
    # Khởi tạo ma trận ô cờ rỗng kích thước 8x8
    ban_co = [["." for _ in range(8)] for _ in range(8)]
    
    # Điền vị trí quân hậu vào bàn cờ (Chuyển đổi từ index 1-based sang 0-based)
    for bien, hang in ket_qua.items():
        cot_idx = int(bien[1:]) - 1
        hang_idx = hang - 1
        ban_co[hang_idx][cot_idx] = "Q"
        
    # In ma trận bàn cờ ra màn hình console
    for dong in ban_co:
        print("    " + " ".join(dong))

if __name__ == "__main__":
    print("BÀI 4: SẮP XẾP 8 QUÂN HẬU TRÊN BÀN CỜ 8x8")
    print("-" * 40)
    ket_qua_8_hau = giai_8_quan_hau()
    in_ban_co_8x8(ket_qua_8_hau)
    print("-" * 40)