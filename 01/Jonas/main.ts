/*
Edit Configurations... > Add New Configuration > Node.js
- Node interpreter: select version
- Node parameters: --require ts-node/register
- JavaScript file: 01/Jonas/main.ts
if error, run command: npm install ts-node --save-dev
*/

import {CalibrationDecipherer} from "./typescript/calibration-decipherer";
import {CalibrationDocument} from "./typescript/calibration-document";
import {ScratchcardPointCounter} from '../../04/Jonas/scratchcard-point-counter';
import {ScratchcardCollection} from '../../04/Jonas/scratchcard-collection';
import {ChristmasPrinter} from './utility/christmas-printer';
import {MapNavigator} from '../../08/Jonas/map-navigator';
import {PouchOfMaps} from '../../08/Jonas/pouch-of-maps';


const christmasPrinter: ChristmasPrinter = new ChristmasPrinter();

const day8: MapNavigator = new MapNavigator(PouchOfMaps.REAL_DEAL);
christmasPrinter.print(day8.getStepsRequiredPart1(), true);

const day4: ScratchcardPointCounter = new ScratchcardPointCounter(ScratchcardCollection.REAL_DEAL);
christmasPrinter.print(day4.getPointsPart1(), false);

const day1: CalibrationDecipherer = new CalibrationDecipherer(CalibrationDocument.REAL_DEAL);
christmasPrinter.print(day1.getDecipheredCalibrationDocumentPart1(), false);
christmasPrinter.print(day1.getDecipheredCalibrationDocumentPart2(), false); // not working
