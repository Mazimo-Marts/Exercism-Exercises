// Package weather gives information about the weather in different locations.
package weather

var (
    // CurrentCondition gives the current condition of the weather when you call it.
	CurrentCondition string
    // CurrentLocation gives your current location and the information about it.
	CurrentLocation  string
)

// Forecast takes your city and the current condition of it and gives back a report as a string.
func Forecast(city, condition string) string {
	CurrentLocation, CurrentCondition = city, condition
	return CurrentLocation + " - current weather condition: " + CurrentCondition
}
