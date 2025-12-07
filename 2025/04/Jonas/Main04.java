import christmasprinter.designs.ChristmasPrinter2025;
import reader.CharLineReader;
import reader.FileType;
import table.character.CharColumn;
import table.Row;
import table.Table;

import java.util.List;

public class Main04 {
    public static void main(String[] args) {
        ChristmasPrinter2025 christmasPrinter = new ChristmasPrinter2025();
        christmasPrinter.print(getAnswerPart1Test(),13);
    }

    private static int getAnswerPart1Test() {
        Table floorTiles = null;
        for (Row floorTileRow : new CharLineReader("2025/04/Jonas/input", "Input1Test", FileType.TXT)) {
            if (floorTiles == null) {
                List<CharColumn> columns = floorTileRow.getFields().stream()
                        .map(_ -> new CharColumn("dummy name"))
                        .toList();
                floorTiles = new Table(columns);
            }

            floorTiles.addRow(floorTileRow);
        }
        System.out.println(floorTiles);
        return 0;
    }
}
