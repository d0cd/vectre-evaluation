inst add__r64__r64__n(arg0: bv64, arg1: bv64, arg2: bv64) {
    arg0 = add_bv64_bv64(arg1, arg2);
    pc = add_bv64_bv64(pc, 4bv64);
}

inst add__r64__r64__r64(arg0: bv64, arg1: bv64, arg2: bv64) {
    arg0 = add_bv64_bv64(arg1, arg2);
    pc = add_bv64_bv64(pc, 4bv64);
}

inst adrp__r64__n(arg0: bv64, arg1: bv64) {
    arg0 = bv_left_shift(12bv8, add_bv64_bv64(arg0, arg1));
    pc = add_bv64_bv64(pc, 4bv64);
}

inst and__r32__r32__r32(arg0: bv64, arg1: bv64, arg2: bv64) {
    arg0 = bv_zero_extend(32, and_bv32_bv32(arg1[31:0], arg2[31:0]));
    pc = add_bv64_bv64(pc, 4bv64);
}

inst and__r64__r64__r64(arg0: bv64, arg1: bv64, arg2: bv64) {
    arg0 = and_bv64_bv64(arg1, arg2);
    pc = add_bv64_bv64(pc, 4bv64);
}

inst b__n(arg0: bv64) {
    pc = arg0;
}

inst b_hs__n(arg0: bv64) {
    if (C == 1bv1) {
        pc = arg0;
    } else {
        pc = add_bv64_bv64(pc, 4bv64);
    }
}

inst b_ne__n(arg0: bv64) {
    if (Z == 0bv1) {
        pc = arg0;
    } else {
        pc = add_bv64_bv64(pc, 4bv64);
    }
}

inst bl__n(arg0: bv64) {
    gpr_30 = add_bv64_bv64(pc, 4bv64);
    pc = arg0;
}

inst blr__r64(arg0: bv64) {
    gpr_30 = add_bv64_bv64(pc, 4bv64);
    pc = arg0;
}

inst cbz__r32__n(arg0: bv64, arg1: bv64) {
    if (arg0[31:0] == 0bv32) {
        pc = arg1;
    } else {
        pc = add_bv64_bv64(pc, 4bv64);
    }
}

inst cmp__r32__r32(arg0: bv64, arg1: bv64) {
    //var new_val: bv32;
    //new_val = sub_bv32_bv32(arg1[31:0], arg2[31:0]);

    N = if (bv_slt_bv32_bv32(sub_bv32_bv32(arg1[31:0], arg2[31:0]), 0bv32)) then (1bv1) else (0bv1);
    Z = if (sub_bv32_bv32(arg1[31:0], arg2[31:0])== 0bv32) then (1bv1) else (0bv1);
    C = if (bv_ult_bv32_bv32(arg1[31:0], sub_bv32_bv32(arg1[31:0], arg2[31:0]))) then (1bv1) else (0bv1);

    V = if (l_and(neq(two_c_sign(arg1[31:0]), two_c_sign(arg2[31:0])), two_c_sign(arg2[31:0]) == two_c_sign(sub_bv32_bv32(arg1[31:0], arg2[31:0])))) then (1bv1) else (0bv1);
    pc = add_bv64_bv64(pc, 4bv64);
}

inst cmp__r64__n(arg0: bv64, arg1: bv64) {
    //var new_val: bv64;
    //new_val = sub_bv64_bv64(arg1, arg2);

    N = if (bv_slt_bv64_bv64(sub_bv64_bv64(arg1, arg2), 0bv64)) then (1bv1) else (0bv1);
    Z = if (sub_bv64_bv64(arg1, arg2) == 0bv64) then (1bv1) else (0bv1);
    C = if (bv_ult_bv64_bv64(arg1, sub_bv64_bv64(arg1, arg2))) then (1bv1) else (0bv1);
    V = if (l_and(neq(two_c_sign(arg1[31:0]), two_c_sign(arg2[31:0])), two_c_sign(arg2[31:0]) == two_c_sign(sub_bv64_bv64(arg1, arg2)))) then (1bv1) else (0bv1);
    pc = add_bv64_bv64(pc, 4bv64);
}

inst cmp__r64__r64(arg0: bv64, arg1: bv64) {
    //var new_val: bv64;
    //new_val = sub_bv64_bv64(arg1, arg2);

    N = if (bv_slt_bv64_bv64(sub_bv64_bv64(arg1, arg2), 0bv64)) then (1bv1) else (0bv1);
    Z = if (sub_bv64_bv64(arg1, arg2) == 0bv64) then (1bv1) else (0bv1);
    C = if (bv_ult_bv64_bv64(arg1, sub_bv64_bv64(arg1, arg2))) then (1bv1) else (0bv1);
    V = if (l_and(neq(two_c_sign(arg1[31:0]), two_c_sign(arg2[31:0])), two_c_sign(arg2[31:0]) == two_c_sign(sub_bv64_bv64(arg1, arg2)))) then (1bv1) else (0bv1);
    pc = add_bv64_bv64(pc, 4bv64);
}

inst cset_lo__r32(arg0: bv64) {
    if (C == 0bv1) {
        arg0 = 1bv64;
    } else {
        arg0 = 0bv64;
    }
    pc = add_bv64_bv64(pc, 4bv64);
}

inst eor__r64__r64__n(arg0: bv64, arg1: bv64, arg2: bv64) {
    arg0 = eor_bv64_bv64(arg1, arg2);
    pc = add_bv64_bv64(pc, 4bv64);
}

inst ldp__r64__r64__t_2_r64_n(arg0: bv64, arg1: bv64, arg2: {bv64, bv64}) {
    //var addr: bv64;
    //addr = add_bv64_bv64(arg2._1, arg2._2);

    arg0 = main_mem[add_bv64_bv64(arg2._1, arg2._2)];
    arg1 = main_mem[add_bv64_bv64(add_bv64_bv64(arg2._1, arg2._2), 8bv64)];
    pc = add_bv64_bv64(pc, 4bv64);
}

inst ldr__r32__t_1_r64(arg0: bv64, arg1: {bv64}) {
    arg0 = bv_zero_extend(32, (main_mem[arg1._1])[31:0]);
    pc = add_bv64_bv64(pc, 4bv64);
}

inst ldr__r64__t_1_r64(arg0: bv64, arg1: {bv64}) {
    arg0 = main_mem[arg1._1];
    pc = add_bv64_bv64(pc, 4bv64);
}

inst ldr__r64__t_2_r64_n(arg0: bv64, arg1: {bv64, bv64}) {
    arg0 = main_mem[add_bv64_bv64(arg._1, arg._2)];
    pc = add_bv64_bv64(pc, 4bv64);
}

inst ldrb__r32__t_1_r64(arg0: bv64, arg1: {bv64}) {
    arg0 = bv_zero_extend(56, (main_mem[arg1._1])[7:0]);
    pc = add_bv64_bv64(pc, 4bv64);
}

inst ldrb__r32__t_2_r64_n(arg0: bv64, arg1: {bv64, bv64}) {
    arg0 = bv_zero_extend(56, (main_mem[add_bv64_bv64(arg1._1, arg1._2)])[7:0]);
    pc = add_bv64_bv64(pc, 4bv64);
}

inst ldrb__r32__t_2_r64_r32_sxtw(arg0: bv64, arg1: {bv64, bv64}) {
    //var addr: bv64;
    //addr = add_bv64_bv64(arg1._1, bv_sign_extend(32, arg1._2[31:0]));

    arg0 = bv_zero_extend(56, (main_mem[add_bv64_bv64(arg1._1, bv_sign_extend(32, arg1._2[31:0]))])[7:0]);
    pc = add_bv64_bv64(pc, 4bv64);
}

inst ldrb__r32__t_2_r64_r64(arg0: bv64, arg1: {bv64, bv64}) {
    arg0 = bv_zero_extend(56, (main_mem[add_bv64_bv64(arg1._1, arg1._2)])[7:0]);
    pc = add_bv64_bv64(pc, 4bv64);
}

inst lsl__r64__r64__n(arg0: bv64, arg1: bv64, arg2: bv64) {
    arg0 = bv_left_shift(arg2, arg1);
    pc = add_bv64_bv64(pc, 4bv64);
}

inst mov__r32__r32(arg0: bv64, arg1: bv64) {
    arg0 = bv_zero_extend(32, arg1[31:0]);
    pc = add_bv64_bv64(pc, 4bv64);
}

inst mov__r64__r64(arg0: bv64, arg1: bv64) {
    arg0 = arg1;
    pc = add_bv64_bv64(pc, 4bv64);
}

inst movz__r32__n(arg0: bv64, arg1: bv64) {
    arg0 = bv_zero_extend(32, arg1[31:0]);
    pc = add_bv64_bv64(pc, 4bv64);
}

inst movz__r64__n(arg0: bv64, arg1: bv64) {
    arg0 = arg1;
    pc = add_bv64_bv64(pc, 4bv64);
}

inst mul__r32__r32__r32(arg0: bv64, arg1: bv64, arg2: bv64) {
    arg0 = bv_zero_extend(32, mul_bv32_bv32(arg1[31:0], arg2[31:0]));
    pc = add_bv64_bv64(pc, 4bv4);
}

inst ret(a: t) {
    pc = gpr_30;
}

inst stp__r64__r64__t_2_r64_n(arg0: bv64, arg1: bv64, arg2: {bv64, bv64}) {
    //var addr: bv64;
    //addr = add_bv64_bv64(arg2._1, arg2._2);

    main_mem[add_bv64_bv64(arg2._1, arg2._2)] = arg0;
    main_mem[add_bv64_bv64(add_bv64_bv64(arg2._1, arg2._2), 8bv64)] = arg1;
    pc = add_bv64_bv64(pc, 4bv64);
}

inst str__r64__t_1_r64(arg0: bv64, arg1: {bv64}) {
    main_mem[arg1] = arg0;
    pc = add_bv64_bv64(pc, 4bv64);
}

inst str__r64__t_2_r64_n(arg0: bv64, arg1: {bv64, bv64}) {
    main_mem[add_bv64_bv64(arg1._1, arg1._2)] = arg0;
    pc = add_bv64_bv64(pc, 4bv64);
}

inst strb__r32__t_1_r64(arg0: bv64, arg1: {bv64}) {
    main_mem[arg1] = bv_concat((main_mem[arg1])[61:8], arg0[7:0]);
    pc = add_bv64_bv64(pc, 4bv64);
}

inst strb__r32__t_2_r64_n(arg0: bv64, arg1: {bv64, bv64}) {
    main_mem[add_bv64_bv64(arg1._1, arg1._2)] = bv_concat((main_mem[add_bv64_bv64(arg1._1, arg1._2)])[61:8], arg0[7:0]);
    pc = add_bv64_bv64(pc, 4bv64);
}

inst sub__r64__r64__n(arg0: bv64, arg1: bv64, arg2: bv64) {
    arg0 = sub_bv64_bv64(arg1, arg2);
    pc = add_bv64_bv64(pc, 4bv64);
}

inst subs__r64__r64__n(arg0: bv64, arg1: bv64, arg2: bv64) {
    //var new_val: bv64;
    //new_val = sub_bv64_bv64(arg1, arg2);

    N = if (bv_slt_bv64_bv64(sub_bv64_bv64(arg1, arg2), 0bv64)) then (1bv1) else (0bv1);
    Z = if (sub_bv64_bv64(arg1, arg2) == 0bv64) then (1bv1) else (0bv1);
    C = if (bv_ult_bv64_bv64(arg1, sub_bv64_bv64(arg1, arg2))) then (1bv1) else (0bv1);
    V = if (l_and(neq(two_c_sign(arg1[31:0]), two_c_sign(arg2[31:0])), two_c_sign(arg2[31:0]) == two_c_sign(sub_bv64_bv64(arg1, arg2)))) then (1bv1) else (0bv1);
    arg0 = sub_bv64_bv64(arg1, arg2);
    pc = add_bv64_bv64(pc, 4bv64);
}

inst sxtw__r64__r32(arg0: bv64, arg1: bv64) {
    arg0 = bv_sign_extend(32, arg1[31:0]);
    pc = add_bv64_bv64(pc, 4bv64);
}

inst tbnz_0__r32__n__n(arg0: bv64, arg1: bv64) {
    if (arg0[0:0] == 1bv1) {
        pc = arg1;
    } else {
        pc = add_bv64_bv64(pc, 4bv64);
    }
}
