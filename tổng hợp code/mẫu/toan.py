import sympy as sp
#1
sp.init_printing(use_unicode=True)
x=sp.symbols('x',real=True)
def ham_so(expr,limit_point,int_bounds,taylor_order):
    print('Phân tích hàm số 1 biến')
    print('Hàm f(x)=')
    sp.pprint(expr)
    #Giới hạn
    lim_a=sp.limit(expr,x,limit_point)
    print(f"\n1. Giới hạn khi x->{limit_point}:")
    sp.pprint(lim_a)
    #Đạo hàm
    derivative=sp.simplify(sp.dif(expr,x))
    print("\n2. Đạo hàm f'(x)=")
    sp.pprint(derivative)
    #Tích phân xác định
    integral_a=sp.integrate(expr,(x,int_bounds[0],int_bounds[1]))
    print(f"\n3. Tích phân từ {int_bounds[0],int_bounds[1]}:")
    sp.pprint(integral_a)
    #Chiều dài đường cong
    cong=sp.sqrt(1+derivative**2)
    dai=sp.integrate(cong,(x,int_bounds[0],int_bounds[1]))
    print(f"\n4. Chiều dài đường cong: {sp.N(dai):.4f}")
    #Taylor
    taylor=sp.series=sp.series(expr,x,x0=0,n=taylor_order).removeO()
    print(f"\n5. Khai triển Taylor bậc {taylor_order-1} quanh x=0:")
    sp.pprint(taylor)
    print("-"*40)
if __name__=="__main__":
    f=sp.sin(x)*sp.exp(-x)
    ham_so(
        expr=f,
        limit_point=sp.oo,
        int_bounds=(0,sp.pi),
        taylor_order=5
    )
#2
sp.init_printing(use_unicode=True)
x,y=sp.symbols('x y',real=True)
def toi_uu(expr):
    print("Tối ưu hàm nhiều biến")
    print("Hàm số f(x, y)="); sp.pprint(expr)
    #đạo hàm bậc 1
    a=[sp.dif(expr,b) for b in (x,y)]
    a_matrix=sp.Matrix(a)
    print("\n1. Vector Gradient =")
    sp.pprint(a_matrix)
    #Điểm tới hạn =0
    c=sp.solve(a,(x,y),dict=True)
    print("\n2. Các điểm tới hạn:")
    for pt in c:
        print(pt)
    #Hessian bậc 2
    hessian=sp.hessian(expr,(x,y))
    print("\n3. Ma trận Hessian H=")
    sp.pprint(hessian) 
    #Phân loại
    print("\n4. Phân loại điểm tới hạn:")
    for pt in c:
        if not pt: continue
        H_pt=hessian.subs(pt)
        det_H=H_pt.det()
        f_xx=H_pt[0,0]
        print(f" Tại điểm {pt}:")
        if det_H>0 and f_xx>0:
            print("-> Cực tiểu địa phương")
        elif det_H>0 and f_xx<0:
            print("-> Cực đại địa phương")
        elif det_H<0:
            print("->Điểm yên ngựa")
        else:
            print("->Không thể kết luận")
if __name__=="__main__":
    ham=x**3-3*x+y**3-3*y
    toi_uu(ham)
#3
sp.init_printing(use_unicdoe=True)
x,y,z=sp.symbols('x y z',real=True)
def matran(a,b):
    print("Ma trận Jacobian") 
    #Khởi tạo
    f=sp.Matrix(a)
    x=sp.Matrix(b)
    print("Hệ hàm F=")
    sp.pprint(f)
    # Jacobian
    j=f.jacobian(x)
    print("\n Ma trận Jacobian j=")
    sp.pprint(j)
    #Đánh giá
    diem={x:1,y:2,z:0}
    dg=j.subs(diem)
    print(f"\n Giá trị Jacobian tại {diem} =")
    sp.pprint(dg)
if __name__=="__main__":
    anh_xa=[
        x**2*y*sp.cos(z),
        x+y**2+sp.sin(z)
    ]  
    list=[x,y,z]
    matran(anh_xa,list)
#4
sp.init_printing(use_unicode=True)
n=sp.symbols('n',integer=True,positive=True)
def chuoi_vo_han(a):
    print("Chuỗi vô hạn")
    print("Số hạng tổng quát a="); sp.pprint(a)
    #kiểm tra tỷ số
    b=a.subs(n,n+1)
    do=sp.Abs(b/a)
    do_gh=sp.limit(do,n,sp.oo)
    print(f"\n Giới hạn tỷ số L={do_gh}")
    if do_gh<1:
        print("->Chuỗi hội tụ tuyệt đối")
    elif do_gh>1:
        print("->Chuỗi phân kỳ")
    else:
        print("->Tiêu chuẩn ty số không kết luận được")
    #Tính tổng
    chuoi=sp.Sum(a,(n,1,sp.oo))
    print("\ Biểu thức tổng: "); sp.pprint(chuoi) 
    try:
        kq=chuoi.doit()
        print("\ Kết quả: "); sp.pprint(kq)
    except sp.SympifyError:
        print("\n Khổng thể tính tổng chính xác bằng phương pháp giải tích")       
if __name__=="__main__":
    mau=(2**n)/sp.factorial(n) 
    chuoi_vo_han(mau)