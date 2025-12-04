import java.util.Collections;
import java.util.List;
import java.util.stream.Collectors;

public class NumberGenerator {

    public static long createLargestNumberByOrder(List<Long> numbers, int numbersOfDigitsToUse) {
        if (numbers.size() < numbersOfDigitsToUse || numbersOfDigitsToUse <= 0) {
            throw new IllegalArgumentException();
        }

        List<Long> numbersToAddUp = new java.util.ArrayList<>(Collections.emptyList());

        for (int i = numbers.size() - 1; i >= 0; i--) {
            Long number = numbers.get(i);

            if (numbersToAddUp.size() < numbersOfDigitsToUse) {
                numbersToAddUp.add(0, number);
            }
            else if (number >= numbersToAddUp.get(0)) {
                long indexOf1stSmallestNumber = numbersToAddUp.stream()
                        .min(Long::compareTo)
                        .get();
                numbersToAddUp.remove(indexOf1stSmallestNumber);
                numbersToAddUp.add(0, number);
            }
        }

        String combined = numbersToAddUp.stream()
                .map(String::valueOf)
                .collect(Collectors.joining());
        return Long.parseLong(combined);
    }
}
