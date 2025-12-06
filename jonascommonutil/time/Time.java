package time;

import java.time.Instant;
import java.time.LocalDate;
import java.time.ZoneId;
import java.time.temporal.ChronoUnit;

public class Time {

    private Instant instant;

    private Time(Instant instant) {
        this.instant = instant;
    }

    public static Time now() {
        return new Time(Instant.now());
    }

    public static Time of(int year, Month month, int day) {
        Instant instant = LocalDate.of(year, month.getMonthNumber(), day)
                .atStartOfDay(ZoneId.systemDefault())
                .toInstant();
        return new Time(instant);
    }

    public int getYear() {
        return this.instant.atZone(ZoneId.systemDefault()).getYear();
    }

    public int getMonth() {
        return this.instant.atZone(ZoneId.systemDefault()).getMonth().getValue();
    }

    public int getDayOfMonth() {
        return this.instant.atZone(ZoneId.systemDefault()).getDayOfMonth();
    }

    public long getDaysUntilTime(Time time) {
        return ChronoUnit.DAYS.between(
                this.instant.atZone(ZoneId.systemDefault()).toLocalDate(),
                time.instant.atZone(ZoneId.systemDefault()).toLocalDate()
        );
    }

    public Time add(long amount, ChronoUnit unit) {
        if (unit == ChronoUnit.YEARS || unit == ChronoUnit.MONTHS) {
            this.instant = this.instant.atZone(ZoneId.systemDefault())
                    .toLocalDateTime()
                    .plus(amount, unit)
                    .atZone(ZoneId.systemDefault())
                    .toInstant();
        } else {
            this.instant = this.instant.plus(amount, unit);
        }
        return this;
    }

    public long toEpochMilli() {
        return instant.toEpochMilli();
    }
}
