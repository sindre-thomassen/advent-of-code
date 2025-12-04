public class GiftShopIdValidator {

    public static boolean isInvalidIdPart1(long id) {
        String idString = String.valueOf(id);
        if (idString.length() % 2 == 1) {
            return false;
        }

        int splitIndex = idString.length() / 2;
        String part1 = idString.substring(0, splitIndex);
        String part2 = idString.substring(splitIndex);

        return part1.equals(part2);
    }

    public static boolean isInvalidIdPart2(long id) {
        String idString = String.valueOf(id);
        double breakPoint = (double) idString.length() / 2;

        for (int numberSpan = 1; numberSpan <= breakPoint; numberSpan++) {
            if (isRepeatedSpan(numberSpan, idString)) {
                return true;
            }
        }

        return false;
    }

    private static boolean isRepeatedSpan(int step, String idString) {
        if (idString.length() % step != 0) {
            return false;
        }

        String idSpan = idString.substring(0, step);
        int matches = 0;

        for (int i = step; i < idString.length(); i += step) {
            if (!idSpan.equals(idString.substring(i, i + step))) {
                return false;
            }
            matches++;
        }

        return matches >= 1;
    }
}
