class Main5 {
    int num = 10;

    void display() {
        int num = 20;
        System.out.println("Local variable: " + num);
        System.out.println("Global variable: " + this.num);
    }

    public static void main(String[] args) {
        Main5 obj = new Main5();
        obj.display();
    }
}
