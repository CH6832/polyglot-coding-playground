public class Main {
    public static void main(String[] args) {
        char[] charArray = {'a','b','a','b','a','a','b','a','b'};
        char[] charPattern = {'a','b'};
        BruteForce bruteforce = new BruteForce();
        bruteforce.firstMatch(charArray, charPattern);
        bruteforce.everyMatch(charArray, charPattern);
    }
}