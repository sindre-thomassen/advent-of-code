package table;

import stringformatter.Message;

import java.util.ArrayList;
import java.util.List;

public abstract class Column<T> {

    private final String name;
    private final List<Field<T>> values;

    public Column(String name) {
        this.name = name;
        this.values = new ArrayList<>();
    }

    protected abstract Field<T> getConvertedValue(Field<?> field);

    public String getName() {
        return name;
    }

    public List<Field<T>> getValues() {
        return values;
    }

    public void addRow(Field<?> row) {
        values.add(getConvertedValue(row));
    }

    @Override
    public String toString() {
        Message message = Message.create().appendText(name).appendText(":").appendNewLine();
        for (Field<T> value : values) {
            message.appendText("[").appendText(value.toString()).appendText("]").appendNewLine();
        }
        return message.toString();
    }
}
