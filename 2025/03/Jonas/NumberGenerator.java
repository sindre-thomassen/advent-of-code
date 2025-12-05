import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.stream.Collectors;

public class NumberGenerator {

    public static long createLargestNumberByOrder(List<Long> numbers, int numbersOfDigitsToUse) {
        if (numbers.size() < numbersOfDigitsToUse || numbersOfDigitsToUse <= 0) {
            throw new IllegalArgumentException();
        }

        List<Long> numbersToAddUp = new java.util.ArrayList<>(Collections.emptyList());

        for (Long number : numbers) {
            if (numbersToAddUp.size() < numbersOfDigitsToUse) {
                numbersToAddUp.add(number);
            } else {
                numbersToAddUp = getAdjustedList(numbersToAddUp, number);
            }
        }

        String combined = numbersToAddUp.stream()
                .map(String::valueOf)
                .collect(Collectors.joining());
        return Long.parseLong(combined);
    }

    private static List<Long> getAdjustedList(List<Long> largestNumbers, Long number) {
        List<Long> adjustedList = new ArrayList<>();
        boolean isAdjusted = false;

        for (int i = 0; i < largestNumbers.size(); i++) {
            if (isLastLoopIteration(i, largestNumbers.size())) {
                if (!isAdjusted && largestNumbers.get(i) < number) {
                    adjustedList.add(number);
                } else {
                    adjustedList.add(largestNumbers.get(i));
                }
            } else if (!isAdjusted && isNextNumberLarger(i, largestNumbers)) {
                adjustedList.add(largestNumbers.get(++i));
                isAdjusted = true;
            } else {
                adjustedList.add(largestNumbers.get(i));
            }
        }
        if (isAdjusted) {
            adjustedList.add(number);
        }

        return adjustedList;
    }

    public static boolean isLastLoopIteration(int currentIndex, int listSize) {
        return currentIndex + 1 == listSize;
    }

    public static boolean isNextNumberLarger(int currentIndex, List<Long> numbers) {
        return numbers.get(currentIndex) < numbers.get(currentIndex + 1);
    }
}
