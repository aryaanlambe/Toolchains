# Supported sources in MiBench

### [x] automotive
[x] basicmath  
[x] bitcount  
[x] qsort  
[x] susan  

### [ ] consumer
[ ] jpeg (Requires configure before make)  
[ ] lame (Requires termcap.h from libncurses5-dev)   
[ ] mad (Requires configure before make)  
[ ] tiff (Still uses cc)  
[ ] typeset (Conflicting option -c)  

### [ ] network
[x] dijkstra  
[ ] patricia (Wierd bug around line 50 riscv-compiler.py)  

### [ ] office
[ ] ghostscript (Bug not yet accessed)  
[ ] ispell (Still uses cc)  
[ ] rsynth (Requires configure before make)  
[ ] sphinx (Requires configure before make)  
[ ] stringsearch (Wierd bug around line 50 riscv-compiler.py)  

### [ ] security
[ ] blowfish (Conflicting option -c)  
[ ] pgp (Still uses cc)  
[ ] rijndael (Wierd bug around line 50 riscv-compiler.py)  
[ ] sha (Conflicting option -c)  

### [ ] telecom
[ ] adpcm (Conflicting option -c)  
[x] CRC32  
[ ] FFT (set compiler for .o files)  
[ ] gsm (Conflicting option -c)   

### 6 / 24 source passing!

### Todo buckets with count  

| TODO for riscv-compiler.py | Count |
| ---- | ----- | 
| Conflicting option -c | 5 |
| Requires configure before make | 4 |
| Wierd loop bug around line 50 | 3 |
| Still uses cc | 3 |
| set compiler for .o files | 1 |
| Requires termcap.h from libncurses5-dev | 1 |
| Bug not yet accessed | 1 |
