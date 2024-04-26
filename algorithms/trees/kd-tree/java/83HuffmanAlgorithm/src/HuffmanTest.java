import org.junit.Assert;
import org.junit.Before;
import org.junit.Test;

import java.util.PriorityQueue;

public class HuffmanTest {
    Huffman h;
    @Before
    public void init() {
        h = new Huffman();
    }
    @Test
    public void createFrequencyTableTest() {
        int[] frequencies = h.createFrequencyTable("aabbbcd".toCharArray());
        Assert.assertEquals(h.CHARACTER_LIMIT, frequencies.length);
        Assert.assertEquals(2, frequencies[97]);
        Assert.assertEquals(3, frequencies[98]);
        Assert.assertEquals(1, frequencies[99]);
        Assert.assertEquals(1, frequencies[100]);
    }

    @Test
    public void createPriorityQueueTest() {
        int[] frequencies = h.createFrequencyTable("aabbbcd".toCharArray());
        PriorityQueue<HuffmanNode> queue = h.createPriorityQueue(frequencies);
        // c=1 d=1 a=2 b=3
        Assert.assertEquals('c', queue.peek().c);
        Assert.assertEquals(1, queue.poll().frequency);

        // d=1 a=2 b=3
        Assert.assertEquals('d', queue.peek().c);
        Assert.assertEquals(1, queue.poll().frequency);

        // a=2 b=3
        Assert.assertEquals('a', queue.peek().c);
        Assert.assertEquals(2, queue.poll().frequency);

        // b=3
        Assert.assertEquals('b', queue.peek().c);
        Assert.assertEquals(3, queue.poll().frequency);

        Assert.assertEquals(0, queue.size());

        Assert.assertEquals("\u0001:a2:b3:c1:d1\u0002", h.header.toString());
    }

    @Test
    public void pullLeastUsedAsNodeTest() {
        int[] frequencies = h.createFrequencyTable("aabbbcd".toCharArray());
        PriorityQueue<HuffmanNode> queue = h.createPriorityQueue(frequencies);

        // c=1 d=1 a=2 b=3
        HuffmanNode root = h.pullLeastUsedAsNode(queue);
        // a=2 b=3
        Assert.assertEquals('-', root.c);
        Assert.assertEquals(2, root.frequency);

        Assert.assertEquals('c', root.left.c);
        Assert.assertEquals(1, root.left.frequency);
        Assert.assertNull(root.left.left);
        Assert.assertNull(root.left.right);

        Assert.assertEquals('d', root.right.c);
        Assert.assertEquals(1, root.right.frequency);
        Assert.assertNull(root.right.left);
        Assert.assertNull(root.right.right);


        root = h.pullLeastUsedAsNode(queue);
        // empty
        Assert.assertEquals('-', root.c);
        Assert.assertEquals(5, root.frequency);

        Assert.assertEquals('a', root.left.c);
        Assert.assertEquals(2, root.left.frequency);
        Assert.assertNull(root.left.left);
        Assert.assertNull(root.left.right);

        Assert.assertEquals('b', root.right.c);
        Assert.assertEquals(3, root.right.frequency);
        Assert.assertNull(root.right.left);
        Assert.assertNull(root.right.right);
    }

    /**
     *          aabbbcd
     *
     *              -7
     *          b3      -4
     *              a2      -2
     *                  c1      d1
     *
     */
    @Test
    public void createHuffmanTreeTest() {
        int[] frequencies = h.createFrequencyTable("aabbbcd".toCharArray());
        PriorityQueue<HuffmanNode> queue = h.createPriorityQueue(frequencies);
        HuffmanNode root = h.createHuffmanTree(queue);

        Assert.assertEquals('-', root.c);
        Assert.assertEquals(7, root.frequency);
        Assert.assertEquals('b', root.left.c);
        Assert.assertEquals(3, root.left.frequency);
        Assert.assertNull(root.left.left);
        Assert.assertNull(root.left.right);

        Assert.assertEquals('-', root.right.c);
        Assert.assertEquals(4, root.right.frequency);
        Assert.assertEquals('a', root.right.left.c);
        Assert.assertEquals(2, root.right.left.frequency);
        Assert.assertNull(root.right.left.left);
        Assert.assertNull(root.right.left.right);

        Assert.assertEquals('-', root.right.right.c);
        Assert.assertEquals(2, root.right.right.frequency);
        Assert.assertEquals('c', root.right.right.left.c);
        Assert.assertEquals(1, root.right.right.left.frequency);
        Assert.assertNull(root.right.right.left.left);
        Assert.assertNull(root.right.right.left.right);

        Assert.assertEquals('d', root.right.right.right.c);
        Assert.assertEquals(1, root.right.right.right.frequency);
        Assert.assertNull(root.right.right.right.left);
        Assert.assertNull(root.right.right.right.right);
    }

    @Test
    public void encodeStringTest() {
        String text = "aabbbcd";
        int[] frequencies = h.createFrequencyTable(text.toCharArray());
        PriorityQueue<HuffmanNode> queue = h.createPriorityQueue(frequencies);
        HuffmanNode root = h.createHuffmanTree(queue);
        String s = h.encodeString(text.toCharArray(), root);

        Assert.assertEquals("1010000110111", s);
    }


    @Test
    public void generateBitesTest() {
        String[] st = new String[h.CHARACTER_LIMIT];
        int[] frequencies = h.createFrequencyTable("aabbbcd".toCharArray());
        PriorityQueue<HuffmanNode> queue = h.createPriorityQueue(frequencies);
        HuffmanNode root = h.createHuffmanTree(queue);
        h.generateBites(st, root, new StringBuilder());

        Assert.assertEquals("10", st[97]);
        Assert.assertEquals("0", st[98]);
        Assert.assertEquals("110", st[99]);
        Assert.assertEquals("111", st[100]);

    }

    @Test
    public void compressTest() {
        System.out.println(h.compress("aabbbcd".toCharArray()));

    }

    @Test
    public void parseHeaderAsFrequencyTest() {
        char[] c = "\u0001:a2:b3:c1:d1\u00021010000110111".toCharArray(); // aabbbcd
        int[] freq = h.parseHeaderAsFrequency(c);
        Assert.assertEquals(2, freq['a']);
        Assert.assertEquals(3, freq['b']);
        Assert.assertEquals(1, freq['c']);
        Assert.assertEquals(1, freq['d']);
    }

    @Test
    public void isLeafTest() {
        HuffmanNode root = new HuffmanNode('-',2);
        HuffmanNode leftNode = new HuffmanNode('a',2);
        root.left = leftNode;
        Assert.assertTrue(h.isLeaf(leftNode));
        Assert.assertFalse(h.isLeaf(root));
        Assert.assertFalse(h.isLeaf(null));
    }

    @Test
    public void decodeStringTest() {
        char[] c = "\u0001:a2:b3:c1:d1\u00021010000110111".toCharArray(); // aabbbcd
        int[] freq = h.parseHeaderAsFrequency(c);
        PriorityQueue<HuffmanNode> queue = h.createPriorityQueue(freq);
        HuffmanNode root = h.createHuffmanTree(queue);
        String decoded = h.decodeString(c, root);
        Assert.assertEquals("aabbbcd", decoded);
        Assert.assertNotSame("aaabbcd", decoded);
    }

    @Test
    public void decompressTest() {
        char[] c = "\u0001:a2:b3:c1:d1\u00021010000110111".toCharArray(); // aabbbcd
        char[] decompressed = h.decompress(c);

    }
}
