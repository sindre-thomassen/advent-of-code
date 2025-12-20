import christmasprinter.designs.ChristmasPrinter2025;
import reader.CharLineReader;
import reader.FileType;
import table.character.*;

import java.util.List;

public class Main04 {
    public static void main(String[] args) {
        ChristmasPrinter2025 christmasPrinter = new ChristmasPrinter2025();
        christmasPrinter.print(getAnswerPart1Test(),13);
    }

    private static int getAnswerPart1Test() {
        CharTable floorTiles = new CharTable("Floor tiles");
        for (List<Character> floorTileRow : new CharLineReader("2025/04/Jonas/input", "Input1Test", FileType.TXT)) {
            if (floorTiles.getColumns().isEmpty()) {
                for (int i = 1; i <= floorTileRow.size(); i++) {
                    floorTiles.addColumn("Column" + i, ' ');
                }
            }
            floorTiles.addRow(floorTileRow);
        }
        System.out.println(floorTiles);
        return 0;
    }
}
