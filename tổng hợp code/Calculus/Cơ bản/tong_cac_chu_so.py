so=input('nhập nhiều số(trong 1000) cách nhau bởi dấu cách: ').split()
for i in so:
    n=int(i)
    if 0<n<1000:
        tong=sum(map(int,str(n)))
        print(f'{n}->Tổng các chữ số={tong}')
    else:
        print(f'{n}Không hợp lệ(từ 1-999).')