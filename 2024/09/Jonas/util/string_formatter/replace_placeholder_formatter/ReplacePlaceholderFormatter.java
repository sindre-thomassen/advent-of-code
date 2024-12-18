package util.string_formatter.replace_placeholder_formatter;

public interface ReplacePlaceholderFormatter {

    String STRING_FORMATTING_PLACEHOLDER = "%s";

    String format(String text, String replacement);
}
