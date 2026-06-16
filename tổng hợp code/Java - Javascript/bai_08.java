import java.util.Scanner;
public class bai_08 {
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        System.out.print("Nhap mot so nguyen duong n: ");
        int n =sc.nextInt();
        int tongChan = 0;
        int tongLe=0;
        for (int i=1; i <= n;i++){
            if (i%2==0){
                tongChan+=i;
            }else{
                tongLe+=i;
            }
        }
        System.out.println("tong cac so chan la: "+tongChan);
        System.out.println("tong cac so le la: "+tongLe);
        sc.close();
    }
}
