platform aarch64 {

    // Registers in AArch64 state
    arch var main_mem: mem[64, 8];

    arch var pc: reg[64];

    arch var C: reg[1];

    arch var reg_0 : reg[64];
    arch var reg_1 : reg[64];
    arch var reg_2 : reg[64];
    arch var reg_3 : reg[64];
    arch var reg_4 : reg[64];
    arch var reg_5 : reg[64];
    arch var reg_6 : reg[64];
    arch var reg_7 : reg[64];
    arch var reg_8 : reg[64];
    arch var reg_9 : reg[64];
    arch var reg_10: reg[64];
    arch var reg_11: reg[64];
    arch var reg_12: reg[64];
    arch var reg_13: reg[64];
    arch var reg_14: reg[64];
    arch var reg_15: reg[64];
    arch var reg_16: reg[64];
    arch var reg_17: reg[64];
    arch var reg_18: reg[64];
    arch var reg_19: reg[64];
    arch var reg_20: reg[64];
    arch var reg_20: reg[64];
    arch var reg_20: reg[64];
    arch var reg_20: reg[64];
    arch var reg_20: reg[64];
    arch var reg_20: reg[64];
    arch var reg_20: reg[64];
    arch var reg_20: reg[64];
    arch var reg_20: reg[64];
    arch var reg_20: reg[64];
    arch var lr, reg_30: reg[64];

    arch var sp, sp_el0: reg[64];
    arch var sp_el1: reg[64];
    arch var sp_el2: reg[64];
    arch var sp_el3: reg[64];

    arch var elr_el1: reg[64];
    arch var elr_el2: reg[64];
    arch var elr_el3: reg[64];

    arch var spsr_el1: reg[32];
    arch var spsr_el2: reg[32];
    arch var spsr_el3: reg[32];

    // Flags
    flag N;
    flag Z;
    flag C;
    flag V;





}