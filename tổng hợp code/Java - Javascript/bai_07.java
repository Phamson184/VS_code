import java.util.Scanner;
public class bai_07 {
    public static void main(String[]args){
        Scanner sc = new Scanner (System.in);
        System.out.print("Nhap mot so nguyen: ");
        int n=sc.nextInt();
        if(n>0){
            System.out.println("day la so nguyen duong");
        } else if (n<0){
            System.out.println("day la so nguyen am");
        } else {
            System.out.println("so nhap vao la 0");
        }
        sc.close();
    }
    
}
