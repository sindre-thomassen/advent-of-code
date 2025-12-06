package christmasprinter.designs;

import christmasprinter.ChristmasPrinter;
import stringformatter.Message;
import stringformatter.replaceplaceholderformatter.CenteredOverwriteFormatter;
import stringformatter.replaceplaceholderformatter.ReplacePlaceholderFormatter;
import stringformatter.replaceplaceholderformatter.RightOverwriteFormatter;
import time.DateOfYear;
import time.Month;

public class ChristmasPrinter2024 extends ChristmasPrinter {

    public ChristmasPrinter2024() {
        super(new DateOfYear(Month.DECEMBER, 24));
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
