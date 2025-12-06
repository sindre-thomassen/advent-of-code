package stringformatter.replaceplaceholderformatter;

public class RightOverwriteFormatter implements ReplacePlaceholderFormatter {

    @Override
    public String format(String text, String replacement) {
        int deleteAndInsertIndex = text.indexOf(STRING_FORMATTING_PLACEHOLDER);
        return new StringBuilder(text)
                .delete(deleteAndInsertIndex, deleteAndInsertIndex + (STRING_FORMATTING_PLACEHOLDER.length() - 1) + replacement.length())
                .insert(deleteAndInsertIndex, replacement + " ".repeat(STRING_FORMATTING_PLACEHOLDER.length() - 1))
                .toString();
    }
}
