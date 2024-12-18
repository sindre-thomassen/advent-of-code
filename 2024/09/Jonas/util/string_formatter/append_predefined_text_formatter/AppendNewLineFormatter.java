package util.string_formatter.append_predefined_text_formatter;

public class AppendNewLineFormatter implements AppendPredefinedTextFormatter {

    private static final String NEW_LINE = "\n";

    @Override
    public String format(String text) {
        return text + NEW_LINE;
    }

    @Override
    public String format(String text, int repetitions) {
        return text + NEW_LINE.repeat(repetitions);
    }
}
