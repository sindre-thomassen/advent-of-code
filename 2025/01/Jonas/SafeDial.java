public class SafeDial {

    private static int endClickCount;
    private static int allClicksCount;
    private int currentPosition;
    private final int minPosition;
    private final int maxPosition;
    private final int numberToCount;

    public SafeDial(int startingPosition, int minPosition, int maxPosition, int numberToCount) {
        endClickCount = 0;
        allClicksCount = 0;
        this.currentPosition = startingPosition;
        this.minPosition = minPosition;
        this.maxPosition = maxPosition;
        this.numberToCount = numberToCount;
    }

    public void rotate(RotationInstruction rotationInstruction) {
        if (rotationInstruction.direction() == Direction.LEFT) {
            turnLeft(rotationInstruction.steps());
        } else {
            turnRight(rotationInstruction.steps());
        }
    }

    public void turnLeft(int steps) {
        for (int i = 0; i < steps; i++) {
            if (currentPosition == minPosition) {
                currentPosition = maxPosition;
            } else {
                currentPosition--;
            }
            countAllClicksIfMathc();
        }

        countEndClickIfMatch();
    }

    public void turnRight(int steps) {
        for (int i = 0; i < steps; i++) {
            if (currentPosition == maxPosition) {
                currentPosition = minPosition;
            } else {
                currentPosition++;
            }
            countAllClicksIfMathc();
        }

        countEndClickIfMatch();
    }

    private void countEndClickIfMatch() {
        if (currentPosition == numberToCount) {
            endClickCount++;
        }
    }

    private void countAllClicksIfMathc() {
        if (currentPosition == numberToCount) {
            allClicksCount++;
        }
    }

    public int getEndClickCount() {
        return endClickCount;
    }

    public int getAllClicksCount() {
        return allClicksCount;
    }
}
