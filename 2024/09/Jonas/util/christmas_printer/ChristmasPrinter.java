package util.christmas_printer;

import util.string_formatter.Message;
import util.string_formatter.replace_placeholder_formatter.ReplacePlaceholderFormatter;
import util.time.DateOfYear;
import util.time.Time;

import java.time.temporal.ChronoUnit;
import java.util.Comparator;
import java.util.stream.Stream;

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
        Stream.of(
                getChristmasCountdownDesignTask(),
                getAnswerDesignTask(),
                getExpectedAnswerDesignTask()
        )
                .sorted(Comparator.comparingInt(ChristmasPrinterDesignTask::order))
                .forEach(designTask -> design.format(designTask.replacePlaceholderFormatter(), designTask.value()));
        return design.toString();
    }

    protected abstract Message getDesign();

    protected abstract ReplacePlaceholderFormatter getChristmasCountdownFormatter();

    protected abstract ReplacePlaceholderFormatter getAnswerFormatter();

    protected abstract ReplacePlaceholderFormatter getExpectedAnswerFormatter();

    protected abstract int getChristmasCountdownOrder();

    protected abstract int getAnswerOrder();

    protected abstract int getExpectedAnswerOrder();

    private ChristmasPrinterDesignTask getChristmasCountdownDesignTask() {
        return new ChristmasPrinterDesignTask(
                getChristmasCountdown(),
                getChristmasCountdownOrder(),
                getChristmasCountdownFormatter()
        );
    }

    private ChristmasPrinterDesignTask getAnswerDesignTask() {
        return new ChristmasPrinterDesignTask(
                answer,
                getAnswerOrder(),
                getAnswerFormatter()
        );
    }

    private ChristmasPrinterDesignTask getExpectedAnswerDesignTask() {
        return new ChristmasPrinterDesignTask(
                expectedAnswer,
                getExpectedAnswerOrder(),
                getExpectedAnswerFormatter()
        );
    }

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
