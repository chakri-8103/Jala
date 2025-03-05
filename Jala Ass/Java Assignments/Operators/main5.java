class main5 {
    public static void main(String[] args) {
        boolean a = true, b = false;

        // Logical AND (&&) - returns true if both conditions are true
        System.out.println("Logical AND (a && b): " + (a && b)); // false

        // Logical OR (||) - returns true if at least one condition is true
        System.out.println("Logical OR (a || b): " + (a || b)); // true

        // Logical NOT (!) - reverses the boolean value
        System.out.println("Logical NOT (!a): " + (!a)); // false
        System.out.println("Logical NOT (!b): " + (!b)); // true
    }
}
