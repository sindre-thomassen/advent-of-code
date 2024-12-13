package util.string_formatter;

public class CenteredOverwriteFormatter implements MessageFormatter{

    @Override
    public String format(String message, String stringFormattingPlaceholder, String replacement) {
        int placeholderIndex = message.indexOf(stringFormattingPlaceholder);
        int deleteAndInsertIndex = placeholderIndex - (int) Math.round(replacement.length() / 2.0) + 1;
        return new StringBuilder(message)
                .delete(deleteAndInsertIndex, deleteAndInsertIndex + (stringFormattingPlaceholder.length() - 1) + replacement.length())
                .insert(deleteAndInsertIndex, replacement + " ".repeat(stringFormattingPlaceholder.length() - 1))
                .toString();
    }
}
