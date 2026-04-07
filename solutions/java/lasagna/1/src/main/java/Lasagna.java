public class Lasagna {

    public int expectedMinutesInOven() {
        int time = 40;
        return time;
    }

    public int remainingMinutesInOven(int timeInOven) {
        int remainingTime = expectedMinutesInOven() - timeInOven;
        return remainingTime;
    }

    public int preparationTimeInMinutes(int layers) {
        int timePreparing = layers * 2;
        return timePreparing;
    }

    public int totalTimeInMinutes(int layers, int timeInOven) {
        int totalTime = preparationTimeInMinutes(layers) + timeInOven;
        return totalTime;
    }
}
