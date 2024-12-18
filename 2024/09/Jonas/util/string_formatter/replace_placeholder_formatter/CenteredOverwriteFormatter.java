package util.string_formatter.replace_placeholder_formatter;

public class CenteredOverwriteFormatter implements ReplacePlaceholderFormatter {

    @Override
    public String format(String text, String replacement) {
        int placeholderIndex = text.indexOf(STRING_FORMATTING_PLACEHOLDER);
        int deleteAndInsertIndex = placeholderIndex - (int) Math.round(replacement.length() / 2.0) + 1;
        return new StringBuilder(text)
                .delete(deleteAndInsertIndex, deleteAndInsertIndex + (STRING_FORMATTING_PLACEHOLDER.length() - 1) + replacement.length())
                .insert(deleteAndInsertIndex, replacement + " ".repeat(STRING_FORMATTING_PLACEHOLDER.length() - 1))
                .toString();
    }
}
