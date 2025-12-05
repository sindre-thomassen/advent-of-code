import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.stream.Collectors;

public class BatteryNumberGenerator {

    public static long generateLargestNumber(List<Long> numbers, int numbersOfDigitsToUse) {
        if (numbers.size() < numbersOfDigitsToUse || numbersOfDigitsToUse <= 0) {
            throw new IllegalArgumentException();
        }

        List<Long> numbersToAddUp = new java.util.ArrayList<>(Collections.emptyList());

        for (Long number : numbers) {
            if (numbersToAddUp.size() < numbersOfDigitsToUse) {
                numbersToAddUp.add(number);
            } else {
                numbersToAddUp = getIncreasedNumberIfPossible(numbersToAddUp, number);
            }
        }

        String combined = numbersToAddUp.stream()
                .map(String::valueOf)
                .collect(Collectors.joining());
        return Long.parseLong(combined);
    }

    private static List<Long> getIncreasedNumberIfPossible(List<Long> largestNumbers, Long number) {
        List<Long> adjustedList = new ArrayList<>();
        boolean needAdjustement = false;

        for (int i = 0; i < largestNumbers.size(); i++) {
            long currentNumber = largestNumbers.get(i);
            long nextNumber = isLastLoopIteration(i, largestNumbers.size()) ? number : largestNumbers.get(i + 1);

            if (!needAdjustement && currentNumber < nextNumber) {
                needAdjustement = true;
                if (!isLastLoopIteration(i, largestNumbers.size())) {
                    adjustedList.add(nextNumber);
                    i += 1;
                }
            } else {
                adjustedList.add(currentNumber);
            }
        }
        if (needAdjustement) {
            adjustedList.add(number);
        }

        return adjustedList;
    }

    private static boolean isLastLoopIteration(int currentIndex, int listSize) {
        return currentIndex + 1 == listSize;
    }
}
