package table.character;

import table.Field;

import java.util.ArrayList;
import java.util.List;

public class CharRow {

    private final List<Field<Character>> fields;

    public CharRow(String string) {
        fields = new ArrayList<>();
        for (char character : string.toCharArray()) {
            fields.add(new Field<>(character));
        }
    }

    public List<Field<Character>> getFields() {
        return fields;
    }

    public Field<Character> getField(int index) {
        return fields.get(index);
    }
}
