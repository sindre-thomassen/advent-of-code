package util.string_formatter.replace_placeholder_formatter;

public class RightOverwriteFormatter implements ReplacePlaceholderFormatter {

    @Override
    public String format(String text, String formattingPlaceholder, String replacement) {
        int deleteAndInsertIndex = text.indexOf(formattingPlaceholder);
        return new StringBuilder(text)
                .delete(deleteAndInsertIndex, deleteAndInsertIndex + (formattingPlaceholder.length() - 1) + replacement.length())
                .insert(deleteAndInsertIndex, replacement + " ".repeat(formattingPlaceholder.length() - 1))
                .toString();
    }
}
