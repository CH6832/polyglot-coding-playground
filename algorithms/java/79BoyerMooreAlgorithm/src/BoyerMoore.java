/**
 * Boyer Moore Algorithm<br>
 *     This algorithm will search for a pattern into an array of characters and return the
 *     index of the match ot -1 in case of no mach.
 *     This algorithm uses two tables that helps to improve the time complexity and return the
 *     search value in less comparisons than the Brute Force Algorithm
 */
public class BoyerMoore {

    private final int ASCII_TABLE_SIZE = 256;

    /**
     * This method will use the tables of Good Suffix and BAd Character to decide how many
     * comparison are possible to skip. Which one that computes ore comparisons the search will
     * use to optimize the search
     *
     * abcdbabaibai
     *    baibai
     *
     * @param array
     * @param pattern
     * @return
     */
    public int search(char[] array, char[] pattern) {
        if (pattern == null || pattern.length == 0) return 0;
        if (array == null) return -1;

        int[] badCharTable = precomputeBadCharTable(pattern);
        int[] suffixTable = preprocessSuffixTable(pattern);
        for (int i=pattern.length-1, j; i<array.length;) {
            for(j=pattern.length-1; pattern[j]==array[i]; --i, --j) {
                if (j==0) return i;
            }
            i += Math.max(suffixTable[pattern.length - 1 - j], badCharTable[array[i]]);
        }
        return -1;
    }

    /**
     *
     * This method pre-processes the Good Suffix Table
     *
     * abcdbabaibai
     * baibai
     * 1st round 6,7,8,9,10,11
     *
     * @param pattern
     * @return
     */
    public int[] preprocessSuffixTable(char[] pattern) {
        int[] table = new int[pattern.length];
        computePrefix(pattern, table);
        computeSuffix(pattern, table);
        return table;
    }

    /**
     * This method creates  the bad character table.
     * It will add pattern.length to every character that is not in the pattern.
     * It will also add pattern.length to the last character of the patter in case it is unique.
     *
     * test as in test
     * 121
     *
     * ab* as in abc
     * 213
     * max(1, p.length - index - 1)
     * @param pattern
     * @return
     */
    public int[] precomputeBadCharTable(char[] pattern) {
        int[] table = new int[ASCII_TABLE_SIZE];
        for (int i=0; i<ASCII_TABLE_SIZE; i++) {
            table[i] = pattern.length;
        }

        for (int t=0; t<pattern.length-1; t++) {
            table[pattern[t]] = Math.max(1, pattern.length - t - 1);
        }

        if (table[pattern[pattern.length-1]] < pattern.length) {
            table[pattern[pattern.length-1]]  = 1;
        }
        return table;
    }


    public void computePrefix(char[] pattern, int[] table) {
        int lastPrefixPosition = pattern.length;
        for(int i=pattern.length; i>0; --i) {
            if (isPrefix(pattern, i)) lastPrefixPosition = i;
            table[pattern.length - i] = lastPrefixPosition - i + pattern.length;
        }
    }


    public void computeSuffix(char[] pattern, int[] table) {
        for (int i=0; i<pattern.length-1; ++i) {
            int len = suffixLength(pattern, i);
            table[len] = pattern.length - 1 - i + len;
        }
    }


    /**
     * baibai
     *   j  i
     * @param pattern
     * @param index
     * @return
     */
    public boolean isPrefix(char[] pattern, int index) {
        for(int i=index, j=0; i < pattern.length; ++i, ++j) {
            if (pattern[i] != pattern[j]) return false;
        }
        return true;
    }

    /**
     * baidai
     * i    j
     *
     * @param pattern
     * @param index
     * @return
     */
    public int suffixLength(char[] pattern, int index) {
        int len = 0;
        int j = pattern.length - 1;
        for(int i=index; i>=0 && pattern[i] == pattern[j]; --i, --j) {
            len++;
        }
        return len;
    }

}
