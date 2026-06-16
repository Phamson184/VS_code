def tinh_tien_ho_tro(hoc_phi,tong_quy,so_luong,tile):
    nhom=input('nhập nhóm (1, 2, 3a, 3b, 4): ').strip().lower()
    if nhom not in tile:
        print(f'Nhoms {nhom} không hợp lệ! các nhóm hợp lệ: {', '.join(tile.keys())}')
        return
    tien_sv=hoc_phi*tile[nhom]
    print(f'Sinh viên nhóm {nhom} nhận: {tien_sv:,.0f}VND')
    print(f'\n{'Nhóm:<5'}{'Số lượng':>10}{'Tổng tiền':>20}')
    tong_ho_tro=0
    for i in so_luong:
        tien=so_luong[i]*hoc_phi*tile[i]
        tong_ho_tro+=tien
        print(f'{i:<5}{so_luong[i]:>10}{tien:>20,.0f}')
    print(f'\n Tổng hỗ trợ toàn trường {tong_ho_tro:,.0f}VND')
    print("trạng thái:","chưa vượt 3 tỷ"if tong_ho_tro<=tong_quy else 'Đã vượt 3 tỷ')
hoc_phi=20_000_000
tong_quy=3_000_000_000
so_luong = {"1": 200, "2": 120, "3a": 100, "3b": 80, "4": 300}
tile = {"1": 0.20, "2": 0.30, "3a": 0.15, "3b": 0.08, "4": 0.05}
tinh_tien_ho_tro(hoc_phi,tong_quy,so_luong,tile)