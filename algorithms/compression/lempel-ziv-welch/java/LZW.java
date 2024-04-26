import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class LZW {
    public List<Integer> compress(String text) {
        if (text == null) return null;

        int dictionarySize = 256;
        List<Integer> result = new ArrayList<Integer>();
        Map<String, Integer> dictionary = new HashMap<String, Integer>();
        for(int i=0; i<dictionarySize; i++) {
            dictionary.put("" + (char) i, i);
        }

        String previous = "";
        for(char c : text.toCharArray()) {
            String combined = previous + c;
            if (dictionary.containsKey(combined)) {
                previous = combined;
            } else {
                result.add(dictionary.get(previous));
                dictionary.put(combined, dictionarySize++);
                previous = "" + c;
            }
        }

        if (!previous.equals("")) {
            result.add(dictionary.get(previous));
        }

        return result;
    }

    public String decompress(List<Integer> compressed) {
        if (compressed == null) return null;

        int dictionarySize = 256;
        Map<Integer, String> dictionary = new HashMap<Integer, String>();
        for (int i=0; i<dictionarySize; i++) {
            dictionary.put(i, "" + (char) i);
        }

        String previous = "" + (char)(int) compressed.remove(0);
        StringBuilder result = new StringBuilder(previous);
        for (int j : compressed) {
            String combined;
            if (dictionary.containsKey(j)) {
                combined = dictionary.get(j);
            } else if (j == dictionarySize) {
                combined = previous + previous.charAt(0);
            } else {
                return "-1";
            }

            result.append(combined);
            dictionary.put(dictionarySize++, previous + combined.charAt(0));
            previous = combined;
        }
        return result.toString();
    }
}
