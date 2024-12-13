package util.string_formatter;

public class Message {

    public static final String STRING_FORMATTING_PLACEHOLDER = "%s";
    private static final String TAB = "\t";
    private static final String NEW_LINE = "\n";

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
        this.message += Message.TAB.repeat(count);
        return this;
    }

    public Message newLine() {
        this.message += Message.NEW_LINE;
        return this;
    }

    public Message format(MessageFormatter messageFormatter, String replacement) {
        this.message = messageFormatter.format(this.message, Message.STRING_FORMATTING_PLACEHOLDER, replacement);
        return this;
    }

    @Override
    public String toString() {
        return this.message;
    }
}
