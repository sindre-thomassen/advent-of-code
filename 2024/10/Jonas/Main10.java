import util.christmas_printer.AdventOfCodeAnswer;
import util.christmas_printer._2023.ChristmasPrinter2023;
import util.christmas_printer._2024.ChristmasPrinter2024;

public class Main10 {
    public static void main(String[] args) {
        AdventOfCodeAnswer adventOfCodeAnswer = new AdventOfCodeAnswer("11 answer", "22 exp answer");
        ChristmasPrinter2024 christmasPrinter2024 = new ChristmasPrinter2024(adventOfCodeAnswer);
        ChristmasPrinter2023 christmasPrinter2023 = new ChristmasPrinter2023(adventOfCodeAnswer);
        christmasPrinter2023.print();
    }
}
