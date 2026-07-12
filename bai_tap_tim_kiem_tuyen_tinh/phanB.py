from typing import List, Tuple, Optional
#6
def tim_kiem(a:List[int], x:int)->int:
    for i in range(len(a)):
        if a[i]==x:
            return i
    return -1
#7
def ton_tai(a:List[int],x:int)->bool:
    for e in a:
        if e==x:
            return True
    return False
#8
def dem(a:List[int],x:int)->int:
    c=0
    for q in a:
        if q==x:
            c+=1
    return c
#9
def tat_ca(a:List[int],x:int)->List[int]:
    vi_tri=[]
    for i in range(len(a)):
        if a[i]==x:
            vi_tri.append(i)
    return vi_tri
#10
def cuoi(a:List[int],x:int)->int:
    for i in range(len(a)-1,-1,-1):
        if a[i]==x:
            return i
    return -1
#11
def tmax(a:List[int])->Tuple[Optional[int],int]:
    if not a: return None,-1
    b=a[0]
    c=0
    for i in range(1,len(a)):
        if a[i]>b:
            b=a[i]
            c=i
    return b,c
#12
def min_max(a:List[int])->Tuple[Optional[int],Optional[int]]:
    if not a: return None, None
    min_gt=max_gt=a[0]
    min_i=max_i=0
    for i in range(1,len(a)):
        if a[i]>max_gt:
            max_gt=a[i]
            max_i=i
        elif a[i]<min_gt:
            min_gt=a[i]
            min_i=i
    print(f"Min là {min_gt} tại vị trí {min_i}")
    print(f"Max là {max_gt} tại vị trí {max_i}")
    return min_gt,max_gt
def main():
    test=[2,5,2,7,2,9,1]
    print("Bài 6 Vị trí đầu tiên của 7:",tim_kiem(test,7))
    print("Bài 7 Số 5 có tồn tại không",ton_tai(test,5))
    print("Bài 8 Số lần xuất hiện của 2:",dem(test,2))
    print("Bài 9 Các vị trí của 2:",tat_ca(test,2))
    print("Bài 10 Vị trí cuối cùng của 2:",cuoi(test,2))
    max_gt,max_i=tmax(test)
    print(f"Bài 11 Giá trị lớn nhất là {max_gt} tại vị trí {max_i}")
    print("Bài 12 Min và Mã trong 1 lần duyệt:")
    min_max(test)
if __name__=='__main__':
    main()            
    