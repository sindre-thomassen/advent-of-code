import {CalibrationDocument} from './calibration-document';

export class CalibrationDecipherer {

    private calibrationDocument: CalibrationDocument;

    constructor(calibrationDocument: CalibrationDocument) {
        this.calibrationDocument = calibrationDocument;
    }

    public getDecipheredCalibrationDocumentPart1(): number {
        return this.getCalibrationLines()
            .map((calibrationLine: string) => this.getCalibrationValue(calibrationLine))
            .reduce((sumSoFar: number, calibrationValue: number) => sumSoFar + calibrationValue, 0);
    }

    private getCalibrationLines(): string[] {
        return this.calibrationDocument.value.split('\n');
    }

    private getCalibrationValue(line: string): number {
        const self = this;
        return parseInt(self.get1stDigitFromTheLeftAsString(line) + self.get1stDigitFromTheRightAsString(line));
    }

    private get1stDigitFromTheLeftAsString(line: string): string {
        for (const letter of line) {
            if (letter.match('[1234567890]')) {
                return letter;
            }
        }
        return '';
    }

    private get1stDigitFromTheRightAsString(line: string): string {
        for (let i = line.length - 1; i >= 0; i--) {
            const letter: string = line[i];
            if (letter.match('[1234567890]')) {
                return letter;
            }
        }
        return '';
    }
}