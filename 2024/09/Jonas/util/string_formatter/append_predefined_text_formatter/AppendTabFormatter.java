package util.string_formatter.append_predefined_text_formatter;

public class AppendTabFormatter implements AppendPredefinedTextFormatter {

    private static final String TAB = "\t";

    @Override
    public String format(String text) {
        return text + TAB;
    }

    @Override
    public String format(String text, int repetitions) {
        return text + TAB.repeat(repetitions);
    }
}
