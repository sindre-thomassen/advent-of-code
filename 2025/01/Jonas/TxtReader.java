import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class TxtReader implements AutoCloseable {

    private final BufferedReader reader;
    private String nextLine;

    public TxtReader(String path, String fileName) throws IOException {
        this.reader = new BufferedReader(new FileReader(createFilePath(path, fileName)));
        readNextLine();
    }

    protected String getNextLine() throws Exception {
        if (!hasNextLine()) {
            return null;
        }
        String lineToReturn = nextLine;
        readNextLine();
        return lineToReturn;
    }

    public boolean hasNextLine() {
        return nextLine != null;
    }

    private String createFilePath(String path, String fileName) {
        return path + "/" + fileName + ".txt";
    }

    private void readNextLine() throws IOException {
        nextLine = reader.readLine();
    }

    @Override
    public void close() throws IOException {
        if (reader != null) {
            reader.close();
        }
    }
}
