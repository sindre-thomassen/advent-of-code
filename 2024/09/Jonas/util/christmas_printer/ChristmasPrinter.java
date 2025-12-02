package util.christmas_printer;

import util.string_formatter.Message;
import util.string_formatter.replace_placeholder_formatter.ReplacePlaceholderFormatter;
import util.time.DateOfYear;
import util.time.Time;

import java.time.temporal.ChronoUnit;
import java.util.Comparator;
import java.util.stream.Stream;

public abstract class ChristmasPrinter {

    private AdventOfCodeAnswer adventOfCodeAnswer;
    private final DateOfYear christmasDate;
    private final String defaultAnswer = "?";

    protected ChristmasPrinter(DateOfYear christmasDate) {
        this.adventOfCodeAnswer = new AdventOfCodeAnswer(defaultAnswer, defaultAnswer);
        this.christmasDate = christmasDate;
    }

    public void print(int answer, int expected) {
        setAdventOfCodeAnswer(answer, expected);
        print();
    }

    public void print(int answer) {
        setAdventOfCodeAnswer(answer);
        print();
    }

    public void print(AdventOfCodeAnswer adventOfCodeAnswer) {
        this.adventOfCodeAnswer = adventOfCodeAnswer;
        print();
    }

    public void print() {
        System.out.println(getFormattedDesign());
    }

    private void setAdventOfCodeAnswer(int answer) {
        this.adventOfCodeAnswer = new AdventOfCodeAnswer(String.valueOf(answer), defaultAnswer);
    }

    public void setAdventOfCodeAnswer(int answer, int expected) {
        this.adventOfCodeAnswer = new AdventOfCodeAnswer(String.valueOf(answer), String.valueOf(expected));
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
                adventOfCodeAnswer.answer(),
                getAnswerOrder(),
                getAnswerFormatter()
        );
    }

    private ChristmasPrinterDesignTask getExpectedAnswerDesignTask() {
        return new ChristmasPrinterDesignTask(
                adventOfCodeAnswer.expectedAnswer(),
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
