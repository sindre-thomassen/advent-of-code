import christmasprinter.AdventOfCodeAnswer;
import christmasprinter.designs.ChristmasPrinter2023;
import christmasprinter.designs.ChristmasPrinter2024;

public class Main10 {
    public static void main(String[] args) {
        AdventOfCodeAnswer adventOfCodeAnswer = new AdventOfCodeAnswer("11 answer", "22 exp answer");
        ChristmasPrinter2024 christmasPrinter2024 = new ChristmasPrinter2024();
        ChristmasPrinter2023 christmasPrinter2023 = new ChristmasPrinter2023();

        christmasPrinter2023.print(adventOfCodeAnswer);
        christmasPrinter2024.print(adventOfCodeAnswer);
    }
}
