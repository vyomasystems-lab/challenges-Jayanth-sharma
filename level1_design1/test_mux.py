# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer
import random  

@cocotb.test()
async def test_mux(dut):
    """Test for mux2"""
    sl=30
    print(sl)

    k=[random.randint(0,3) for i in range(32)]
    print(k)
    dut.sel.value=sl
    dut.inp0.value=k[0]
    dut.inp1.value=k[1]
    dut.inp2.value=k[2]
    dut.inp3.value=k[3]
    dut.inp4.value=k[4]
    dut.inp5.value=k[5]
    dut.inp6.value=k[6]
    dut.inp7.value=k[7]
    dut.inp8.value=k[8]
    dut.inp9.value=k[9]
    dut.inp10.value=k[10]
    dut.inp11.value=k[11]
    dut.inp12.value=k[12]
    dut.inp13.value=k[13]
    dut.inp14.value=k[14]
    dut.inp15.value=k[15]
    dut.inp16.value=k[16]
    dut.inp17.value=k[17]
    dut.inp18.value=k[18]
    dut.inp19.value=k[19]
    dut.inp20.value=k[20]
    dut.inp21.value=k[21]
    dut.inp22.value=k[22]
    dut.inp23.value=k[23]
    dut.inp24.value=k[24]
    dut.inp25.value=k[25]
    dut.inp26.value=k[26]
    dut.inp27.value=k[27]
    dut.inp28.value=k[28]
    dut.inp29.value=k[29]
    dut.inp30.value=k[30]
    
    for i in  range(0,31):
     await Timer(2, units='ns') 
     if(sl==30):
      assert dut.out.value == k[i],f'mux result is incorrect:{dut.out.value} != k[i]'
    return 



        
        
                    
   
    
   