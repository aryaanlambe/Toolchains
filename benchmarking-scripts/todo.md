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

### [x] network
[x] dijkstra  
[x] patricia   

### [ ] office
[ ] ghostscript (Bug not yet accessed)  
[ ] ispell (Still uses cc)  
[ ] rsynth (Requires configure before make)  
[ ] sphinx (Requires configure before make)  
[x] stringsearch  

### [ ] security
[ ] blowfish (Conflicting option -c)  
[ ] pgp (Still uses cc)  
[ ] rijndael (Bug not yet accessed)  
[ ] sha (Conflicting option -c)  

### [ ] telecom
[ ] adpcm (Conflicting option -c)  
[x] CRC32  
[ ] FFT (set compiler for .o files)  
[ ] gsm (Conflicting option -c)   

### 8 / 24 source passing!

### Todo buckets with count  

| TODO for riscv-compiler.py | Count |
| ---- | ----- | 
| Conflicting option -c | 5 |
| Requires configure before make | 4 |
| Still uses cc | 3 |
| set compiler for .o files | 1 |
| Requires termcap.h from libncurses5-dev | 1 |
| Bug not yet accessed | 2 |
