import {PouchOfMaps} from './pouch-of-maps';
import {IChristmasPrinterInput} from '../../01/Jonas/utility/christmas-printer';

export class MapNavigator {

    private pouchOfMaps: PouchOfMaps;

    constructor(pouchOfMaps: PouchOfMaps) {
        this.pouchOfMaps = pouchOfMaps;
    }

    public getStepsRequiredPart1(): IChristmasPrinterInput {

        return {
            suggestedAnswer: 0,
            answer: this.pouchOfMaps.answer
        };
    }
}
