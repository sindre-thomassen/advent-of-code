package table;

public record Field<T>(T value) {

    @Override
    public String toString() {
        return value.toString();
    }
}
