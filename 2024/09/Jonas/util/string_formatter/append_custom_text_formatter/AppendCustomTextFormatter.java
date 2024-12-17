package util.string_formatter.append_custom_text_formatter;

public interface AppendCustomTextFormatter {
    String format(String text, String appendText);

    String format(String text, String appendText, int repetitions);
}
