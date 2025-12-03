package util.reader;

import util.FileType;

import java.util.Arrays;
import java.util.Iterator;
import java.util.List;

public abstract class CsvReader<T> implements Iterable<T> {

    private final String filePath;
    private final String fileName;
    private final FileType fileType;

    public CsvReader(String filePath, String fileName, FileType fileType) {
        this.filePath = filePath;
        this.fileName = fileName;
        this.fileType = fileType;
    }
    
    protected abstract T parseCsvLine(String line);
    
    @Override
    public Iterator<T> iterator() {
        return new Iterator<>() {
            private int currentIndex = 0;
            private final List<String> fields = getFields();


            private List<String> getFields() {
                String regex = ",\\s*(?=(([^\"]*\"){2})*[^\"]*$)";
                String[] rawFields = getFileInOneLine().split(regex, -1);

                return Arrays.stream(rawFields)
                        .map(this::getCleanedField)
                        .toList();
            }

            private String getFileInOneLine() {
                String fileContentInOneLine = "";
                for (String line : new TextLineReader(filePath, fileName, fileType)) {
                    fileContentInOneLine += line;
                }
                return fileContentInOneLine;
            }

            private String getCleanedField(String rawField) {
                if (rawField.length() >= 2 && rawField.startsWith("\"") && rawField.endsWith("\"")) {
                    String cleanedField = rawField.substring(1, rawField.length() - 1);
                    return cleanedField.replace("\"\"", "\"");
                }
                return rawField;
            }

            @Override
            public boolean hasNext() {
                return currentIndex < fields.size();
            }

            @Override
            public T next() {
                return parseCsvLine(fields.get(currentIndex++));
            }
        };
    }
}
