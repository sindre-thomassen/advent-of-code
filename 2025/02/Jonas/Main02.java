import christmasprinter.designs.ChristmasPrinter2025;
import util.FileType;

public class Main02 {
    public static void main(String[] args) {
        ChristmasPrinter2025 christmasPrinter = new ChristmasPrinter2025();

//        christmasPrinter.print(getAnswerPart1Test(), 1227775554);
//        christmasPrinter.print(getAnswerPart1(), 24043483400L);
//        christmasPrinter.print(getAnswerPart2Test(), 4174379265L);
        christmasPrinter.print(getAnswerPart2());
    }

    public static long getAnswerPart1Test() {
        long answer = 0;
        for (Range idRange : new GiftShopIdReader("2025/02/Jonas/input", "InputTestDay2", FileType.CSV)) {
            for (long currentId = idRange.start(); currentId <= idRange.end(); currentId++) {
                if (GiftShopIdValidator.isInvalidIdPart1(currentId)) {
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
                if (GiftShopIdValidator.isInvalidIdPart1(currentId)) {
                    answer += currentId;
                }
            }

        }
        return answer;
    }

    public static long getAnswerPart2Test() {
        long answer = 0;
        for (Range idRange : new GiftShopIdReader("2025/02/Jonas/input", "InputTest2Day2", FileType.CSV)) {
            for (long currentId = idRange.start(); currentId <= idRange.end(); currentId++) {
                if (GiftShopIdValidator.isInvalidIdPart2(currentId)) {
                    answer += currentId;
                }
            }

        }
        return answer;
    }

    public static long getAnswerPart2() {
        long answer = 0;
        for (Range idRange : new GiftShopIdReader("2025/02/Jonas/input", "Input1Day2", FileType.CSV)) {
            for (long currentId = idRange.start(); currentId <= idRange.end(); currentId++) {
                if (GiftShopIdValidator.isInvalidIdPart2(currentId)) {
                    answer += currentId;
                }
            }

        }
        return answer;
    }
}
