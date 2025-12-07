package reader;

import table.Row;

import java.util.List;

public class CharLineReader extends LineReader<Row>{

    public CharLineReader(String path, String fileName, FileType fileType) {
        super(path, fileName, fileType);
    }

    @Override
    protected Row processLine(String line) {
        List<Character> characters = line.chars()
                .mapToObj(character -> (char) character)
                .toList();
        return new Row(characters);
    }
}
