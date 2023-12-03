import {CalibrationDocument} from './calibration-document';

export class CalibrationDecipherer {

    private calibrationDocument: CalibrationDocument;

    constructor(calibrationDocument: CalibrationDocument) {
        this.calibrationDocument = calibrationDocument;
    }

    public getDecipheredCalibrationDocumentPart1(): number {
        return this.getCalibrationLines()
            .map((calibrationLine: string) => this.getCalibrationValuePart1(calibrationLine))
            .reduce((sumSoFar: number, calibrationValue: number) => sumSoFar + calibrationValue, 0);
    }

    public getDecipheredCalibrationDocumentPart2(): number {
        return this.getCalibrationLines()
            .map((calibrationLine: string) => this.getCalibrationValuePart2(calibrationLine))
            .reduce((sumSoFar: number, calibrationValue: number) => sumSoFar + calibrationValue, 0);
    }

    private getCalibrationLines(): string[] {
        return this.calibrationDocument.value.split('\n');
    }

    private getCalibrationValuePart1(line: string): number {
        const self = this;
        return parseInt('' +
            self.get1stDigitFromTheLeftPart1(line) +
            self.get1stDigitFromTheRightPart1(line)
        );
    }

    private get1stDigitFromTheLeftPart1(line: string): number {
        for (const letter of line) {
            if (letter.match('[0-9]')) {
                return parseInt(letter);
            }
        }
        return -1;
    }

    private get1stDigitFromTheRightPart1(line: string): number {
        for (let i = line.length - 1; i >= 0; i--) {
            const letter: string = line[i];
            if (letter.match('[0-9]')) {
                return parseInt(letter);
            }
        }
        return -1;
    }

    private getCalibrationValuePart2(line: string): number {
        return parseInt('' +
            this.get1stDigitFromTheLeftPart2(line) +
            this.get1stDigitFromTheRightPart2(line)
        );
    }

    private get1stDigitFromTheLeftPart2(line: string): number {
        const regExp: RegExp = new RegExp('one|two|three|four|five|six|seven|eight|nine|[0-9]');
        const firstMatch: string = [...line.match(regExp) || ['']][0];
        return this.convertWordOrDigitToDigit(firstMatch);
    }

    private get1stDigitFromTheRightPart2(line: string): number {
        const regExp: RegExp = new RegExp('one|two|three|four|five|six|seven|eight|nine|[0-9]', 'g');
        const lastMatch: string = [...line.match(regExp) || []]
            .reduce((firstMatch: string, currentMatch: string) => currentMatch);
        return this.convertWordOrDigitToDigit(lastMatch);
    }

    private convertWordOrDigitToDigit(wordOrDigit: string): number {
        switch (wordOrDigit) {
            case 'one':
                return 1;
            case 'two':
                return 2;
            case 'three':
                return 3;
            case 'four':
                return 4;
            case 'five':
                return 5;
            case 'six':
                return 6;
            case 'seven':
                return 7;
            case 'eight':
                return 8;
            case 'nine':
                return 9;
            default:
                return parseInt(wordOrDigit);
        }
    }
}