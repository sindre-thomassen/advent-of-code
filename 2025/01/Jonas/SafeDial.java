public class SafeDial {

    private static int numberCount;
    private int currentPosition;
    private int minPosition;
    private int maxPosition;
    private int numberToCount;

    public SafeDial(int startingPosition, int minPosition, int maxPosition, int numberToCount) {
        numberCount = 0;
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
        }

        countNumberIfMatch();
    }

    public void turnRight(int steps) {
        for (int i = 0; i < steps; i++) {
            if (currentPosition == maxPosition) {
                currentPosition = minPosition;
            } else {
                currentPosition++;
            }
        }

        countNumberIfMatch();
    }

    private void countNumberIfMatch() {
        if (currentPosition == numberToCount) {
            numberCount++;
        }
    }

    public int getNumberCount() {
        return numberCount;
    }
}
