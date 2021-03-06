from myhdl import block, always_comb, concat, intbv

from riscv.control_constants import *


@block
def immediate_gen(instruction, imm_type, imm):

    """
    Generates the immediate value from the instruction

    :param Signal instruction: The whole instruction
    :param Signal imm_type: The type of immediate value (I, S, U, J)
    :param Signal imm: The output immediate value
    """

    @always_comb
    def output():

        if imm_type == IMM_I:
            rep_inst_i = intbv(0)[21:]
            if instruction[31]:
                rep_inst_i = intbv((1 << 21) - 1)[21:]
            else:
                rep_inst_i = intbv(0)[21:]
            imm.next = concat(rep_inst_i, instruction[31:20])

        elif imm_type == IMM_S:
            rep_inst_s = intbv(0)[21:]
            if instruction[31]:
                rep_inst_s = intbv((1 << 21) - 1)[21:]
            else:
                rep_inst_s = intbv(0)[21:]
            imm.next = concat(rep_inst_s, instruction[31:25], instruction[12:8], instruction[7])

        elif imm_type == IMM_U:
            imm.next = concat(instruction[31], instruction[31:12], intbv(0)[12:])

        elif imm_type == IMM_J:
            rep_inst_j = intbv(0)[12:]
            if instruction[31]:
                rep_inst_j = intbv((1 << 12) - 1)[12:]
            else:
                rep_inst_j = intbv(0)[12:]
            imm.next = concat(rep_inst_j, instruction[20:12], instruction[20], instruction[31:21], False)

        else:
            rep_inst = intbv(0)[21:]
            if instruction[31]:
                rep_inst = intbv((1 << 21) - 1)[21:]
            else:
                rep_inst = intbv(0)[21:]
            imm.next = concat(rep_inst, instruction[31:20])

    return output
