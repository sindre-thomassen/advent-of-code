import {ScratchcardCollection} from './scratchcard-collection';

export interface IScratchCard {
    winningNumbers: number[];
    numbers: number[];
}

export class ScratchcardPointCounter {

    private scrambledScratchcard: ScratchcardCollection;
    private readonly cardNumber: number = 1;
    private readonly numberOfWinningNumbers: number = 10;
    private readonly numberOfNumbers: number = 25;

    constructor(scratchcardCollection: ScratchcardCollection) {
        this.scrambledScratchcard = scratchcardCollection;
    }

    public getPointsPart1(): number {
        return this.getScratchCards()
            .map(scratchCard => this.getNumberOfWinnings(scratchCard))
            .map(winnings => this.getScratchcardPoints(winnings))
            .reduce((sumSoFar: number, points: number) => sumSoFar + points, 0);
    }

    private getScratchCards(): IScratchCard[] {
        return this.scrambledScratchcard.value
            .split('\n')
            .map((scratchcard: string) => this.getScratchCard(scratchcard))
    }

    private getScratchCard(scratchcard: string): IScratchCard {
        const regExp: RegExp = new RegExp('\\d+', 'g');
        const matchingNumbers: number[] = [...scratchcard.match(regExp) || []]
            .map(matchingNumber => parseInt(matchingNumber));
        if (matchingNumbers.length !== this.cardNumber + this.numberOfWinningNumbers + this.numberOfNumbers) {
            return {winningNumbers: [], numbers: []};
        }

        return {
            winningNumbers: matchingNumbers.slice(1, 11),
            numbers: matchingNumbers.slice(11)
        };
    }

    private getNumberOfWinnings(scratchcard: IScratchCard): number {
        return scratchcard.numbers
            .filter(number => scratchcard.winningNumbers.includes(number)).length;
    }

    private getScratchcardPoints(winnings: number): number {
        return winnings <= 0 ? 0 : 2 ** (winnings - 1);
    }
}
