def tim_may_ranh_nhat(thoi_gian_may):
    return thoi_gian_may.index(min(thoi_gian_may))

def xep_lich_tren_may(danh_sach_cv, so_may=3):
    phan_cong = [[] for _ in range(so_may)]
    thoi_gian_may = [0] * so_may
    
    for cv in danh_sach_cv:
        idx = tim_may_ranh_nhat(thoi_gian_may)
        phan_cong[idx].append(cv['id'])
        thoi_gian_may[idx] += cv['dur']   
    return phan_cong, thoi_gian_may

def in_ket_qua(tieu_de, phan_cong, thoi_gian_may):
    print(f"\n--- {tieu_de} ---")
    for i in range(len(phan_cong)):
        print(f"Máy {i+1} | Khối lượng: {thoi_gian_may[i]:>2} tuần | Các công việc: {' -> '.join(phan_cong[i])}")
    print(f"=> Tổng thời gian hoàn thành: {max(thoi_gian_may)} tuần")

if __name__ == "__main__":
    cong_viec = [
        {'id': 'A', 'dur': 2, 'es': 0, 'ls': 0, 'slack': 0, 'gang': True},
        {'id': 'B', 'dur': 3, 'es': 0, 'ls': 1, 'slack': 1, 'gang': False},
        {'id': 'C', 'dur': 2, 'es': 2, 'ls': 2, 'slack': 0, 'gang': True},
        {'id': 'D', 'dur': 4, 'es': 3, 'ls': 4, 'slack': 1, 'gang': False},
        {'id': 'E', 'dur': 4, 'es': 4, 'ls': 4, 'slack': 0, 'gang': True},
        {'id': 'F', 'dur': 3, 'es': 4, 'ls': 10, 'slack': 6, 'gang': False}, 
        {'id': 'G', 'dur': 5, 'es': 8, 'ls': 8, 'slack': 0, 'gang': True},
        {'id': 'H', 'dur': 2, 'es': 13, 'ls': 13, 'slack': 0, 'gang': True}
    ]

    ds_gang = [cv for cv in cong_viec if cv['gang']]
    ds_khong_gang = [cv for cv in cong_viec if not cv['gang']]
    ds_xen_ke = []
    for i in range(max(len(ds_gang), len(ds_khong_gang))):
        if i < len(ds_gang):
            ds_xen_ke.append(ds_gang[i])
        if i < len(ds_khong_gang):
            ds_xen_ke.append(ds_khong_gang[i])

    pc_a, tg_a = xep_lich_tren_may(ds_xen_ke, 3)
    in_ket_qua("YÊU CẦU A: XẾP LỊCH XEN KẼ (GĂNG / KHÔNG GĂNG)", pc_a, tg_a)

    cv_du_tru_thap = [cv for cv in cong_viec if cv['slack'] <= 3]
    cv_trien_khai_cham = sorted(cv_du_tru_thap, key=lambda x: x['ls'])
    pc_b, tg_b = xep_lich_tren_may(cv_trien_khai_cham, 3)
    in_ket_qua("YÊU CẦU B: TRIỂN KHAI CHẬM (SLACK <= 3, ƯU TIÊN LS)", pc_b, tg_b)

    pc_c, tg_c = xep_lich_tren_may(cv_du_tru_thap, 3)
    in_ket_qua("YÊU CẦU C: TRIỂN KHAI CHẬM (SLACK <= 3, GIỮ TRẬT TỰ A->H)", pc_c, tg_c)