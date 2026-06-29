from simpleai.search import SearchProblem, greedy

class BaiToanTimChuoi(SearchProblem):
    def __init__(self, chuoi_muc_tieu, trang_thai_dau=""):
        super().__init__(initial_state=trang_thai_dau)
        self.chuoi_muc_tieu = chuoi_muc_tieu

    def actions(self, trang_thai):
        if len(trang_thai) < len(self.chuoi_muc_tieu):
            bang_chu_cai = 'abcdefghijklmnopqrstuvwxyz'
            return list(bang_chu_cai + ' ' + bang_chu_cai.upper())
        return []

    def result(self, trang_thai, hanh_dong):
        return trang_thai + hanh_dong

    def is_goal(self, trang_thai):
        return trang_thai == self.chuoi_muc_tieu

    def heuristic(self, trang_thai):
        sai_khac = sum([1 if trang_thai[i] != self.chuoi_muc_tieu[i] else 0 for i in range(len(trang_thai))])
        thieu_hut = len(self.chuoi_muc_tieu) - len(trang_thai)
        return sai_khac + thieu_hut

def in_ket_qua_chuoi(tieu_de, ket_qua):
    print(f"\n--- {tieu_de} ---")
    buoc = 0
    for hanh_dong, trang_thai in ket_qua.path():
        hd_hien_thi = hanh_dong if hanh_dong else "Bắt đầu"
        # Căn lề số bước và hành động để bảng in ra thẳng tắp
        print(f"Bước {buoc:<2} | Hành động: {hd_hien_thi:<8} -> Trạng thái: '{trang_thai}'")
        buoc += 1
    print(f"=> Tổng số bước để đạt mục tiêu: {buoc - 1}")

if __name__ == "__main__":
    chuoi_dich = "Artificial Intelligence"
    trang_thai_dau = ""
    
    bai_toan = BaiToanTimChuoi(chuoi_muc_tieu=chuoi_dich, trang_thai_dau=trang_thai_dau)
    kq_tim_kiem = greedy(bai_toan)
    
    in_ket_qua_chuoi(f"TÌM CHUỖI MỤC TIÊU: '{chuoi_dich}'", kq_tim_kiem)