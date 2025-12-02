import util.reader.TxtReader;

public class RotationReader extends TxtReader<RotationInstruction> {

    public RotationReader(String path, String fileName) {
        super(path, fileName);
    }

    @Override
    protected RotationInstruction processLine(String line) {
        if (line == null) {
            throw new NullPointerException("Null line");
        }

        return new RotationInstruction(getDirection(line), getSteps(line));
    }

    private Direction getDirection(String line) {
        char letter = line.charAt(0);
        if (letter == 'R') {
            return Direction.RIGHT;
        } else {
            return Direction.LEFT;
        }
    }

    private int getSteps(String line) {
        return Integer.parseInt(line.substring(1));
    }
}
