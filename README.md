# Welcome to the Painful World of Brain4ck
A cursed language based off of brainfuck, however all characters are numbers and are mutable.
<br>
<br>

## Idea and Syntax
This is a brainfuck version of the ideas presented in the 69420 language which you can find here: https://github.com/ProgrammerByte/69420
<br><br>
The whole idea behind the language is that every instruction is a digit which is mutable. The following table shows the conversion from brainfuck to Brain4ck:
| brainfuck  | Brain4ck | Instruction |
| ------------- | ------------- | ------------- |
| `,` | `0`  | Take numerical input from user and insert it at current data pointer |
| `.` | `1`  | Output data at data pointer as ASCII character |
| `>` | `2`  | Increment data pointer by one |
| `<` | `3`  | Decrement data pointer by one |
| `[` | `4`  | If the value at the data pointer is zero, then instead of moving the instruction pointer forward to the next command, jump it forward to the command after the matching ] command |
| `]` | `5`  |  	If the byte at the data pointer is nonzero, then instead of moving the instruction pointer forward to the next command, jump it back to the command after the matching [ command |
| `+` | `6`  | Increment value at data pointer by one |
| `-` | `7`  | Decrement value at data pointer by one |

Additionally, whenever a cell value is changed the corresponding instruction is altered modulo 8. For example if we increment memory cell `13` by 1, then the value for instruction 5 (as 13 % 8 = 5) will increment by 1, therefore instruction `5` will correspond to instruction `6`.

When the program starts the data pointer points to cell 0, and there are 32000 cells which wrap cyclically.

Here's a more concrete example:
```
060
```
In this program we take input from the user, store it in cell `0`, increment cell `0` by 1 which in turn changes the function of `0` to `1`, then we use `0` as `1` which outputs the contents of cell `0` as an ASCII character.

If we instead incremented (or decremented) the contents of cell `0` by a multiple of 8 for example with `66666666` or `77777777`, then `0` will still function as output instead of input.
<br>
<br>
<br>


## The "Hello World" program
Here is a Brain4ck "Hello World" program
```
2666666664366666666627531266664366666662753616666666116661226666663333333366336222222222222222226666666666666666666666666666666612222222266666666436666666662753666666666666666177777777777777726666436666666275366666666666166617777771666777777777771
```
<br>

## Usage of the Brain4ck interpreter
You can run a Brain4ck program with:
```
py brain4ck.py file_name
```

For example you can test the hello world program with:
```
py brain4ck.py hello_world.b4ck
```

<br>

## Debug operator

In addition to the standard brainfuck operations, Brain4ck supports a debug operation (with either `8` or `9`) which shows useful information regarding the current state of the program. For example the program
```
0690
```
shows the following debug information in the console
```
Current value being altered: 0
Current instruction values:  [1, 1, 2, 3, 4, 5, 6, 7]
Current memory address:      0
Cell and neighbors view:     [...0, 70, 0...]
```
A breakdown of this information follows:
| Information  | Meaning |
| ------------ | -------- |
| Current value being altered | Which instruction would be changed if an increment operation were to occur (this is just the memory address modulo 8) |
| Current instruction values | Shows which instruction is bound to what. For example `[1, 1, 2, 3, 4, 5, 6, 7]` shows that all instructions are unchanged, however instruction `0` is mapped onto instruction `1` |
| Current memory address | Where the data pointer currently is in memory |
| Cell and neighbors view | Shows the data in the cell pointed to by the data pointer, as well as immediate neighbors |
<br>

## Usage of the converter

If you want to convert an existing brainfuck program to Brain4ck then you can use:
```
py bf_to_b4ck.py input_file_name output_file_name
```

The program comes with a sample program hello_world_bf.txt which you can translate as follows:
```
py bf_to_b4ck.py hello_world_bf.txt hello_world.b4ck
```
This only maps brainfuck characters onto Brain4ck ones and do not account for integer mutability, so a direct mapping will almost certainly not work as intended.
