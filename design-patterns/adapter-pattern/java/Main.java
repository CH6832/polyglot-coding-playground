public class Main {
    public static void main(String[] args) {
        Adaptee adaptee = new Adaptee();
        Adapter adapter = new Adapter(adaptee);
        clientCode(adapter);
    }

    public static void clientCode(Target target) {
        System.out.println(target.request());
    }
}
