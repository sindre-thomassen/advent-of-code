export interface IChristmasPrinterInput {
    suggestedAnswer: number | string;
    answer: number | string;
}

export class ChristmasPrinter {

    public print(value: IChristmasPrinterInput, print?: boolean): void {
        if (print) {
            console.log('         ┌-------------------------------------------------------------------------------------------------┐');
            console.log('         |                                                 ┌------------------╲                ╲   ╱       |');
            console.log('         |╲            ^                                   | North Pole 807km  >              ─  *  ─      |');
            console.log('         |  ╲        ╱   ╲               ^                 └------------------╱                 ╱o╲        |');
            console.log('         |    ╲    ╱~~~~~~~╲           ╱~~~╲                       |  |                        ╱*~~╲       |');
            console.log('         |      ╲╱           ╲     ╱╲╱       ╲  ┌-----------------------------------┬----┐    ╱o~*~o╲      |');
            console.log(`         |        ╲__     ╱╲   ╲_╱    ╲____    ╲|     ${this.getChristmasCountdown(30)}╰─╮  |   ╱~o~o~~*╲     |`);
            console.log(`         |           ╲__╱    ╲_╱        ╲       | Suggested Answer: ${this.getMessageWithAvailableTrailingSpaces(value.suggestedAnswer, 17)} ╰──|  ╱*~~o~*~~o╲    |`);
            console.log(`         |      ╱╲                        ╲___  | Answer:           ${this.getMessageWithAvailableTrailingSpaces(value.answer, 20)} | ╱~o~~*~o~~*~╲   |`);
            console.log('         |     ╱˷˷╲    ,_____,     ╭╮╭───────╯  └----------------------------------------┘╱o~*~~o~*~~o~~╲  |');
            console.log('         |   ╭──||────/_╲_____╲────╯╰╯                             |  |               ┌─┬─┐`˜`˜|˜˜˜|˜`˜´┌┬┐|');
            console.log('         |   ╰────    |_|_____|                                    |  |               └─┴┬┼┐┌─┬┴┐ ┌┼┐┌─┬┴┤┘|');
            console.log('         |                                                        ~~~~~~                 └┴┘└─┴─┘~└┴┘└─┴─┘ |');
            console.log('         └-------------------------------------------------------------------------------------------------┘');
        }
    }

    private getMessageWithAvailableTrailingSpaces(message: number | string, spaceAvailable: number): string {
        return message.toString().padEnd(spaceAvailable);
    }

    private getChristmasCountdown(spaceAvailable: number): string {
        const daysUntilChristmas: number = 24 - new Date().getDate();
        const message: string = daysUntilChristmas > 0 ? `Days Until Christmas ${daysUntilChristmas}` : 'Merry Christmas!';
        const padStart: number = Math.round((spaceAvailable - message.length) / 2);
        const padEnd: number = spaceAvailable - padStart;
        return ''.padStart(padStart) + message.padEnd(padEnd);
    }
}
