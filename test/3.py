from collections import deque

def bfs_quan_ma(bat_dau, muc_tieu, diem_hop_le):
    huong_di = [
        (-2, -1), (-2, 1), (-1, -2), (-1, 2),
        (1, -2), (1, 2), (2, -1), (2, 1)
    ]
    hang_doi = deque([(bat_dau, [bat_dau])])
    da_tham = {bat_dau}
    
    while hang_doi:
        hien_tai, duong_di = hang_doi.popleft()
        if hien_tai == muc_tieu:
            return duong_di

        for dr, dc in huong_di:
            diem_moi = (hien_tai[0] + dr, hien_tai[1] + dc)
            
            # Chỉ đi tiếp nếu điểm mới là điểm hợp lệ (chấm trắng) và chưa thăm
            if diem_moi in diem_hop_le and diem_moi not in da_tham:
                da_tham.add(diem_moi)
                hang_doi.append((diem_moi, duong_di + [diem_moi]))           
    return []

if __name__ == "__main__":
    tap_diem_trang = {
        (0, 1), (0, 7), 
        (1, 3), 
        (2, 2), 
        (3, 4), (3, 7), 
        (4, 2), 
        (5, 0)
    }
    
    diem_xuat_phat = (1, 3)
    diem_dich = (5, 0)
    print("BÀI 3: MÔ PHỎNG ĐƯỜNG ĐI CỦA QUÂN MÃ")
    kq_duong_di = bfs_quan_ma(diem_xuat_phat, diem_dich, tap_diem_trang)
    
    if kq_duong_di:
        chuoi_duong_di = " -> ".join([str(toa_do) for toa_do in kq_duong_di])
        print(f"Từ {diem_xuat_phat} đến {diem_dich}:")
        print(f"Đường đi: {chuoi_duong_di}")
        print(f"Tổng số bước (ít nhất): {len(kq_duong_di) - 1}")
    else:
        print("Không tìm thấy đường đi hợp lệ trên các chấm trắng.")
