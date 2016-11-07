
## Background Analysis

IDA can analyze a program when it is not occupied performing an action you prompted. You disassemble a program together with IDA, but your requests have priority. 

  The state of background analysis is shown on the upper right-hand corner of the screen.

  You can disable autoanalysis, but in this case some functions of IDA will produce strange results (e.g. if you try to convert data into instructions, IDA will NOT trace all the threads of control flow and the data will be converted into instructions only on the screen...) 
