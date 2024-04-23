public class Main {
    public static void main(String[] args) {
        String eampleText = "aabaaca";
        SuffixTree sftree = new SuffixTree(eampleText);
        sftree.isSubstring("ab");
    }
}