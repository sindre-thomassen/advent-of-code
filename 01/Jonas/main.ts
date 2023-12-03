/*
Edit Configurations... > Add New Configuration > Node.js
- Node interpreter: select version
- Node parameters: --require ts-node/register
- JavaScript file: 01/Jonas/main.ts
if error, run command: npm install ts-node --save-dev
*/

import {CalibrationDecipherer} from "./typescript/calibration-decipherer";
import {CalibrationDocument} from "./typescript/calibration-document";

const day1: CalibrationDecipherer = new CalibrationDecipherer(CalibrationDocument.REAL_DEAL);
// console.log(day1.getDecipheredCalibrationDocumentPart1());
console.log('Answer:            ', day1.getDecipheredCalibrationDocumentPart2());
console.log('Predefined answer: ', CalibrationDocument.REAL_DEAL.answer);
