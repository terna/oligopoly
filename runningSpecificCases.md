The files T1.pdf, T2.pdf, and T3.pdf are in this folder.

**To run the experiments of the cases *0a* and *0b***, we need to use the
Oligopoly code version V5 or V5bP2_fd, running the project with SLAPP 2.0,
which is at [https://github.com/terna/SLAPP2](https://github.com/terna/SLAPP2) and controlling that the parameters are those of rows 1 and 2 of Tables T1.pdf and T2.pdf here. Using that SMAC (Simple Market Aggregate Clearing mechanism) specific version of the *oligopoly* project, the *startHayekianMarket* parameter is not used, while in the Table T2.pdf is set to 51 by default.

To set the correct parameters, for the cases *0a* and *0b** we can simply modify the parameter absoluteBarrierToBecomeEntrepreneur at row 123 of the file commonVar.py of the above releases of Oligopoly (20 in case *0a* and 0 in case *0b*).

**To run the experiments of the cases from *1* to *7* (with *7b*)**
* delete the file schedule.xls;
* duplicate the file schedule6.xls.backwardCompatibily;
* rename the result as schedule.xls.

The experiments from *1* to *7* also run without these modifications, but producing slightly different results.

**To run the experiments of the cases from *8* upwards**

If we made the modifications above:
* delete the file schedule.xls;
* duplicate the file schedule6.xls;
* rename the result as schedule.xls.

**For each specific experiment**:

* delete the files commonVar.py,  workers.txtx, entrepreneurs.txt;

* for case *X*, duplicate the files commonVar.py.caseX, workers.txtx.caseX, entrepreneurs.txt.caseX;

* rename the results as commonVar.py,  workers.txtx, entrepreneurs.txt.
