import util.ChristmasPrinter2025;
import util.FileType;

import java.util.List;

public class Main03 {
    public static void main(String[] args) {
        ChristmasPrinter2025 christmasPrinter = new ChristmasPrinter2025();

//        christmasPrinter.print(getAnswerPart1Test(), 357);
        christmasPrinter.print(getAnswerPart1(), 17383);
    }

    public static long getAnswerPart1Test(){
        long joltage = 0;
        for (List<Long> batteries : new BatteryBankReader("2025/03/Jonas/input", "Input1Day3Test", FileType.TXT)) {
            joltage += NumberGenerator.createLargestNumberByOrder(batteries, 2);
        }
        return joltage;
    }

    public static long getAnswerPart1(){
        long joltage = 0;
        for (List<Long> batteries : new BatteryBankReader("2025/03/Jonas/input", "Input1Day3", FileType.TXT)) {
            System.out.println(NumberGenerator.createLargestNumberByOrder(batteries, 2));
            joltage += NumberGenerator.createLargestNumberByOrder(batteries, 2);
        }
        return joltage;
    }
}
