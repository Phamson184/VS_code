from simpleai.search import CspProblem, backtrack
import itertools

def rang_buoc_giao_nhau(idx1, idx2):
    return lambda bin, val: val[0][idx1] == val[1][idx2]

def giai_o_chu_chuan():
    # Danh sách từ gốc (loại bỏ từ ngoại lai)
    danh_sach_tu = ['ALE', 'LEE', 'EEL', 'LINE', 'HEEL', 'SAILS', 'HIKE', 
                    'SHEET', 'HOSES', 'STEER', 'KEEL', 'TIE', 'KNOT']
    
    tap_bien = ('1_N', '2_D', '3_D', '4_N', '5_D', '6_D', '7_N', '8_N')
    do_dai = {'1_N': 5, '2_D': 5, '3_D': 5, '4_N': 4, '5_D': 4, '6_D': 3, '7_N': 3, '8_N': 5}
    
    mien_gia_tri = {b: [t for t in danh_sach_tu if len(t) == do_dai[b]] for b in tap_bien}
    
    # Ràng buộc khác nhau cho tất cả các vị trí
    tap_rang_buoc = [((b1, b2), lambda bin, val: val[0] != val[1]) 
                     for b1, b2 in itertools.combinations(tap_bien, 2)]
    
    # Thêm ràng buộc giao nhau
    tap_rang_buoc.extend([
        (('1_N', '2_D'), rang_buoc_giao_nhau(2, 0)),
        (('1_N', '3_D'), rang_buoc_giao_nhau(4, 0)),
        (('4_N', '2_D'), rang_buoc_giao_nhau(1, 2)),
        (('4_N', '5_D'), rang_buoc_giao_nhau(2, 0)),
        (('4_N', '3_D'), rang_buoc_giao_nhau(3, 2)),
        (('7_N', '2_D'), rang_buoc_giao_nhau(0, 3)),
        (('7_N', '5_D'), rang_buoc_giao_nhau(1, 1)),
        (('7_N', '3_D'), rang_buoc_giao_nhau(2, 3)),
        (('8_N', '6_D'), rang_buoc_giao_nhau(0, 1)),
        (('8_N', '2_D'), rang_buoc_giao_nhau(2, 4)),
        (('8_N', '5_D'), rang_buoc_giao_nhau(3, 2)),
        (('8_N', '3_D'), rang_buoc_giao_nhau(4, 4))
    ])
    
    return backtrack(CspProblem(tap_bien, mien_gia_tri, tap_rang_buoc))

if __name__ == "__main__":
    ket_qua = giai_o_chu_chuan()
    if ket_qua:
        print("Kết quả ô chữ:")
        for b, t in ket_qua.items(): print(f"{b}: {t}")
    else:
        print("Không tìm thấy lời giải với từ điển gốc.")