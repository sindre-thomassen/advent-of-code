package stringformatter.replaceplaceholderformatter;

public interface ReplacePlaceholderFormatter {

    String STRING_FORMATTING_PLACEHOLDER = "%s";

    String format(String text, String replacement);
}
