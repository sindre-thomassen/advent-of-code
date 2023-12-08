import {PouchOfMaps} from './pouch-of-maps';
import {IChristmasPrinterInput} from '../../01/Jonas/utility/christmas-printer';

export enum LeftRightInstruction {
    LEFT = 'L',
    RIGHT = 'R'
}

export class MapNavigator {

    private pouchOfMaps: PouchOfMaps;

    constructor(pouchOfMaps: PouchOfMaps) {
        this.pouchOfMaps = pouchOfMaps;
    }

    public getStepsRequiredPart1(): IChristmasPrinterInput {
        const leftRightInstructions: LeftRightInstruction[] = this.getLeftRightInstructions();
        return {
            suggestedAnswer: 0,
            answer: this.pouchOfMaps.answer
        };
    }

    private getLeftRightInstructions(): LeftRightInstruction[] {
        return this.pouchOfMaps.value
            .split('\n')[0]
            .split('')
            .map((letter: string) => letter === 'L' ? LeftRightInstruction.LEFT : LeftRightInstruction.RIGHT);
    }
}
