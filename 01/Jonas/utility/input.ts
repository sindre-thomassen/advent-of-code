export class Input {

    protected readonly _value: string;
    protected readonly _answer: string | number;

    protected constructor(value: string, answer?: string | number) {
        this._value = value;
        this._answer = answer || `No predefined answer`;
    }

    get value() {
        return this._value;
    }

    get answer() {
        return this._answer;
    }
}
