package util.christmas_printer._2024;

import util.christmas_printer.AdventOfCodeAnswer;
import util.christmas_printer.ChristmasPrinter;
import util.string_formatter.replace_placeholder_formatter.CenteredOverwriteFormatter;
import util.string_formatter.Message;
import util.string_formatter.replace_placeholder_formatter.ReplacePlaceholderFormatter;
import util.string_formatter.replace_placeholder_formatter.RightOverwriteFormatter;
import util.time.DateOfYear;
import util.time.Month;

public class ChristmasPrinter2024 extends ChristmasPrinter {

    public ChristmasPrinter2024(AdventOfCodeAnswer adventOfCodeAnswer) {
        super(adventOfCodeAnswer, new DateOfYear(Month.DECEMBER, 24));
    }

    @Override
    protected Message getDesign() {
        return Message.create()
                .appendText("┌----------------------------------------┐").appendNewLine()
                .appendText("|---                %s                ---|").appendNewLine()
                .appendText("|--- Answer: %s                       ---|").appendNewLine()
                .appendText("|--- Expected answer: %s              ---|").appendNewLine()
                .appendText("└----------------------------------------┘");
    }

    @Override
    protected ReplacePlaceholderFormatter getChristmasCountdownFormatter() {
        return new CenteredOverwriteFormatter();
    }

    @Override
    protected ReplacePlaceholderFormatter getAnswerFormatter() {
        return new RightOverwriteFormatter();
    }

    @Override
    protected ReplacePlaceholderFormatter getExpectedAnswerFormatter() {
        return new RightOverwriteFormatter();
    }

    @Override
    protected int getChristmasCountdownOrder() {
        return 1;
    }

    @Override
    protected int getAnswerOrder() {
        return 2;
    }

    @Override
    protected int getExpectedAnswerOrder() {
        return 3;
    }
}
