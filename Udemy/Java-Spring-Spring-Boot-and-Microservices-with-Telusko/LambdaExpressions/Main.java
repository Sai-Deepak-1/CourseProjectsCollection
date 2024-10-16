import java.util.*;

@FunctionalInterface
interface Square {
    int area(int x);
}

public class Main{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter a number: ");
        int x = sc.nextInt();
        Square s = (i) -> (int)Math.pow(i, 2);
        System.out.println(s.area(x));
        sc.close();
    }
}