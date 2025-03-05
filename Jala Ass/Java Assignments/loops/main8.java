import java.util.Scanner;

class main8 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter a number: ");
        int num = scanner.nextInt();
        int originalNum = num;
        int sum = 0;
        int digits = 0;
        
        while (num != 0) {
            num /= 10;
            digits++;
        }
        
        num = originalNum;
        while (num != 0) {
            int remainder = num % 10;
            sum += Math.pow(remainder, digits);
            num /= 10;
        }
        
        if (sum == originalNum) {
            System.out.println(originalNum + " is an Armstrong number.");
        } else {
            System.out.println(originalNum + " is not an Armstrong number.");
        }
        
        scanner.close();
    }
}
