package table;

import java.util.ArrayList;
import java.util.List;

public abstract class Row<FieldType> {

    private final List<FieldType> values;

    protected Row() {
        values = new ArrayList<>();
    }

    public void addValue(FieldType value) {
        values.add(value);
    }

    @Override
    public String toString() {
        return values.toString();
    }
}
