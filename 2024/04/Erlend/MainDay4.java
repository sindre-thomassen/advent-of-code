import java.nio.file.Paths;
import java.util.List;

public class MainDay4 {

    public static void main(String[] args) {
        String fileName = Paths.get("").toAbsolutePath() + "/2024/04/Erlend/input.txt";
        FileReaderDay4 fileReaderDay4 = new FileReaderDay4();
        fileReaderDay4.readInputFile(fileName);
        List<String> inputData = fileReaderDay4.getInputData();

        int totalXmasFound = 0;

        for (int y = 0; y < inputData.size(); y++) {
            for (int x = 0; x < inputData.get(y).length(); x++) {
                totalXmasFound += findXmasInAllDirections(inputData, x, y);
            }
        }

        System.out.println("Total XMAS found: " + totalXmasFound);
    }

    public static int findXmasInAllDirections(List<String> inputData2dArray, int xIndex, int yIndex) {
        int XmasFound = 0;
        XmasSearcher XmasSearcher = new XmasSearcher();

        if (XmasSearcher.foundHorizontally(inputData2dArray, xIndex, yIndex)) {
            XmasFound++;
        };
        if (XmasSearcher.foundVertically(inputData2dArray, xIndex, yIndex)) {
            XmasFound++;
        };
        if (XmasSearcher.foundDiagonallyLeftToRight(inputData2dArray, xIndex, yIndex)) {
            XmasFound++;
        };
        if (XmasSearcher.foundDiagonallyRightToLeft(inputData2dArray, xIndex, yIndex)) {
            XmasFound++;
        };
        return XmasFound;
    }
}
