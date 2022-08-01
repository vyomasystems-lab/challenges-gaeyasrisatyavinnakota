# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer
import random
@cocotb.test()
async def test_mux(dut):
    """Test for mux2"""
    for i in range(10):
        for i in range(31):

            A = i
            B = [0 for i in range(31)]
            dut.sel.value = A
            for i in range(31):
                B[i] = random.randint(0, 1)
            dut.inp0.value = B[0]
            dut.inp1.value = B[1]
            dut.inp2.value = B[2]
            dut.inp3.value = B[3]
            dut.inp4.value = B[4]
            dut.inp5.value = B[5]
            dut.inp6.value = B[6]
            dut.inp7.value = B[7]
            dut.inp8.value = B[8]
            dut.inp9.value = B[9]
            dut.inp10.value = B[10]
            dut.inp11.value = B[11]
            dut.inp12.value = B[12]
            dut.inp13.value = B[13]
            dut.inp14.value = B[14]
            dut.inp15.value = B[15]
            dut.inp16.value = B[16]
            dut.inp17.value = B[17]
            dut.inp18.value = B[18]
            dut.inp19.value = B[19]
            dut.inp20.value = B[20]
            dut.inp21.value = B[21]
            dut.inp22.value = B[22]
            dut.inp23.value = B[23]
            dut.inp24.value = B[24]
            dut.inp25.value = B[25]
            dut.inp26.value = B[26]
            dut.inp27.value = B[27]
            dut.inp28.value = B[28]
            dut.inp29.value = B[29]
            dut.inp30.value = B[30]


            await Timer(2, units='ns')
            
            #dut._log.info(f'A={A:05} B={B:05} model={A+B:05} DUT={int(dut.sum.value):05}')
            assert dut.out.value == B[A], "Test failed for: sel = {A} , output expected= {B}, output observed = {SUM}".format(
                A=dut.sel.value, B = B[A], SUM=dut.out.value)

    cocotb.log.info('##### Test Results for all values of Select input ########')

