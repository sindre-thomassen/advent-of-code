import java.io.IOException;

public class RotationReader extends TxtReader {

    public RotationReader(String path, String fileName) throws IOException {
        super(path, fileName);
    }

    public RotationInstruction getNextRotation() throws Exception {
        String readLine = getNextLine();
        if (readLine == null) {
            return null;
        }

        return new RotationInstruction(getDirection(readLine), getSteps(readLine));
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
