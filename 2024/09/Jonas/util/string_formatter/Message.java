package util.string_formatter;

public class Message {

    private static final String stringFormattingPlaceholder = "%s";
    private String message;

    private Message(String message) {
        this.message = message;
    }

    public static Message create() {
        return new Message("");
    }

    public Message addText(String string) {
        this.message += string;
        return this;
    }

    public Message addTab(int count) {
        this.message += "\t".repeat(count);
        return this;
    }

    public Message newLine() {
        this.message += System.lineSeparator();
        return this;
    }

    public Message overwriteFromPlaceholder(String replacement) {
        int index = this.message.indexOf(stringFormattingPlaceholder);
        this.message = new StringBuilder(this.message)
                .delete(index, index + (stringFormattingPlaceholder.length() - 1) + replacement.length())
                .insert(index, replacement + " ".repeat(stringFormattingPlaceholder.length() - 1))
                .toString();
        return this;
    }

    public Message overwriteSymmetricallyFromPlaceholder(String replacement) {
        int placeholderIndex = this.message.indexOf(stringFormattingPlaceholder);
        int deleteAndInsertIndex = placeholderIndex - (int) Math.round(replacement.length() / 2.0) + 1;
        this.message = new StringBuilder(this.message)
                .delete(deleteAndInsertIndex, deleteAndInsertIndex + (stringFormattingPlaceholder.length() - 1) + replacement.length())
                .insert(deleteAndInsertIndex, replacement + " ".repeat(stringFormattingPlaceholder.length() - 1))
                .toString();
        return this;
    }

    @Override
    public String toString() {
        return this.message;
    }
}
