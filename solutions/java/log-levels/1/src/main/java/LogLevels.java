public class LogLevels {

    public static String message(String logLine) {
        String[] logMessage = logLine.split(":");
        return logMessage[1].trim();
    }

    public static String logLevel(String logLine) {
        String[] errorMessage = logLine.split(":");
        return errorMessage[0].replaceAll("\\[|\\]", "").toLowerCase();

    }

    public static String reformat(String logLine) {
        String base = "%s (%s)";
        String message = LogLevels.message(logLine);
        String error = LogLevels.logLevel(logLine);
        String reformated = String.format(base, message, error);
        return reformated;
    }
}
