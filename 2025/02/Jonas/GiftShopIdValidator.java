public class GiftShopIdValidator {

    public static boolean isInvalidId(long id) {
        String idString = String.valueOf(id);
        if (idString.length() % 2 == 1) {
            return false;
        }

        int splitIndex = idString.length() / 2;
        String part1 = idString.substring(0, splitIndex);
        String part2 = idString.substring(splitIndex);

        return part1.equals(part2);
    }
}
