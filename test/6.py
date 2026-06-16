def tim_may_ranh_nhat(thoi_gian_may):
    return thoi_gian_may.index(min(thoi_gian_may))

def xep_lich(cong_viec, so_may=3):
    cv_da_sap_xep = sorted(cong_viec, reverse=True)
    phan_cong = [[] for _ in range(so_may)]
    thoi_gian_may = [0] * so_may
    
    for cv in cv_da_sap_xep:
        vi_tri_may = tim_may_ranh_nhat(thoi_gian_may)
        phan_cong[vi_tri_may].append(cv)
        thoi_gian_may[vi_tri_may] += cv
        
    return phan_cong, thoi_gian_may

if __name__ == "__main__":
    ds_cong_viec = [2, 5, 8, 1, 5, 1]
    so_may = 3
    
    print("KẾT QUẢ XẾP LỊCH BÀI 4:")
    kq_phan_cong, kq_thoi_gian = xep_lich(ds_cong_viec, so_may)
    
    for i in range(so_may):
        print(f"Máy {i+1}: Các công việc {kq_phan_cong[i]} -> Tổng thời gian = {kq_thoi_gian[i]} giờ")
        
    print(f"\n=> Tổng thời gian hoàn tất tất cả: MAX({kq_thoi_gian}) = {max(kq_thoi_gian)} giờ")