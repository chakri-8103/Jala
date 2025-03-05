class main2 {
    static void showIncrementDecrement() {
        int num = 10;
        
        System.out.println("Initial Value: " + num);
        System.out.println("Pre-Increment (++num): " + (++num));
        

        System.out.println("Post-Increment (num++): " + (num++));
        System.out.println("After Post-Increment: " + num);
        

        System.out.println("Pre-Decrement (--num): " + (--num));
        

        System.out.println("Post-Decrement (num--): " + (num--));
        System.out.println("After Post-Decrement: " + num);
    }

    public static void main(String[] args) {

        showIncrementDecrement();
    }
}
