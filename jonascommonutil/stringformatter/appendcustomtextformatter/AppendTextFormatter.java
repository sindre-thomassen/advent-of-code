package stringformatter.appendcustomtextformatter;

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
