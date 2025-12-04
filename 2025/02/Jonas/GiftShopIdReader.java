import util.FileType;
import util.reader.CsvReader;

public class GiftShopIdReader extends CsvReader<Range> {

    public GiftShopIdReader(String filePath, String fileName, FileType fileType) {
        super(filePath, fileName, fileType);
    }

    @Override
    protected Range parseCsvLine(String line) {
        String[] parts = line.split("-");
        long start = Long.parseLong(parts[0]);
        long end = Long.parseLong(parts[1]);
        return new Range(start, end);
    }
}
