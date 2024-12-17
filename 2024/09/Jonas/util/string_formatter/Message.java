package util.string_formatter;

import util.string_formatter.append_custom_text_formatter.AppendTextFormatter;
import util.string_formatter.append_predefined_text_formatter.AppendNewLineFormatter;
import util.string_formatter.append_predefined_text_formatter.AppendTabFormatter;
import util.string_formatter.replace_placeholder_formatter.ReplacePlaceholderFormatter;

public class Message {

    private String message;
    private static final AppendTextFormatter appendTextFormatter = new AppendTextFormatter();
    private static final AppendTabFormatter appendTabFormatter = new AppendTabFormatter();
    private static final AppendNewLineFormatter appendNewLineFormatter = new AppendNewLineFormatter();

    private Message(String message) {
        this.message = message;
    }

    public static Message create() {
        return new Message("");
    }

    public Message appendText(String appendText) {
        this.message = appendTextFormatter.format(this.message, appendText);
        return this;
    }

    public Message appendTab(int repetitions) {
        this.message = appendTabFormatter.format(this.message, repetitions);
        return this;
    }

    public Message appendNewLine() {
        this.message = appendNewLineFormatter.format(this.message);
        return this;
    }

    public Message format(ReplacePlaceholderFormatter replacePlaceholderFormatter, String replacement) {
        this.message = replacePlaceholderFormatter.format(this.message, replacement);
        return this;
    }

    @Override
    public String toString() {
        return this.message;
    }
}
