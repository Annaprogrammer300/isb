import java.util.Random;

/**
 * Class for generating a pseudo-random the specified length binary sequence.
 */
public class GenerateRandom {

    /**
     * The main method generates a random binary sequence and prints it to the console.
     * @param args the command-line arguments
     */
    public static void main(String[] args) {
        final int BITS = 128;
        printRandomNumbers(BITS);
    }

    /**
     * Pseudo random sequence generation function
     * @param count The number of bits in the sequence
     */
    public static void printRandomNumbers(int count) {
        Random random = new Random();

        for (int i = 0; i < count; i++) {
            System.out.print(random.nextInt(2));
        }
    }
}
