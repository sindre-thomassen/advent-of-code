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

const christmasPrinter: ChristmasPrinter = new ChristmasPrinter();
christmasPrinter.print({suggestedAnswer: 3, answer: 3});

const day4: ScratchcardPointCounter = new ScratchcardPointCounter(ScratchcardCollection.REAL_DEAL);
// console.log(day4.getPointsPart1());

const day1: CalibrationDecipherer = new CalibrationDecipherer(CalibrationDocument.REAL_DEAL);
// console.log(day1.getDecipheredCalibrationDocumentPart1());
// console.log(day1.getDecipheredCalibrationDocumentPart2()); // not working
