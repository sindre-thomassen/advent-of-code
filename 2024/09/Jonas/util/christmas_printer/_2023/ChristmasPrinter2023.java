package util.christmas_printer._2023;

import util.christmas_printer.ChristmasPrinter;
import util.string_formatter.replace_placeholder_formatter.CenteredOverwriteFormatter;
import util.string_formatter.Message;
import util.string_formatter.replace_placeholder_formatter.ReplacePlaceholderFormatter;
import util.string_formatter.replace_placeholder_formatter.RightOverwriteFormatter;
import util.time.DateOfYear;
import util.time.Month;

public class ChristmasPrinter2023 extends ChristmasPrinter {

    public ChristmasPrinter2023() {
        super(new DateOfYear(Month.DECEMBER, 24));
    }

    @Override
    protected Message getDesign() {
        int tabs = 10;

        return Message.create()
                .appendTab(tabs).appendText("┌-------------------------------------------------------------------------------------------------┐").appendNewLine()
                .appendTab(tabs).appendText("|       *          *                           *  ┌------------------╲      *         ╲   ╱       |").appendNewLine()
                .appendTab(tabs).appendText("|╲            ^                    *              | North Pole 70km   >              ─  *  ─      |").appendNewLine()
                .appendTab(tabs).appendText("|  ╲        ╱   ╲               ^             *   └------------------╱                 ╱o╲        |").appendNewLine()
                .appendTab(tabs).appendText("|    ╲    ╱~~~~~~~╲     *     ╱~~~╲                       |  |     *                  ╱*~~╲    *  |").appendNewLine()
                .appendTab(tabs).appendText("|      ╲╱           ╲     ╱╲╱       ╲  ┌-----------------------------------┬----┐  * ╱o~*~o╲      |").appendNewLine()
                .appendTab(tabs).appendText("|        ╲__     ╱╲   ╲_╱    ╲____    ╲|                   %s              ╰─╮  |   ╱~o~o~~*╲     |").appendNewLine()
                .appendTab(tabs).appendText("|           ╲__╱    ╲_╱        ╲       |  Expected Answer: %s                ╰──|  ╱*~~o~*~~o╲    |").appendNewLine()
                .appendTab(tabs).appendText("|      ╱╲                        ╲___  |  Answer:          %s                   | ╱~o~~*~o~~*~╲   |").appendNewLine()
                .appendTab(tabs).appendText("|     ╱˷˷╲    ,_____,     ╭╮╭───────╯  └----------------------------------------┘╱o~*~~o~*~~o~~╲  |").appendNewLine()
                .appendTab(tabs).appendText("|   ╭──||────/_╲_____╲────╯╰╯                             |  |               ┌─┬─┐`˜`˜|˜˜˜|˜`˜´┌┬┐|").appendNewLine()
                .appendTab(tabs).appendText("|   ╰────    |_|_____|                                    |  |               └─┴┬┼┐┌─┬┴┐ ┌┼┐┌─┬┴┤┘|").appendNewLine()
                .appendTab(tabs).appendText("|                                                        ~~~~~~                 └┴┘└─┴─┘~└┴┘└─┴─┘ |").appendNewLine()
                .appendTab(tabs).appendText("└-------------------------------------------------------------------------------------------------┘");
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
        return 3;
    }

    @Override
    protected int getExpectedAnswerOrder() {
        return 2;
    }
}
