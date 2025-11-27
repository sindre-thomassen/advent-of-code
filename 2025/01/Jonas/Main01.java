import util.christmas_printer.AdventOfCodeAnswer;

public class Main01 {
    public static void main(String[] args) {
        AdventOfCodeAnswer adventOfCodeAnswer = new AdventOfCodeAnswer("11 answer", "22 exp answer");
        ChristmasPrinter2025 christmasPrinter = new ChristmasPrinter2025(adventOfCodeAnswer);
        christmasPrinter.print();
    }
}
