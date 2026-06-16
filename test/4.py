from collections import deque

def loang_da_nguon_bao_ve(ma_tran_luoi):
    hang = len(ma_tran_luoi)
    cot = len(ma_tran_luoi[0]) 
    khoang_cach = [[-1] * cot for _ in range(hang)]
    hang_doi = deque()
    
    for r in range(hang):
        for c in range(cot):
            if ma_tran_luoi[r][c] == 'G':
                khoang_cach[r][c] = 0
                hang_doi.append((r, c))
            elif ma_tran_luoi[r][c] == '0' or ma_tran_luoi[r][c] == 'O':
                khoang_cach[r][c] = float('inf')           
    huong_di = [(-1, 0), (1, 0), (0, -1), (0, 1)] 
    
    while hang_doi:
        r, c = hang_doi.popleft()
        kc_hien_tai = khoang_cach[r][c]
        
        for dr, dc in huong_di:
            r_moi, c_moi = r + dr, c + dc
            if 0 <= r_moi < hang and 0 <= c_moi < cot:
                if khoang_cach[r_moi][c_moi] == float('inf'):
                    khoang_cach[r_moi][c_moi] = kc_hien_tai + 1
                    hang_doi.append((r_moi, c_moi))                
    return khoang_cach

if __name__ == "__main__":
    luoi_ngan_hang = [
        ['0', '0', '0', '0', 'G'],
        ['0', 'W', 'W', '0', '0'],
        ['0', '0', '0', 'W', '0'],
        ['G', 'W', 'W', 'W', '0'],
        ['0', '0', '0', '0', 'G']
    ]
    kq_ma_tran = loang_da_nguon_bao_ve(luoi_ngan_hang)
    print("BÀI 4: KẾT QUẢ SỐ BƯỚC CỦA BẢO VỆ")
    for dong in kq_ma_tran:
        print("\t".join(f"{o:>2}" for o in dong))