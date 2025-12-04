package util;

public enum FileType {
    TXT("txt"),
    CSV("csv");

    private String suffix;

    FileType(String suffix) {
        this.suffix = suffix;
    }

    public String getSuffix() {
        return suffix;
    }
}
