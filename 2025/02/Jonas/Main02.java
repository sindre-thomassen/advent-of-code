import util.ChristmasPrinter2025;
import util.FileType;

public class Main02 {
    public static void main(String[] args) {
        ChristmasPrinter2025 christmasPrinter = new ChristmasPrinter2025();

//        christmasPrinter.print(getAnswerTest(), 1227775554);
        christmasPrinter.print(getAnswerPart1(), 24043483400L);
    }

    public static long getAnswerTest() {
        long answer = 0;
        for (Range idRange : new GiftShopIdReader("2025/02/Jonas/input", "InputTestDay2", FileType.CSV)) {
            for (long currentId = idRange.start(); currentId <= idRange.end(); currentId++) {
                if (GiftShopIdValidator.isInvalidId(currentId)) {
                    answer += currentId;
                }
            }

        }
        return answer;
    }

    public static long getAnswerPart1() {
        long answer = 0;
        for (Range idRange : new GiftShopIdReader("2025/02/Jonas/input", "Input1Day2", FileType.CSV)) {
            for (long currentId = idRange.start(); currentId <= idRange.end(); currentId++) {
                if (GiftShopIdValidator.isInvalidId(currentId)) {
                    answer += currentId;
                }
            }

        }
        return answer;
    }
}
