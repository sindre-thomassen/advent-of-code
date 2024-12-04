import java.util.List;

public class XmasSearcher {
    static int wordLength = "XMAS".length();

    public boolean foundHorizontally(List<String> inputData2dArray, int xIndex, int yIndex) {
        boolean possibleToSearch = xIndex + (wordLength - 1) < inputData2dArray.get(0).length();

        if (possibleToSearch) {
            boolean first = inputData2dArray.get(yIndex).charAt(xIndex) == 'X';
            boolean second = inputData2dArray.get(yIndex).charAt(xIndex + 1) == 'M';
            boolean third = inputData2dArray.get(yIndex).charAt(xIndex + 2) == 'A';
            boolean fourth = inputData2dArray.get(yIndex).charAt(xIndex + 3) == 'S';

            boolean first2 = inputData2dArray.get(yIndex).charAt(xIndex) == 'S';
            boolean second2 = inputData2dArray.get(yIndex).charAt(xIndex + 1) == 'A';
            boolean third2 = inputData2dArray.get(yIndex).charAt(xIndex + 2) == 'M';
            boolean fourth2 = inputData2dArray.get(yIndex).charAt(xIndex + 3) == 'X';

            return (first && second && third && fourth) || (first2 && second2 && third2 && fourth2);
        } else {
            return false;
        }
    }

    public boolean foundVertically(List<String> inputData2dArray, int xIndex, int yIndex) {
        boolean possibleToSearch = yIndex + (wordLength - 1) < inputData2dArray.size();

        if (possibleToSearch) {
            boolean first = inputData2dArray.get(yIndex).charAt(xIndex) == 'X';
            boolean second = inputData2dArray.get(yIndex + 1).charAt(xIndex) == 'M';
            boolean third = inputData2dArray.get(yIndex + 2).charAt(xIndex) == 'A';
            boolean fourth = inputData2dArray.get(yIndex + 3).charAt(xIndex) == 'S';

            boolean first2 = inputData2dArray.get(yIndex).charAt(xIndex) == 'S';
            boolean second2 = inputData2dArray.get(yIndex + 1).charAt(xIndex) == 'A';
            boolean third2 = inputData2dArray.get(yIndex + 2).charAt(xIndex) == 'M';
            boolean fourth2 = inputData2dArray.get(yIndex + 3).charAt(xIndex) == 'X';

            return (first && second && third && fourth) || (first2 && second2 && third2 && fourth2);
        } else {
            return false;
        }
    }

    public boolean foundDiagonallyLeftToRight(List<String> inputData2dArray, int xIndex, int yIndex) {
        boolean possibleToSearch = xIndex + (wordLength - 1) < inputData2dArray.get(yIndex).length() && yIndex + (wordLength - 1) < inputData2dArray.size();

        if (possibleToSearch) {
            boolean first = inputData2dArray.get(yIndex).charAt(xIndex) == 'X';
            boolean second = inputData2dArray.get(yIndex + 1).charAt(xIndex + 1) == 'M';
            boolean third = inputData2dArray.get(yIndex + 2).charAt(xIndex + 2) == 'A';
            boolean fourth = inputData2dArray.get(yIndex + 3).charAt(xIndex + 3) == 'S';

            boolean first2 = inputData2dArray.get(yIndex).charAt(xIndex) == 'S';
            boolean second2 = inputData2dArray.get(yIndex + 1).charAt(xIndex + 1) == 'A';
            boolean third2 = inputData2dArray.get(yIndex + 2).charAt(xIndex + 2) == 'M';
            boolean fourth2 = inputData2dArray.get(yIndex + 3).charAt(xIndex + 3) == 'X';

            return (first && second && third && fourth) || (first2 && second2 && third2 && fourth2);
        } else {
            return false;
        }
    }

    public boolean foundDiagonallyRightToLeft(List<String> inputData2dArray, int xIndex, int yIndex) {
        boolean possibleToSearch = xIndex - (wordLength - 1) >= 0 && yIndex + (wordLength - 1) < inputData2dArray.size();

        if (possibleToSearch) {
            boolean first = inputData2dArray.get(yIndex).charAt(xIndex) == 'X';
            boolean second = inputData2dArray.get(yIndex + 1).charAt(xIndex - 1) == 'M';
            boolean third = inputData2dArray.get(yIndex + 2).charAt(xIndex - 2) == 'A';
            boolean fourth = inputData2dArray.get(yIndex + 3).charAt(xIndex - 3) == 'S';

            boolean first2 = inputData2dArray.get(yIndex).charAt(xIndex) == 'S';
            boolean second2 = inputData2dArray.get(yIndex + 1).charAt(xIndex - 1) == 'A';
            boolean third2 = inputData2dArray.get(yIndex + 2).charAt(xIndex - 2) == 'M';
            boolean fourth2 = inputData2dArray.get(yIndex + 3).charAt(xIndex - 3) == 'X';

            return (first && second && third && fourth) || (first2 && second2 && third2 && fourth2);
        } else {
            return false;
        }
    }

}
