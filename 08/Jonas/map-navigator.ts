import {PouchOfMaps} from './pouch-of-maps';
import {IChristmasPrinterInput} from '../../01/Jonas/utility/christmas-printer';

export enum LeftRightInstruction {
    LEFT = 'L',
    RIGHT = 'R'
}

export type Direction = {[key: string]: {left: string, right: string}}

export class MapNavigator {

    private pouchOfMaps: PouchOfMaps;

    constructor(pouchOfMaps: PouchOfMaps) {
        this.pouchOfMaps = pouchOfMaps;
    }

    public getStepsRequiredPart1(): IChristmasPrinterInput {
        const leftRightInstructions: LeftRightInstruction[] = this.getLeftRightInstructions();
        const directions: Direction = this.getDirections();
        return {
            suggestedAnswer: this.getStepsTaken('AAA', 'ZZZ', leftRightInstructions, directions),
            answer: this.pouchOfMaps.answer
        };
    }

    private getLeftRightInstructions(): LeftRightInstruction[] {
        return this.pouchOfMaps.value
            .split('\n')[0]
            .split('')
            .map((letter: string) => letter === 'L' ? LeftRightInstruction.LEFT : LeftRightInstruction.RIGHT);
    }

    private getDirections(): Direction {
        const rows: string[] = this.pouchOfMaps.value
            .split('\n');
        const directions: Direction = {};
        const regExp: RegExp = new RegExp('\\w{3}', 'g');

        for (const row of rows) {
            const match: string[] = [...row.match(regExp) || []];
            if (match.length === 3) {
                directions[match[0]] = {left: match[1], right: match[2]};
            }
        }
        return directions;
    }

    private getStepsTaken(startDirection: string, endDirection: string, leftRightInstructions: LeftRightInstruction[], directions: Direction): number {
        let stepCounter: number = 0;
        let instructionIndex: number = 0;
        let nextDirection: string = startDirection;
        while (nextDirection !== endDirection) {
            stepCounter++;
            nextDirection = leftRightInstructions[instructionIndex] === LeftRightInstruction.LEFT
                ? directions[nextDirection].left
                : directions[nextDirection].right;
            instructionIndex = instructionIndex + 1 === leftRightInstructions.length ? 0 : instructionIndex + 1;
        }
        return stepCounter;
    }
}
