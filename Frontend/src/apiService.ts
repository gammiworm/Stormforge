import axios from 'axios';

const API_URL = 'http://localhost:8000/api/';

/*
TypeScript:
- Superset of JavaScript
- Adds *static types* to JavaScript (meaning you can define types for your variables/functions to hold or return)
    - In javascript, you can do x = 1, then x = "hello" and it's fine
        - This is known as *dynamic typing*
    - In typescript, it will throw an error if x is defined as a number
- Compiles to plain JavaScript
    - So the code is ran in the browser as JavaScript

let id: number = 42; // Variable declaration. (number id = 42; in Java) (value can be changed)
const name: string = "John"; // Constant declaration (value cannot be changed)

type person = {name: string;}; // Type declaration.

function greet(guest: person) { // Function declaration (as like in Python, Java, etc)
    return "Hello, " + guest.name;
}


Types: Describes what the variable must hold, or what the function must return

    type User = {       //Example custom type
        name: string;     
        age: number;
        gender?: string; //Optional key, compiler won't throw an error if it's missing
    };

    const user1: User = {   //Example variable with custom type
        name: "Ash",
        age: 15
    };                      //This variable is valid bc both keys are filled with the correct type

    const user2: User = {   
        name: "Ash"
    };                      //This variable is invalid bc the age key is missing


Primitive types: number, string, boolean, null, undefined, symbol, bigint
    - number: integer, float
    - null: "no value"
    - undefined: a variable declared but not given a value
    - symbol: unique and immutable value (often used as object keys)
    - bigint: large integer

Other types:
    - any: any type (turns off type checking - be careful)
    - unknown: any type (but type checking is still on)
    - never: type for functions that never return (always throw an error or loop forever)
    - void: absence of value (often used for functions that don't return anything)
    - tuple: fixed-length array with fixed types    
        let rgb: [number, number, number] = [255, 0, 0]; // Fixed length and types
    - array: list of values
        let numbers: number[] = []; // Empty array of any size, but has to contain numbers
    - function: functions are objects too. They are just callable ones.

        let greet: (name: string) => string;

        greet = (name) => {
            return `Hello, ${name}`;
        };

    - enum: set of named constants
        enum UserRole {
            Admin,
            Editor,
            Viewer
          }
        let userRole: UserRole = UserRole.Editor; //usage case

    - union: value that can be one of several types (its the | symbol)
        let id: string | number; // Can be a string or a number

    - intersection: combines multiple types into one
        type User = { name: string };
        type AdminStatus = { isAdmin: boolean };

        type Admin = User & AdminStatus;

        const person1: Admin = {
            name: "Gummy",
            isAdmin: true,
        };

    - literal: exact value
        let direction: "left" | "right" | "up" | "down" = "left"; // Can only be one of these 4 values

Object types: object, array, function


export: to allow other files to use the function/type
*/

export type DataPoint = {
    id: number;
    x: number;
    y: number;
    [key: string]: any; // fallback for unknown fields if needed
  };

  export const createDataPoint = async (x: number, y: number): Promise<DataPoint> => {
    try {
        const response = await axios.post(`${API_URL}crud/`, {
            operation: 'create',
            metadata: {
                changes: { x, y }
            }
        });
        return response.data;
    } catch (error) {
        console.error("Error creating data point:", error);
        throw error;
    }
};

export const fetchDataPoints = async (): Promise<DataPoint[]> => {
    try {
        const response = await axios.get(`${API_URL}get-data-points/`);
        return response.data;
    } catch (error) {
        console.error("Error fetching data points:", error);
        throw error;
    }
};