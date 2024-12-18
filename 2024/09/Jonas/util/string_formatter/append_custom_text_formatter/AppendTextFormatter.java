package util.string_formatter.append_custom_text_formatter;

public class AppendTextFormatter implements AppendCustomTextFormatter {

    @Override
    public String format(String text, String appendText) {
        return text + appendText;
    }

    @Override
    public String format(String text, String appendText, int repetitions) {
        return text + appendText.repeat(repetitions);
    }
}
