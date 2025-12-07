package reader;

public class TextLineReader extends LineReader<String> {

    public TextLineReader(String path, String fileName, FileType fileType) {
        super(path, fileName, fileType);
    }

    @Override
    protected String processLine(String line) {
        return line;
    }
}
