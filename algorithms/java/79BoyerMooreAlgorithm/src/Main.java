public class Main {
    public static void main(String[] args) {
        char[] charArray = {'a','b','a','b','a','a','b','a','b'};
        char[] charPattern = {'a','b'};
        BoyerMoore bm = new BoyerMoore();
        bm.search(charArray, charPattern);
    }
}