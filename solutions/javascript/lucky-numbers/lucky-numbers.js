// @ts-check

/**
 * Calculates the sum of the two input arrays.
 *
 * @param {number[]} array1
 * @param {number[]} array2
 * @returns {number} sum of the two arrays
 */
export function twoSum(array1, array2) {
  let firstArray = Number(array1.join(''));
  let secondArray = Number(array2.join(''));
  return firstArray + secondArray;
}

/**
 * Checks whether a number is a palindrome.
 *
 * @param {number} value
 * @returns {boolean} whether the number is a palindrome or not
 */
export function luckyNumber(value) {
  let arrayReversed = String(value).split('').reverse();
  let reversedNumber = Number(arrayReversed.join(''));
  return value == reversedNumber;
}

/**
 * Determines the error message that should be shown to the user
 * for the given input value.
 *
 * @param {string|null|undefined} input
 * @returns {string} error message
 */
export function errorMessage(input) {
  if (input == undefined || input == null || input == '') {
    return 'Required field';
  } else if (input == '0' || isNaN(input)) {
    return 'Must be a number besides 0';
  } else {
    return '';
  }
}
