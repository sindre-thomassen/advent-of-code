package util.string_formatter.replace_placeholder_formatter;

public class CenteredOverwriteFormatter implements ReplacePlaceholderFormatter {

    @Override
    public String format(String text, String formattingPlaceholder, String replacement) {
        int placeholderIndex = text.indexOf(formattingPlaceholder);
        int deleteAndInsertIndex = placeholderIndex - (int) Math.round(replacement.length() / 2.0) + 1;
        return new StringBuilder(text)
                .delete(deleteAndInsertIndex, deleteAndInsertIndex + (formattingPlaceholder.length() - 1) + replacement.length())
                .insert(deleteAndInsertIndex, replacement + " ".repeat(formattingPlaceholder.length() - 1))
                .toString();
    }
}
