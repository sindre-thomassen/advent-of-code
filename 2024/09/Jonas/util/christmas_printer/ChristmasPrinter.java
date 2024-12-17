package util.christmas_printer;

import util.string_formatter.Message;
import util.string_formatter.replace_placeholder_formatter.ReplacePlaceholderFormatter;
import util.time.DateOfYear;
import util.time.Time;

import java.time.temporal.ChronoUnit;

public abstract class ChristmasPrinter {

    private final String answer;
    private final String expectedAnswer;
    private final DateOfYear christmasDate;

    protected ChristmasPrinter(AdventOfCodeAnswer adventOfCodeAnswer, DateOfYear christmasDate) {
        this.answer = adventOfCodeAnswer.answer();
        this.expectedAnswer = adventOfCodeAnswer.expectedAnswer();
        this.christmasDate = christmasDate;
    }

    public void print() {
        System.out.println(getFormattedDesign());
    }

    private String getFormattedDesign() {
        Message design = getDesign();
        return design
                .format(getChristmasCountdownFormatter(), getChristmasCountdown())
                .format(getAnswerFormatter(), answer)
                .format(getExpectedAnswerFormatter(), expectedAnswer)
                .toString();
    }

    protected abstract Message getDesign();

    protected abstract ReplacePlaceholderFormatter getChristmasCountdownFormatter();

    protected abstract ReplacePlaceholderFormatter getAnswerFormatter();

    protected abstract ReplacePlaceholderFormatter getExpectedAnswerFormatter();

    protected abstract int getChristmasCountdownOrder();

    protected abstract int getAnswerOrder();

    protected abstract int getExpectedAnswerOrder();

    private String getChristmasCountdown() {
        long daysUntilChristmas = getDaysUntilChristmas();
        return daysUntilChristmas > 0 ? String.format("Days Until Christmas %s", daysUntilChristmas) : "Merry Christmas!";
    }

    private long getDaysUntilChristmas() {
        Time today = Time.now();
        Time christmas = Time.of(today.getYear(), this.christmasDate.month(), this.christmasDate.day());

        if (today.getMonth() == christmas.getMonth() && today.getDayOfMonth() == christmas.getDayOfMonth()) {
            return 0;
        } else if (today.toEpochMilli() > christmas.toEpochMilli()) {
            christmas = christmas.add(1, ChronoUnit.YEARS);
        }

        return today.getDaysUntilTime(christmas);
    }
}
