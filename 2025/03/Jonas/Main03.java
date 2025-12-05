import util.ChristmasPrinter2025;
import util.FileType;

import java.util.List;

public class Main03 {
    public static void main(String[] args) {
        ChristmasPrinter2025 christmasPrinter = new ChristmasPrinter2025();

//        christmasPrinter.print(getAnswerPart1Test(), 357);
//        christmasPrinter.print(getAnswerPart1(), 17383);
//        christmasPrinter.print(getAnswerPart2Test(), 3121910778619L);
        christmasPrinter.print(getAnswerPart2());
    }

    public static long getAnswerPart1Test(){
        long joltage = 0;
        for (List<Long> batteries : new BatteryBankReader("2025/03/Jonas/input", "Input1Day3Test", FileType.TXT)) {
            joltage += BatteryNumberGenerator.generateLargestNumber(batteries, 2);
        }
        return joltage;
    }

    public static long getAnswerPart1(){
        long joltage = 0;
        for (List<Long> batteries : new BatteryBankReader("2025/03/Jonas/input", "Input1Day3", FileType.TXT)) {
            joltage += BatteryNumberGenerator.generateLargestNumber(batteries, 2);
        }
        return joltage;
    }

    public static long getAnswerPart2Test(){
        long joltage = 0;
        for (List<Long> batteries : new BatteryBankReader("2025/03/Jonas/input", "Input1Day3Test", FileType.TXT)) {
            joltage += BatteryNumberGenerator.generateLargestNumber(batteries, 12);
        }
        return joltage;
    }

    public static long getAnswerPart2(){
        long joltage = 0;
        for (List<Long> batteries : new BatteryBankReader("2025/03/Jonas/input", "Input1Day3", FileType.TXT)) {
            joltage += BatteryNumberGenerator.generateLargestNumber(batteries, 12);
        }
        return joltage;
    }
}
