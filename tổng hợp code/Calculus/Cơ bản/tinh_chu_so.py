def phan_tich(money: int, so_luong_chu_so: int):
    ten_so_hang = [
        "đơn vị", "chục", "trăm", "nghìn", "chục nghìn", "trăm nghìn",
        "triệu", "chục triệu", "trăm triệu", "tỷ", "chục tỷ", "trăm tỷ", "nghìn tỷ"
    ]
    chu_so_tieng_viet = ["không", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]

    print(f"\nPhân tích số {money:,} theo các hàng:")

    tong = 0
    chua_so_0 = False
    so_tam = money

    for i in range(so_luong_chu_so):
        if so_tam == 0:
            break
        chu_so = so_tam % 10
        tong += chu_so
        if chu_so == 0:
            chua_so_0 = True

        hang = ten_so_hang[i] if i < len(ten_so_hang) else f"hàng thứ {i+1}"
        chu = chu_so_tieng_viet[chu_so]
        print(f"Chữ số hàng {hang:12s}: {chu_so} ({chu})")
        so_tam //= 10

    print("\n--- Kết quả tổng hợp ---")
    print(f"Tổng các chữ số của {money:,} là: {tong}")
    print(f"Trung bình các chữ số: {tong / len(str(money)):.2f}")
    if chua_so_0:
        print("Số này có chứa chữ số 0.")
    if tong % 3 == 0:
        print("Số này chia hết cho 3.")
    if tong % 9 == 0:
        print("Số này chia hết cho 9.")


# --- Chạy thử ---
money = int(input("Nhập số tiền: "))
so_luong_chu_so = len(str(money))
phan_tich(money, so_luong_chu_so)
