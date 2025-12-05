import util.FileType;
import util.reader.LineReader;

import java.util.ArrayList;
import java.util.List;

public class BatteryBankReader extends LineReader<List<Long>> {

    public BatteryBankReader(String folderPath, String fileName, FileType fileType) {
        super(folderPath, fileName, fileType);
    }

    @Override
    protected List<Long> processLine(String line) {
        List<Long> batteries = new ArrayList<>();

        for (char battery : line.toCharArray()) {
            batteries.add(Long.parseLong(String.valueOf(battery)));
        }
        return batteries;
    }
}
