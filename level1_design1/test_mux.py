# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer
import random  

@cocotb.test()
async def test_mux(dut):
    """Test for mux2"""
    sl=31
    I=1

    dut.sel.value=sl
    dut.inp30.value=I
    
    await Timer(2, units='ns') 
    assert dut.out.value == I, "mux result is incorrect: out != {I}".format(
            sl=int(dut.sel.value),inp30=int(dut.I.value)) 
    
    return 


@cocotb.test()
async def mux_randomised_test(dut):
    """Test for adding 2 random numbers multiple times"""

    for i in range(20):
        sl=random.randint(0,31)
        I=random.randint(0,3)
        print("sel:{},inp:{}".format(sl,I))
        
        dut.sel.value = sl
        dut.inp30.value=I

        await Timer(2, units='ns')
        assert dut.out.value == sl & I, "Randomised test failed with: {sl} && {I} = {out}".format(sl=dut.sel.value, I=dut.inp30.value,OUT=dut.out.value)
                    
   
    
   