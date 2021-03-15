import java.util.Scanner;
public class test {
        public static void main(String[] args)
        {        
        Scanner sc=new Scanner(System.in);
        int a=sc.nextInt(),b=sc.nextInt();
        if(a>1000||-a>1000)
        {
            System.out.println("|a|>100");
        }
        else System.out.println(a+b);
        sc.close();
    }        
}
