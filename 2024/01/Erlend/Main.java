import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Main {

    public static void main(String[] args) {
        part1();
        part2();
    }

    private static void part1() {
        List<Integer> list1 = new List1().getList();
        List<Integer> list2 = new List2().getList();

        Collections.sort(list1);
        Collections.sort(list2);

        int result = 0;
        for (int i = 0; i < list1.size(); i++) {
            result += Math.abs(list1.get(i) - list2.get(i));
        }

        System.out.println("Part 1: " + result);
    }

    private static void part2() {
        List<Integer> list1 = new List1().getList();
        List<Integer> list2 = new List2().getList();

        Map<Integer, Integer> nMap = new HashMap<>();

        int result = 0;
        for (Integer n : list2) {
            if (!nMap.containsKey(n)) {
                nMap.put(n, 1);
            } else {
                nMap.put(n, nMap.get(n) + 1);
            }
        }

        for (Integer n : list1) {
            Integer factor = 0;
            if (nMap.containsKey(n)) {
                factor = nMap.get(n);
            }
            result += n * factor;
        }

        System.out.println("Part 2: " + result);
    }
}
