import util.christmas_printer.AdventOfCodeAnswer;

public class Main01 {
    public static void main(String[] args) {
//        test();
//        part1();
        part2();
    }

    public static void test() {
        SafeDial safeDial = new SafeDial(50, 0, 99, 0);

        try (RotationReader rotationReader = new RotationReader("2025/01/Jonas", "InputTestDay1")) {
            while (rotationReader.hasNextLine()) {
                RotationInstruction rotationInstruction = rotationReader.getNextRotation();
                safeDial.rotate(rotationInstruction);
            }
        } catch (Exception e) {
            throw new RuntimeException(e);
        }

        AdventOfCodeAnswer adventOfCodeAnswer = new AdventOfCodeAnswer(String.valueOf(safeDial.getNumberCount()), "3");
        ChristmasPrinter2025 christmasPrinter = new ChristmasPrinter2025(adventOfCodeAnswer);
        christmasPrinter.print();
    }

    public static void part1() {
        SafeDial safeDial = new SafeDial(50, 0, 99, 0);

        try (RotationReader rotationReader = new RotationReader("2025/01/Jonas", "Input1Day1")) {
            while (rotationReader.hasNextLine()) {
                RotationInstruction rotationInstruction1 = rotationReader.getNextRotation();
                safeDial.rotate(rotationInstruction1);
            }
        } catch (Exception e) {
            throw new RuntimeException(e);
        }

        AdventOfCodeAnswer adventOfCodeAnswer = new AdventOfCodeAnswer(String.valueOf(safeDial.getNumberCount()), "?");
        ChristmasPrinter2025 christmasPrinter = new ChristmasPrinter2025(adventOfCodeAnswer);
        christmasPrinter.print();
    }

    public static void part2() {
    }
}
