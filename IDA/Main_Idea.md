
## Main Idea

IDA is an interactive disassembler, which means that the user takes active participation in the disassembly process. IDA is not an automatic analyzer of programs. IDA will give you hints about suspicious instructions, unsolved problem etc. It is your job to inform IDA how to proceed.

  If you are using IDA for the very first time, here are some commands that you will find very useful:

  - convert to instruction : the hotkey is "C"
  - convert to data : the hotkey is "D"
 
All the changes that you made are saved to disk. When you run IDA again, all the information on the file being diassembled is read from the disk, so that you can rescue your work.

```
CODE:00401000 6A 00                             push    0
CODE:00401002 E8 64 02 00 00                    call    GetModuleHandleA ; Call Procedure
```

Press Key `D`, and you will see:

```
CODE:00401000 6A 00                             push    0
CODE:00401000                   ; ---------------------------------------------------------------------------
CODE:00401002 E8                                db 0E8h
CODE:00401003 64                                db  64h ; d
CODE:00401004 02                                db    2
CODE:00401005 00                                db    0
CODE:00401006 00                                db    0
CODE:00401007                   ; ---------------------------------------------------------------------------
```
