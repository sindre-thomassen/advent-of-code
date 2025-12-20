package reader;

import java.util.List;

public class CharLineReader extends LineReader<List<Character>>{

    public CharLineReader(String path, String fileName, FileType fileType) {
        super(path, fileName, fileType);
    }

    @Override
    protected List<Character> processLine(String line) {
        return line.chars()
                .mapToObj(character -> (char) character)
                .toList();
    }
}
