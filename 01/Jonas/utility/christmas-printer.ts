export interface IChristmasPrinterInput {
    suggestedAnswer: number | string;
    answer: number | string;
}

export class ChristmasPrinter {

    public print(value: IChristmasPrinterInput, dontPrintNow?: boolean): void {
        console.log('         ┌--------------------------------------------------------------------------------------------------------------------┐');
        console.log('         |            ^                 ^                          ┌------------------╲                                       |');
        console.log('         |╲         ╱   ╲             ╱   ╲          ^             | North Pole 807km  >                                      |');
        console.log('         |  ╲     ╱~~~~~~~╲         ╱       ╲      ╱~~~╲           └------------------╱                                       |');
        console.log('         |    ╲_╱           ╲     ╱           ╲__╱                         |  |                                               |');
        console.log('         |                    ╲_╱                       ┌----------------------------------------┐                            |');
        console.log('         |                                              |                                        |                            |');
        console.log('         |                                              | Suggested Answer:                      |                            |');
        console.log('         |                                              | Answer:           No predefined answer |                            |');
        console.log('         |                                              └----------------------------------------┘                            |');
        console.log('         |                                                                 |  |                                               |');
        console.log('         |                                                                 |  |                                               |');
        console.log('         |                                                                ~~~~~~                                              |');
        console.log('         └--------------------------------------------------------------------------------------------------------------------┘');
    }
}
