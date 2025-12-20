package table.character;

import table.Row;

import java.util.List;

public class CharRow extends Row<Character> {

    public CharRow(List<Character> characters) {
        for (Character character : characters) {
            addValue(character);
        }
    }
}
