import java.util.List;

public class SuffixTree {

    TreeNode root = new TreeNode();

    public SuffixTree(String text) {
        root.insertSuffix(text);
    }

    public List<Integer> search(String pattern) {
        return root.search(pattern);
    }

    public boolean isSuffix(String pattern) {
        return root.isSuffix(pattern);
    }

    public boolean isSubstring(String pattern) {
        return root.isSubstring(pattern);
    }

}
