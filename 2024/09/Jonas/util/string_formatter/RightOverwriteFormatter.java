package util.string_formatter;

public class RightOverwriteFormatter implements MessageFormatter {

    @Override
    public String format(String message, String stringFormattingPlaceholder, String replacement) {
        int deleteAndInsertIndex = message.indexOf(stringFormattingPlaceholder);
        return new StringBuilder(message)
                .delete(deleteAndInsertIndex, deleteAndInsertIndex + (stringFormattingPlaceholder.length() - 1) + replacement.length())
                .insert(deleteAndInsertIndex, replacement + " ".repeat(stringFormattingPlaceholder.length() - 1))
                .toString();
    }
}
