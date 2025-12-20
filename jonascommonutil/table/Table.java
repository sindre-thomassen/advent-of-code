package table;

import stringformatter.Message;

import java.util.ArrayList;
import java.util.List;

public abstract class Table<FieldType> {

    protected final String name;
    protected final List<Column<FieldType>> columns;
    protected final List<Row<FieldType>> rows;

    protected Table(String name) {
        this.name = name;
        this.columns = new ArrayList<>();
        this.rows = new ArrayList<>();
    }

    public void addColumn(String name, FieldType defaultValue) {
        if (!rows.isEmpty()) {
            for (Row<FieldType> row : rows) {
                row.addValue(defaultValue);
            }
        }
        columns.add(getNewColumn(name));
    }

    abstract protected Column<FieldType> getNewColumn(String name);

    public void addRow(List<FieldType> values) {
        if (values.size() != columns.size()) {
            throw new IllegalArgumentException("Row does not match table columns");
        }
        rows.add(getNewRow(values));
    }

    abstract protected Row<FieldType> getNewRow(List<FieldType> values);

    public List<Column<FieldType>> getColumns() {
        return columns.stream().toList();
    }

    @Override
    public String toString() {
        Message message = Message.create()
                .appendText(name).appendNewLine();
        for (Column<FieldType> column : columns) {
            message.appendText(column.name).appendText(", ");
        }
        message.removeLastIfMatch(", ").appendNewLine();
        for (Row<FieldType> row : rows) {
            message.appendText(row.toString()).appendNewLine();
        }
        return message.toString();
    }
}
