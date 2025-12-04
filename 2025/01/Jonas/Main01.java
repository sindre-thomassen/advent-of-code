import util.ChristmasPrinter2025;
import util.FileType;

public class Main01 {
    public static void main(String[] args) {
        ChristmasPrinter2025 christmasPrinter = new ChristmasPrinter2025();

//        christmasPrinter.print(getTestAnswer(), 3);
//        christmasPrinter.print(getPart1Answer(), 989);
        christmasPrinter.print(getPart2Answer());
    }

    public static int getTestAnswer() {
        SafeDial safeDial = new SafeDial(50, 0, 99, 0);

        for (RotationInstruction rotationInstruction : new RotationReader("2025/01/Jonas/input", "InputTestDay1", FileType.TXT)) {
            safeDial.rotate(rotationInstruction);
        }

        return safeDial.getEndClickCount();
    }

    public static int getPart1Answer() {
        SafeDial safeDial = new SafeDial(50, 0, 99, 0);

        for (RotationInstruction rotationInstruction : new RotationReader("2025/01/Jonas/input", "Input1Day1", FileType.TXT)) {
            safeDial.rotate(rotationInstruction);
        }

        return safeDial.getEndClickCount();
    }

    public static int getPart2Answer() {
        SafeDial safeDial = new SafeDial(50, 0, 99, 0);

        for (RotationInstruction rotationInstruction : new RotationReader("2025/01/Jonas/input", "Input1Day1", FileType.TXT)) {
            safeDial.rotate(rotationInstruction);
        }

        return safeDial.getAllClicksCount();
    }
}
