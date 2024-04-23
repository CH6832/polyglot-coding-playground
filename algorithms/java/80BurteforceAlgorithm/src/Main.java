public class Main {
    public static void main(String[] args) {
        char[] charArray = {'a','b','a','b','a','a','b','a','b'};
        char[] charPattern = {'a','b'};
        BruteForce brfrce = new BruteForce();
        brfrce.firstMatch(charArray, charPattern);
        brfrce.everyMatch(charArray, charPattern);
    }
}