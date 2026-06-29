from simpleai.search import CspProblem, backtrack

def rang_buoc_khac_nhau(cac_bien, cac_gia_tri):
    """Đảm bảo 2 phần tử kề nhau không được trùng giá trị"""
    return cac_gia_tri[0] != cac_gia_tri[1]

def tim_gia_tri_do_thi():
    tap_bien = ['C1', 'C2', 'C3', 'C4', 'C5']
    
    mien_gia_tri = {
        'C1': ['C'],
        'C2': ['B', 'C'],
        'C3': ['A', 'B', 'C'],
        'C4': ['A', 'B', 'C'],
        'C5': ['B', 'C']
    }
    
    tap_rang_buoc = [
        (('C1', 'C2'), rang_buoc_khac_nhau),
        (('C2', 'C3'), rang_buoc_khac_nhau),
        (('C3', 'C4'), rang_buoc_khac_nhau),
        (('C4', 'C5'), rang_buoc_khac_nhau),
        (('C2', 'C4'), rang_buoc_khac_nhau),
        (('C3', 'C5'), rang_buoc_khac_nhau)
    ]
    
    bai_toan = CspProblem(tap_bien, mien_gia_tri, tap_rang_buoc)
    return backtrack(bai_toan)

if __name__ == "__main__":
    print("BÀI 1: LỰA CHỌN GIÁ TRỊ CHO CÁC PHẦN TỬ ĐỒ THỊ")
    ket_qua = tim_gia_tri_do_thi()
    
    if ket_qua:
        print(f"\n{'Phần tử':<10} | {'Giá trị':<10}")
        print("-" * 25)
        for bien in sorted(ket_qua.keys()):
            print(f"{bien:<10} | {ket_qua[bien]:<10}")
    else:
        print("\n=> Không tìm thấy giải pháp hợp lệ.")