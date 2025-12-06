package stringformatter;

import stringformatter.appendcustomtextformatter.AppendTextFormatter;
import stringformatter.appendpredefinedtextformatter.AppendNewLineFormatter;
import stringformatter.appendpredefinedtextformatter.AppendTabFormatter;
import stringformatter.replaceplaceholderformatter.ReplacePlaceholderFormatter;

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
