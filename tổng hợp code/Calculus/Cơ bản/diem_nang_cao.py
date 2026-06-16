def nhap_diem():
    """Nhập nhiều điểm cho 1 sinh viên"""
    diem_list = []
    while True:
        raw = input("Nhập điểm (Enter để kết thúc): ").strip()
        if raw == "":
            break
        try:
            diem = float(raw)
            if 0 <= diem <= 10:
                diem_list.append(diem)
            else:
                print("Điểm phải trong khoảng 0–10")
        except ValueError:
            print("Vui lòng nhập số hợp lệ")
    return diem_list

def tinh_trung_binh(ds):
    return sum(ds) / len(ds) if ds else 0.0

def xep_loai(tb):
    if tb >= 9:
        return "Giỏi"
    elif tb >= 7:
        return "Khá"
    elif tb >= 5:
        return "Trung bình"
    else:
        return "Yếu"

def nhap_sinh_vien():
    """Nhập thông tin 1 sinh viên"""
    ten = input("Nhập tên sinh viên: ").strip().title()
    diem = nhap_diem()
    tb = tinh_trung_binh(diem)
    loai = xep_loai(tb)
    return {
        "ten": ten,
        "diem": diem,
        "trung_binh": tb,
        "xep_loai": loai
    }

def hien_thi_danh_sach(ds):
    if not ds:
        print("Danh sách trống")
        return
    print("\n=== DANH SÁCH SINH VIÊN ===")
    for i, sv in enumerate(ds, 1):
        print(f"{i}. {sv['ten']} | TB: {sv['trung_binh']:.2f} | {sv['xep_loai']}")

def loc_sinh_vien_gioi(ds):
    print("\n=== SINH VIÊN GIỎI ===")
    found = False
    for sv in ds:
        if sv["xep_loai"] == "Giỏi":
            print(f"- {sv['ten']} ({sv['trung_binh']:.2f})")
            found = True
    if not found:
        print("Không có sinh viên giỏi")

def menu():
    print("""
========= MENU =========
1. Nhập sinh viên
2. Hiển thị danh sách
3. Lọc sinh viên giỏi
4. Thống kê số sinh viên
0. Thoát
========================
""")

def main():
    ds_sinh_vien = []
    while True:
        menu()
        choice = input("Chọn chức năng: ").strip()
        if choice == "1":
            sv = nhap_sinh_vien()
            ds_sinh_vien.append(sv)
            print("Đã thêm sinh viên")
        elif choice == "2":
            hien_thi_danh_sach(ds_sinh_vien)
        elif choice == "3":
            loc_sinh_vien_gioi(ds_sinh_vien)
        elif choice == "4":
            print("Tổng số sinh viên:", len(ds_sinh_vien))
        elif choice == "0":
            print("Thoát chương trình")
            break
        else:
            print("Lựa chọn không hợp lệ")
if __name__ == "__main__":
    main()
