
class BirdWatcher {
    private final int[] birdsPerDay;

    public BirdWatcher(int[] birdsPerDay) {
        this.birdsPerDay = birdsPerDay.clone();
    }

    public int[] getLastWeek() {
        return birdsPerDay;
    }

    public int getToday() {
        return birdsPerDay[6];
    }

    public void incrementTodaysCount() {
        birdsPerDay[6] = birdsPerDay[6] + 1;
    }

    public boolean hasDayWithoutBirds() {
        for (int numberBirds : birdsPerDay) {
            if (numberBirds == 0) {
                return true;
            }
            ;
        }
        return false;
    }

    public int getCountForFirstDays(int numberOfDays) {
        int counter = 0;
        for (int i = 0; i < numberOfDays; i++) {
            if (i < birdsPerDay.length) {
                counter = counter + birdsPerDay[i];
            }
        }
        ;
        return counter;
    }

    public int getBusyDays() {
        int counter = 0;
        for (int numberBirds : birdsPerDay) {
            if (numberBirds >= 5) {
                counter++;
            }
            ;
        }
        return counter;
    };
}
