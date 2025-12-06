package stringformatter.appendcustomtextformatter;

public interface AppendCustomTextFormatter {
    String format(String text, String appendText);

    String format(String text, String appendText, int repetitions);
}
