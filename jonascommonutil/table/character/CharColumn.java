package table.character;

import table.Column;
import table.Field;

public class CharColumn extends Column<Character> {

    public CharColumn(String name) {
        super(name);
    }

    @Override
    protected Field<Character> getConvertedValue(Field<?> field) {
        try {
            return new Field<>((Character) field.value());
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    }
}
