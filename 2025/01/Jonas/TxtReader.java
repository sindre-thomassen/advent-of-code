import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.Iterator;

public abstract class TxtReader<ProcessedLineType> implements Iterable<ProcessedLineType> {

    private final BufferedReader reader;

    public TxtReader(String path, String fileName) {
        try {
            this.reader = new BufferedReader(new FileReader(createFilePath(path, fileName)));
        } catch (IOException e) {
            throw new RuntimeException("Failed to open file", e);
        }
    }

    private String createFilePath(String path, String fileName) {
        return path + "/" + fileName + ".txt";
    }

    protected abstract ProcessedLineType processLine(String line);

    @Override
    public Iterator<ProcessedLineType> iterator() {
        return new Iterator<>() {
            private String nextRawLine = readNextLine();
            private boolean hasReachedEndOfFile = false;

            private String readNextLine() {
                try {
                    String readLine = reader.readLine();
                    if (readLine == null) {
                        hasReachedEndOfFile = true;
                        reader.close();
                    }
                    return readLine;
                } catch (IOException e) {
                    throw new RuntimeException(e);
                }
            }

            @Override
            public boolean hasNext() {
                return !hasReachedEndOfFile;
            }

            @Override
            public ProcessedLineType next() {
                String lineToReturn = nextRawLine;
                nextRawLine = readNextLine();
                return processLine(lineToReturn);
            }
        };
    }
}
