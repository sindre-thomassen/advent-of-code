package table;

import stringformatter.Message;

import java.util.ArrayList;
import java.util.List;

public class Table {

    private final List<Column<?>> columns;

    public Table(List<? extends Column<?>> columns) {
//        this.columns = (List<Column<?>>) columns;
        this.columns = new ArrayList<>(columns);
    }

    public void addRow(Row row) {
        if (row.getFields().size() != columns.size()) {
            throw new IllegalArgumentException("Row does not match table columns");
        }
        for (int i = 0; i < columns.size(); i++) {
            Column<?> column = columns.get(i);
            Field<?> field = row.getField(i);
            column.addRow(field);
        }
    }

    public List<Row> getRows() {
        List<Row> rows = new ArrayList<>();
        for (int i = 0; i < columns.size(); i++) {
            Column<?> column = columns.get(i);
            if (i == 0) {
                for (Field<?> field : column.getValues()) {
                    List<?> fields = List.of(field);
                    rows.add(new Row(fields));
                }
            } else {
                for (int j = 0; j < column.getValues().size(); j++) {
                    rows.get(j).addColumn(column.getValues().get(j));
                }
            }
        }
        return rows;
    }

    @Override
    public String toString() {
        Message message = Message.create()
                .appendText("Table{").appendNewLine();
        for (Row row : getRows()) {
            message.appendText(row.toString()).appendNewLine();
        }
        return message.appendText("}").toString();
    }
}
