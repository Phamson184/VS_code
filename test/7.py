def xep_lich_co_ten(danh_sach_cv, so_nhan_vien):
    cv_da_sap_xep = sorted(danh_sach_cv, key=lambda x: x[1], reverse=True)
    bang_phan_cong = [[] for _ in range(so_nhan_vien)]
    tong_thoi_gian = [0] * so_nhan_vien
    
    for ten_cv, thoi_gian in cv_da_sap_xep:
        vi_tri_nv = tong_thoi_gian.index(min(tong_thoi_gian))
        bang_phan_cong[vi_tri_nv].append(f"{ten_cv} ({thoi_gian} tuần)")
        tong_thoi_gian[vi_tri_nv] += thoi_gian
        
    return bang_phan_cong, tong_thoi_gian

if __name__ == "__main__":
    danh_sach_du_an = [
    ("A- Xây dựng bộ phận bên trong", 2),
    ("B- Sửa chữa mái và sàn",        3),
    ("C- Xây ống gom khói",           2),
    ("D- Đổ bê tông và xây khung",    4),
    ("E- Xây cửa lò chịu nhiệt",      4),
    ("F- Lắp đặt hệ thống kiểm soát", 3),
    ("G- Lắp đặt thiết bị lọc khí",   5),
    ("H- Kiểm tra và thử nghiệm",     2),
]

    so_nhan_vien = 4

    print("\nKẾT QUẢ XẾP LỊCH BÀI 5 (4 NHÂN VIÊN):")
    kq_phan_cong, kq_thoi_gian = xep_lich_co_ten(danh_sach_du_an, so_nhan_vien)

    for i in range(so_nhan_vien):
        ds_cv = ", ".join(kq_phan_cong[i])
        print(f"Nhân viên {i+1} | Tổng tuần: {kq_thoi_gian[i]:<2} | Gồm: {ds_cv}")

    print(f"\n=> Tổng thời gian của dự án: {max(kq_thoi_gian)} tuần")