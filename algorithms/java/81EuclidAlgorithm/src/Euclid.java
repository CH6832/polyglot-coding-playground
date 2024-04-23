/**
 * Euclid Algorithm<BR>
 *     it calculates the GCD(A,B) - Greatest Common Divisor between two number A and B
 */
public class Euclid {

    /**
     * Implementation using recursion<BR>
     *     22/6 = 3 rest of 4
     *     6/4 = 1 rest of 2
     *     4/2 = 2 rest of 0
     *
     * @param number
     * @param divisor
     * @return
     */
    public int gcd(int number, int divisor) {
        int remaining = (number % divisor);

        if (remaining != 0) {
            return gcd(divisor, remaining);
        } else {
            return divisor;
        }
    }

    /**
     * Implementation without recursion
     *     22/6 = 3 rest of 4
     *     6/4 = 1 rest of 2
     *     4/2 = 2 rest of 0
     *
     *     number/temp = result rest of divisor
     *
     * @param number
     * @param divisor
     * @return
     */
    public int gcd2(int number, int divisor) {
        while(divisor != 0) {
            int  temp = divisor;
            divisor = (number % divisor);
            number = temp;
        }
        return number;
    }
}
