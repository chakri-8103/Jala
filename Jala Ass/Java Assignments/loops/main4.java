class Main4 {
    public static void main(String[] args) {
        System.out.println("Odd numbers:");
        for (int i = 1; i <= 10; i++) {
            if (i % 2 != 0) {
                System.out.println(i);
            }
        }


        System.out.println("Even numbers:");
        for (int i = 1; i <= 10; i++) {
            if (i % 2 == 0) {
                System.out.println(i);
            }
        }
    }
}
