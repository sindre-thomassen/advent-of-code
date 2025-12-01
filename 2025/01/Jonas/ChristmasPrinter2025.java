import util.christmas_printer.AdventOfCodeAnswer;
import util.christmas_printer.ChristmasPrinter;
import util.string_formatter.Message;
import util.string_formatter.replace_placeholder_formatter.CenteredOverwriteFormatter;
import util.string_formatter.replace_placeholder_formatter.ReplacePlaceholderFormatter;
import util.string_formatter.replace_placeholder_formatter.RightOverwriteFormatter;
import util.time.DateOfYear;
import util.time.Month;

public class ChristmasPrinter2025 extends ChristmasPrinter {

    public ChristmasPrinter2025(AdventOfCodeAnswer adventOfCodeAnswer) {
        super(adventOfCodeAnswer, new DateOfYear(Month.DECEMBER, 24));
    }

    @Override
    protected Message getDesign() {
        int margin = 10;

        return Message.create()
                .appendTab(margin).appendText("                    ____________________________________                         ").appendNewLine()
                .appendTab(margin).appendText("                   I_|___|___|___|___|___|___|___|___|__I                        ").appendNewLine()
                .appendTab(margin).appendText("                   I___|___| ..,a@@@a,a@@@a,.. |___|____I                        ").appendNewLine()
                .appendTab(margin).appendText("                   I_|__  .,;*;;@@@@@a@@@@@;;;;,. ___|__I                        ").appendNewLine()
                .appendTab(margin).appendText("                   I__|  ;;;;;;;;;a@@^@@a;;;*;;;;;  __|_I                        ").appendNewLine()
                .appendTab(margin).appendText("                   I_|  ;;;;*;;;a@@@   @@@a;;;;*;;;  |__I                        ").appendNewLine()
                .appendTab(margin).appendText("                   I__ ;;;;;;;a@@@@   .@@@@@;;;;;;;; __|I                        ").appendNewLine()
                .appendTab(margin).appendText("             )╲    I_| ;;*;;;a@@@@@   @@'`@@@;;;;;*; _|_I      /(                ").appendNewLine()
                .appendTab(margin).appendText("            ( ))   I__ ;;;;;;@@;;@@   `@  `@;;;*;;;; ___I     (( )               ").appendNewLine()
                .appendTab(margin).appendText("             :     I_|_ ;;;*;;@;;;;@;;;;;*;;;;;;;;; _|__I       :                ").appendNewLine()
                .appendTab(margin).appendText("            |▔|    I___| `;;;;;;*;;;;;;;;;;;*;;;;' |___|I      |▔|               ").appendNewLine()
                .appendTab(margin).appendText("            | |    I_|___|_ `;;;;;;;;*;;;;;;;;' _|___|__I      | |               ").appendNewLine()
                .appendTab(margin).appendText("         __ |_| __ I___|___|___|___|___|___|___|___|___|I_____ |_|               ").appendNewLine()
                .appendTab(margin).appendText("    ,-'    (___)                          ┍┯┯┯┯┑              (___)`-.           ").appendNewLine()
                .appendTab(margin).appendText("    ,-________________________________________________________________`.         ").appendNewLine()
                .appendTab(margin).appendText("    |~~|  ____________               %s             _______/o╲___   |~~|         ").appendNewLine()
                .appendTab(margin).appendText("    |_||  ||____|____|    Actual:   %s              |___|_/ /,╲__|  ||_|         ").appendNewLine()
                .appendTab(margin).appendText("    |__|  |___|____|_|    Expected: %s              |_|__/ /,,,╲||  ||_|         ").appendNewLine()
                .appendTab(margin).appendText("    |_||__||____|____|______________________________|___|╲/,,,,,╲|__|__|         ").appendNewLine()
                .appendTab(margin).appendText("    |____|____|____|____|____|____|____|____|____|____|___╲,,,,,,╲___|_|         ").appendNewLine()
                .appendTab(margin).appendText("    |_|____|__I####I..........  /%%%%%%%%%%%╲ ..........I##╲,,,,( )|___|         ").appendNewLine()
                .appendTab(margin).appendText("    |____|____I####I.......... .%%%%%( )%%%%%. .........I###╲,,,,╲/__|_|         ").appendNewLine()
                .appendTab(margin).appendText("    |_|____|__I####I.......... @@%%%%0%0%%%%@@  ........I## /,,,,/_|___|         ").appendNewLine()
                .appendTab(margin).appendText("    |____|____I####I.......... `@@@@@@@@@@@@@@' ........I# /,,,,/____|_|         ").appendNewLine()
                .appendTab(margin).appendText("    |_|____|__I####I............ ╲╲╲╲╲╲╲╲╲╲╲╲╲) ........I ( ╲,,/___|___|         ").appendNewLine()
                .appendTab(margin).appendText("    |____|____I####I.............  `╲╲╲╲╲╲╲╲╲╲) ........I# ╲_)/_|____|_|         ").appendNewLine()
                .appendTab(margin).appendText("    |_|____|__I####I............  A   `╲╲╲╲╲╲╲' ..   .. I## I_|____|___|         ").appendNewLine()
                .appendTab(margin).appendText("    |____|____I####I.........    AAA  .. `╲╲╲' ..  A.  .I###I___|____|_|         ").appendNewLine()
                .appendTab(margin).appendText("    |_|____|__I####I......   .A  `AAA ....  *  ..  AAA. I###I_|____|___|         ").appendNewLine()
                .appendTab(margin).appendText("    |____|____I####I....    AAA  AA;AA  ...   ...  `AAA.I###I___|____|_|         ").appendNewLine()
                .appendTab(margin).appendText("    |_|____|__I####/~~~,-.A;;A'-A;;;;;A-----A-----,A;;;AI###I_|____|___|         ").appendNewLine()
                .appendTab(margin).appendText("    |____|____I###/    I.;;;;;  ;;;;;;;   AAA     I;;;A'╲###I___|____|_|         ").appendNewLine()
                .appendTab(margin).appendText("    |_|____|__I##/     I;;;;;; ;;;;;;;   A;;;A    I;;;;  ╲##I_|____|___|         ").appendNewLine()
                .appendTab(margin).appendText("    |____|____I#/     !~;;;;;;~~~~~~~~~~~;;;;;;~~~~~!;'   ╲#I___|____|_|         ").appendNewLine()
                .appendTab(margin).appendText("    |_|____|__I/______!  ::::;;           ;;;;;;    !______╲I_|____|___|         ").appendNewLine()
                .appendTab(margin).appendText("     ~~~~~~~~~/       ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~       ╲~~~~~~~~~~          ").appendNewLine()
                .appendTab(margin).appendText("             /_______________________________________________╲                   ").appendNewLine()
                .appendTab(margin).appendText("                            /╲____/╲                                             ").appendNewLine()
                .appendTab(margin).appendText("                          .'        `,-'''`--.__                                 ").appendNewLine()
                .appendTab(margin).appendText("                     __,- :   -  -  ;  ` ::     `-. -.__                         ").appendNewLine()
                .appendTab(margin).appendText("                  ,-sssss `._  `' _,'`     ,'~~~::`.sssss-.                      ").appendNewLine()
                .appendTab(margin).appendText("                 |ssssss ,' ,_`--'_    __,' ::  `  `.ssssss|                     ").appendNewLine()
                .appendTab(margin).appendText("                |sssssss `-._____~ `,,'_______,---_;; ssssss|                    ").appendNewLine()
                .appendTab(margin).appendText("                 |ssssssssss     `--'~{__   ____   ,'ssssss|                     ").appendNewLine()
                .appendTab(margin).appendText("                  `-ssssssssssssssssss ~~~~~~~~~~~~ ssss.-'                      ").appendNewLine()
                .appendTab(margin).appendText("                       `---.sssssssssssssssssssss.---'                           ");

    }

    @Override
    protected ReplacePlaceholderFormatter getChristmasCountdownFormatter() {
        return new CenteredOverwriteFormatter();
    }

    @Override
    protected ReplacePlaceholderFormatter getAnswerFormatter() {
        return new RightOverwriteFormatter();
    }

    @Override
    protected ReplacePlaceholderFormatter getExpectedAnswerFormatter() {
        return new RightOverwriteFormatter();
    }

    @Override
    protected int getChristmasCountdownOrder() {
        return 1;
    }

    @Override
    protected int getAnswerOrder() {
        return 2;
    }

    @Override
    protected int getExpectedAnswerOrder() {
        return 3;
    }
}
