import java.util.Collections;
import java.util.List;

public class Main {
    public static void main(String[] args) {

        List<Integer> list1 = new List1().getList();
        List<Integer> list2 = new List2().getList();

        Collections.sort(list1);
        Collections.sort(list2);

        int result = 0;
        for (int i = 0; i < list1.size(); i++) {
            result += Math.abs(list1.get(i) - list2.get(i));
        }

        System.out.println(result);
    }
}
