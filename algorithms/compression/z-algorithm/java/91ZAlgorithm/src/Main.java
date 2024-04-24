public class Main {
    public static void main(String[] args) {
        char[] newPatternArray = {'a','b','c'};
        char[] newCharArray = {'a','b','c','a','b','c','a','b','c'};
        ZAlgorithm firstZAlgo = new ZAlgorithm();
        firstZAlgo.search(newPatternArray, newCharArray);
        firstZAlgo.searchAll(newPatternArray, newCharArray);
    }
}