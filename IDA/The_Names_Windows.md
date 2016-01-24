
## The Names Window

The Names window, provides a summary listing of all of the global names within a binary. A name is nothing more than a symbolic description given to a program virtual address. IDA initially derives the list of names from symbol-table and signature analysis during the initial loading of a file. Names can be sorted alphabetically or in virtual address order (either ascending or descending). The Names window is useful for rapidly navigating to known locations within a program listing. Double-clicking any Names window entry will immediately jump the disassembly view to display the selected name.

Displayed names are both color and letter coded. The coding scheme is summaried below:

- **F**  A regular function. These are functions that IDA does not recognize as library functions.
- **L**  A library function. IDA recognizes library functions through the use of signature-matching algoriths. If a signature does not exist for a given library function, the function will be labeled as a regular function instead.
- **I**  An imported name, most commonly a function name imported from a shared library. The different between this and a library function is that no code is present for an imported name, while the body of a library function will be present in the disassembly.
- **C** Named code*. These are named program instruction locations that IDA does not consider to be part of any function. This is posible when IDA finds a name in a program's symbol table but never sees a call to the corresponding program location..
- **D** Data. Named data locations typically represent global variables.
- **A** String data. This is a referenced data location containing a sequence of characters that conform to one of IDA's known string data types, such as a null-terminated ASCII C string.


