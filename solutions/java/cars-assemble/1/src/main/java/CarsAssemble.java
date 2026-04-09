public class CarsAssemble {

    public double productionRatePerHour(int speed) {
        double answer = 0;
        int carsPerHour = 221;
        if (speed <= 4) {
            answer = carsPerHour * speed;
        } else if (speed <= 8) {
            answer = (carsPerHour * speed) * 0.9;
        } else if (speed == 9) {
            answer = (carsPerHour * speed) * 0.8;
        } else {
            answer = (carsPerHour * speed) * 0.77;
        }

        return answer;

    }

    public int workingItemsPerMinute(int speed) {
        double workingCars = productionRatePerHour(speed);
        return (int) (workingCars / 60);
    }
}
