platform aarch64 {

    arch var main_mem: mem_t;
    march var addr0: bv64;
    march var addr1: bv64;
    march var bp_state: bp_state_t;
    march var spec_enabled: boolean;

    arch var pc: bv64;

    arch var gpr_0 : bv64;
    arch var gpr_1 : bv64;
    arch var gpr_2 : bv64;
    arch var gpr_3 : bv64;
    arch var gpr_4 : bv64;
    arch var gpr_5 : bv64;
    arch var gpr_6 : bv64;
    arch var gpr_7 : bv64;
    arch var gpr_8 : bv64;
    arch var gpr_9 : bv64;
    arch var gpr_10: bv64;
    arch var gpr_11: bv64;
    arch var gpr_12: bv64;
    arch var gpr_13: bv64;
    arch var gpr_14: bv64;
    arch var gpr_15: bv64;
    arch var gpr_16: bv64;
    arch var gpr_17: bv64;
    arch var gpr_18: bv64;
    arch var gpr_19: bv64;
    arch var gpr_21: bv64;
    arch var gpr_22: bv64;
    arch var gpr_23: bv64;
    arch var gpr_24: bv64;
    arch var gpr_25: bv64;
    arch var gpr_26: bv64;
    arch var gpr_27: bv64;
    arch var gpr_28: bv64;
    arch var gpr_29: bv64;
    arch var gpr_30: bv64;
    arch var sp: bv64;

    // Condition Flags
    arch var N: bv1;
    arch var Z: bv1;
    arch var C: bv1;
    arch var V: bv1;


}