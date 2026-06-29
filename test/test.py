from graphviz import Graph

# Khởi tạo đồ thị với engine 'neato'
dot = Graph('ERD', engine='neato', format='jpg')
dot.attr(dpi='300', size='15,10') 
dot.attr(overlap='false', splines='true') # Chống đè khối và uốn đường cong mượt

# --- HÀM HỖ TRỢ PHÓNG TO TỌA ĐỘ ---
# Nhân tọa độ lên 120 lần (tránh Graphviz bị kẹt vì các khối quá gần nhau)
SCALE = 120
def p(x, y):
    return f"{x * SCALE},{y * SCALE}!"

# --- STYLE CHUNG ---
dot.attr('node', fontname='Arial', fontsize='11', style='filled')
dot.attr('edge', fontname='Arial', fontsize='11', penwidth='1.5')

# ==========================================
# 1. THỰC THỂ (Entities - Hình chữ nhật xanh)
# ==========================================
dot.attr('node', shape='box', fillcolor='#388E3C', fontcolor='white', width='1.4', height='0.6', peripheries='1')
dot.node('NV', 'NHANVIEN', pos=p(0, 4))
dot.node('PB', 'PHONGBAN', pos=p(0, 0))
dot.node('DA', 'DEAN', pos=p(6, 0))

# Thực thể yếu (2 viền)
dot.attr('node', peripheries='2')
dot.node('TN', 'THANNHAN', pos=p(6, 4))

# ==========================================
# 2. MỐI LIÊN KẾT (Relationships - Hình thoi vàng)
# ==========================================
dot.attr('node', shape='diamond', fillcolor='#DCE775', fontcolor='black', width='1.1', height='0.6', peripheries='1')
dot.node('QL', 'Quản lý', pos=p(0, 6))
dot.node('ThuocNV', 'Thuộc', pos=p(-1, 2))
dot.node('PT', 'Phụ trách', pos=p(1, 2))
dot.node('PC', 'Phân công', pos=p(3, 2))
dot.node('ThuocPB', 'Thuộc', pos=p(3, 0))

# Mối liên kết yếu (2 viền)
dot.attr('node', peripheries='2')
dot.node('Co', 'Có', pos=p(3, 4))

# ==========================================
# 3. THUỘC TÍNH (Attributes - Hình Oval trắng)
# ==========================================
dot.attr('node', shape='ellipse', fillcolor='white', fontcolor='black', width='0.9', height='0.4', peripheries='1')

# --- Cụm Nhân Viên ---
dot.node('MANV', '<<U>MANV</U>>', pos=p(1.5, 4.8))
dot.node('HOTENNV', 'HOTENNV', pos=p(-1.5, 5.5))
dot.node('NGSINH_NV', 'NGSINH', pos=p(-2.5, 4.8))
dot.node('PHAI_NV', 'PHAI', pos=p(-2.5, 2.5))
dot.node('LUONG', 'LUONG', pos=p(-1.5, 1.2))
# Thuộc tính phức hợp Địa chỉ
dot.node('DIACHI', 'DIACHI', pos=p(-3, 3.5))
dot.node('QUAN', 'QUAN', pos=p(-4.5, 4.5))
dot.node('TP', 'TP', pos=p(-4.5, 2.5))

# --- Cụm Phòng Ban ---
dot.node('MAPHG', '<<U>MAPHG</U>>', pos=p(-2.5, 1.5))
dot.node('TENPHG', 'TENPHG', pos=p(-3, 0))
dot.node('NG_NC', 'NG_NC', pos=p(-2.5, -1.5))
# Đa trị
dot.attr('node', peripheries='2')
dot.node('DIADIEM', 'DIADIEM', pos=p(0, -1.5))
dot.attr('node', peripheries='1')

# --- Cụm Đề Án ---
dot.node('TENDA', 'TENDA', pos=p(4.5, -1.5))
dot.node('DDIEM_DA', 'DDIEM_DA', pos=p(7, -1.5))
dot.node('MADA', '<<U>MADA</U>>', pos=p(8, 1))

# --- Cụm Thân Nhân ---
dot.node('TENTN', '<<U>TENTN</U>>', pos=p(4.5, 5.5))
dot.node('PHAI_TN', 'PHAI', pos=p(6.5, 5.5))
dot.node('NGSINH_TN', 'NGSINH', pos=p(8.5, 5))
dot.node('QUANHE', 'QUANHE', pos=p(8.5, 3))

# Thuộc tính của liên kết Phân công
dot.node('THOIGIA', 'THOIGIA', pos=p(4.5, 2.5))

# ==========================================
# 4. KẾT NỐI VÀ LƯỢNG SỐ (Edges)
# ==========================================
dot.attr('edge', dir='none', penwidth='1.2')
attr_edges = [
    ('NV', 'MANV'), ('NV', 'HOTENNV'), ('NV', 'NGSINH_NV'), ('NV', 'PHAI_NV'), ('NV', 'LUONG'), ('NV', 'DIACHI'),
    ('DIACHI', 'QUAN'), ('DIACHI', 'TP'),
    ('PB', 'MAPHG'), ('PB', 'TENPHG'), ('PB', 'NG_NC'), ('PB', 'DIADIEM'),
    ('DA', 'MADA'), ('DA', 'TENDA'), ('DA', 'DDIEM_DA'),
    ('TN', 'TENTN'), ('TN', 'PHAI_TN'), ('TN', 'NGSINH_TN'), ('TN', 'QUANHE'),
    ('PC', 'THOIGIA')
]
for u, v in attr_edges:
    dot.edge(u, v)

# Hàm hỗ trợ vẽ đường liên kết với ký hiệu Lượng số (Crow's foot)
def add_cardinality(u, rel, v, tail, head):
    dot.edge(u, rel, arrowtail=tail, arrowhead='none', dir='back')
    dot.edge(rel, v, arrowtail='none', arrowhead=head)

dot.attr('edge', dir='both', penwidth='1.5')

# NV (N) - Thuộc - (1) PB
add_cardinality('NV', 'ThuocNV', 'PB', 'crow', 'tee')
# NV (1) - Phụ trách - (1) PB
add_cardinality('NV', 'PT', 'PB', 'tee', 'tee')
# NV (1) - Có - (N) TN
add_cardinality('NV', 'Co', 'TN', 'tee', 'crow')
# NV (N) - Phân công - (N) DA
add_cardinality('NV', 'PC', 'DA', 'crow', 'crow')
# PB (1) - Thuộc - (N) DA
add_cardinality('PB', 'ThuocPB', 'DA', 'tee', 'crow')

# Xử lý vòng Quản lý đệ quy (1 - N)
dot.edge('NV', 'QL', arrowtail='tee', arrowhead='none', dir='back')
dot.edge('QL', 'NV', arrowtail='none', arrowhead='crow')

# ==========================================
# 5. XUẤT FILE 
# ==========================================
# Nhớ thay MSSV và Họ tên của bạn vào đây nhé!
file_name = '0202-MSSV-HoTen-PracticeAssignment-Session-4'
dot.render(file_name, view=True, cleanup=True)
print(f"\n[+] Xuất sắc! Ảnh đã được render và lưu tại: {file_name}.png")