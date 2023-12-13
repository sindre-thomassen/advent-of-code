import {PouchOfMaps} from './pouch-of-maps';
import {IChristmasPrinterInput} from '../../01/Jonas/utility/christmas-printer';

export enum LeftRightInstruction {
    LEFT = 'L',
    RIGHT = 'R'
}

export interface ICurrentLocation {
    startDirection: string
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
            suggestedAnswer: this.getStepsTaken(
                this.getStartingLocationsPart1(),
                this.hasReachedGoalPart1,
                leftRightInstructions,
                directions
            ),
            answer: this.pouchOfMaps.answer
        };
    }

    public getStepsRequiredPart2(): IChristmasPrinterInput {
        const leftRightInstructions: LeftRightInstruction[] = this.getLeftRightInstructions();
        const directions: Direction = this.getDirections();
        return {
            suggestedAnswer: this.getStepsTaken(
                this.getStartingLocationsPart2(directions),
                this.hasReachedGoalPart2,
                leftRightInstructions,
                directions
            ),
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

    private getStepsTaken(currentLocations: ICurrentLocation[], hasReachedGoal: (currentLocation: string) => boolean, leftRightInstructions: LeftRightInstruction[], directions: Direction): number {
        let stepCounter: number = 0;
        let instructionIndex: number = 0;
        let allHasReachedGoal: boolean = false;
        while (!allHasReachedGoal) {
            stepCounter++;

            for (const currentLocation of currentLocations) {
                currentLocation.startDirection = leftRightInstructions[instructionIndex] === LeftRightInstruction.LEFT
                    ? directions[currentLocation.startDirection].left
                    : directions[currentLocation.startDirection].right;
            }

            allHasReachedGoal = currentLocations
                .filter((currentLocation: ICurrentLocation) => hasReachedGoal(currentLocation.startDirection)).length === currentLocations.length;
            instructionIndex = instructionIndex + 1 === leftRightInstructions.length ? 0 : instructionIndex + 1;
        }
        return stepCounter;
    }

    private getStartingLocationsPart1(): ICurrentLocation[] {
        return [{
            startDirection: 'AAA'
        }];
    }

    private getStartingLocationsPart2(directions: Direction): ICurrentLocation[] {
        const startingLocations: ICurrentLocation[] = [];
        for (const directionKey in directions) {
            if (directionKey[2] === 'A') {
                startingLocations.push({
                    startDirection: directionKey
                });
            }
        }
        return startingLocations;
    }

    private hasReachedGoalPart1(currentLocation: string): boolean {
        return currentLocation === 'ZZZ';
    }

    private hasReachedGoalPart2(currentLocation: string): boolean {
        return currentLocation.length === 3 && currentLocation[2] === 'Z';
    }
}
