/// <reference path="./global.d.ts" />
// @ts-check

/**
 * Implement the functions needed to solve the exercise here.
 * Do not forget to export them so they are available for the
 * tests. Here an example of the syntax as reminder:
 *
 * export function yourFunction(...) {
 *   ...
 * }
 */

/**
 * 
 * @param {Number} remainingTime 
 * @returns 
 */
export function cookingStatus(remainingTime) {
    if (remainingTime == 0) return 'Lasagna is done.';
    if (remainingTime > 0) return 'Not done, please wait.';
    if (remainingTime == undefined) return 'You forgot to set the timer.';
};

/**
 * 
 * @param {string[]} layers 
 * @param {Number} average 
 * @returns 
 */
export function preparationTime(layers, average) {
    if (average == undefined) return layers.length * 2;
    return layers.length * average;
}

/**
 * 
 * @param {string[]} array 
 * @returns 
 */
export function quantities(array) {
    /**
     * 
     * @param {string[]} array 
     * @param {string} value 
     * @returns 
     */
    function count(array, value) {
        return array.filter(item => item === value).length;
    }
    const amountNoodles = count(array, "noodles") * 50;
    const amountSauce = count(array, "sauce") * 0.2;

    return {
        noodles: amountNoodles,
        sauce: amountSauce,
    }
}


/**
 * @param {string[]} list
 * @param {string[]} myList
 */
export function addSecretIngredient(list, myList) {
    const specialIngredient = list[list.length - 1];
    myList.push(specialIngredient);
}

/**
 * 
 * @param {object} recipe 
 * @param {Number} amount 
 * @returns 
 */
export function scaleRecipe(recipe, amount) {
    const scaledRecipe = Object.fromEntries(
        Object.entries(recipe).map(([k, v]) => [k, v * (amount / 2)])
    );
    return scaledRecipe;
}