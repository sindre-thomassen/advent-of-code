package table;

public abstract class Column<T> {

    protected final String name;

    protected Column(String name) {
        this.name = name;
    }
}
