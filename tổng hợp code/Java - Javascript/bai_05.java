public class bai_05 {
    public static void main(String[]args){
        double a=5;
        double b=4;
        double c=3;
        double nuaChuvi=(a+b+c)/2;
        double chuVi=nuaChuvi*2;
        double dienTich=Math.sqrt(nuaChuvi*(nuaChuvi-a)*(nuaChuvi-b)*(nuaChuvi-c));
        System.out.println("Nua chu vi hinh tam giac = "+nuaChuvi);
        System.out.println("Chu vi hinh tam giac = "+chuVi);
        System.out.println("Dien tich hinh tam giac = "+ dienTich);
    }
    
}
