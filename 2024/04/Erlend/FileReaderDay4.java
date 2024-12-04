import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;
import java.util.stream.Stream;

public class FileReaderDay4 {

    private final List<String> inputData = new ArrayList<String>();

    public void readInputFile(String fileName) {
        try (Stream<String> stream = Files.lines(Paths.get(fileName))) {
            stream.forEach(inputData::add);
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    public List<String> getInputData() {
        return inputData;
    }
}
