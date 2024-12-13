package util.christmas_printer._2023;

import util.christmas_printer.AdventOfCodeAnswer;
import util.christmas_printer.ChristmasPrinter;
import util.string_formatter.CenteredOverwriteFormatter;
import util.string_formatter.Message;
import util.string_formatter.MessageFormatter;
import util.string_formatter.RightOverwriteFormatter;
import util.time.DateOfYear;
import util.time.Month;

public class ChristmasPrinter2023 extends ChristmasPrinter {

    public ChristmasPrinter2023(AdventOfCodeAnswer adventOfCodeAnswer) {
        super(adventOfCodeAnswer, new DateOfYear(Month.DECEMBER, 24));
    }

    @Override
    protected Message getDesign() {
        int tabs = 10;

        return Message.create()
                .addTab(tabs).addText("┌-------------------------------------------------------------------------------------------------┐").newLine()
                .addTab(tabs).addText("|       *          *                           *  ┌------------------╲      *         ╲   ╱       |").newLine()
                .addTab(tabs).addText("|╲            ^                    *              | North Pole 807km  >              ─  *  ─      |").newLine()
                .addTab(tabs).addText("|  ╲        ╱   ╲               ^             *   └------------------╱                 ╱o╲        |").newLine()
                .addTab(tabs).addText("|    ╲    ╱~~~~~~~╲     *     ╱~~~╲                       |  |     *                  ╱*~~╲    *  |").newLine()
                .addTab(tabs).addText("|      ╲╱           ╲     ╱╲╱       ╲  ┌-----------------------------------┬----┐  * ╱o~*~o╲      |").newLine()
                .addTab(tabs).addText("|        ╲__     ╱╲   ╲_╱    ╲____    ╲|                   %s              ╰─╮  |   ╱~o~o~~*╲     |").newLine()
                .addTab(tabs).addText("|           ╲__╱    ╲_╱        ╲       |  Expected Answer: %s                ╰──|  ╱*~~o~*~~o╲    |").newLine()
                .addTab(tabs).addText("|      ╱╲                        ╲___  |  Answer:          %s                   | ╱~o~~*~o~~*~╲   |").newLine()
                .addTab(tabs).addText("|     ╱˷˷╲    ,_____,     ╭╮╭───────╯  └----------------------------------------┘╱o~*~~o~*~~o~~╲  |").newLine()
                .addTab(tabs).addText("|   ╭──||────/_╲_____╲────╯╰╯                             |  |               ┌─┬─┐`˜`˜|˜˜˜|˜`˜´┌┬┐|").newLine()
                .addTab(tabs).addText("|   ╰────    |_|_____|                                    |  |               └─┴┬┼┐┌─┬┴┐ ┌┼┐┌─┬┴┤┘|").newLine()
                .addTab(tabs).addText("|                                                        ~~~~~~                 └┴┘└─┴─┘~└┴┘└─┴─┘ |").newLine()
                .addTab(tabs).addText("└-------------------------------------------------------------------------------------------------┘");
    }

    @Override
    protected MessageFormatter getChristmasCountdownFormatter() {
        return new CenteredOverwriteFormatter();
    }

    @Override
    protected MessageFormatter getAnswerFormatter() {
        return new RightOverwriteFormatter();
    }

    @Override
    protected MessageFormatter getExpectedAnswerFormatter() {
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
