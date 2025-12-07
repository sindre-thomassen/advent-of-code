package table;

import java.util.ArrayList;
import java.util.List;

public class Row {

    private final List<Field<?>> fields;

    public Row(List<?> values) {
        this.fields = new ArrayList<>();
        for (Object value : values) {
            fields.add(new Field<>(value));
        }
    }

    public List<Field<?>> getFields() {
        return fields;
    }

    public Field<?> getField(int index) {
        return fields.get(index);
    }

    public void addColumn(Field<?> column) {
        fields.add(column);
    }

    @Override
    public String toString() {
        return getFields().toString();
    }
}
