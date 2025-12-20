package table.character;

import table.Table;

import java.util.List;

public class CharTable extends Table<Character> {

    public CharTable(String name) {
        super(name);
    }

    @Override
    protected CharColumn getNewColumn(String name) {
        return new CharColumn(name);
    }

    @Override
    protected CharRow getNewRow(List<Character> values) {
        return new CharRow(values);
    }
}
