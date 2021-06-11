inst str__r__t_2_r_n_post(arg0: reg_index_t, arg1: {reg_index_t, word_t}) {
    mem[regs[arg1._1] + arg1._1] = regs[arg0];
    pc = pc + 4bv64;
}

inst sub__r__r__n(arg0: reg_index_t, arg1: reg_index_t, arg2: word_t) {
    regs[arg0] = regs[arg1] - args2;
    pc = pc + 4bv64;
}

inst movz__r__n(arg0: reg_index_t, arg1: word_t) {
    regs[arg0] = arg1;
    pc = pc + 4bv64
}

inst cset__r__r(arg0: reg_index_t, arg1: reg_index_t) {
    // TODO: Specify me.
    // TODO: Type
}

inst str__r__t_1_r_post(arg0: reg_index_t, arg1: {reg_index_t}) {
    mem[regs[arg1._1]] = regs[arg0];
    pc = pc + 4bv64;
}

inst cmp__r__r(arg0: reg_index_t, arg1: reg_index_t) {
    // TODO: Specify me.
}

inst ldrb__r__t_1_r_post(arg0: reg_index_t, arg1: {reg_index_t}) {
    // TODO: Specify me.
}

inst add__r__r__r(arg0: reg_index_t, arg1: reg_index_t, arg2: reg_index_t) {
    // TODO: Specify me.
    regs[args0] = regs[arg1] + regs[arg2];
    pc = pc + 4bv64;
}

inst strb__r__t_1_r_post(arg0: reg_index_t, arg1: {reg_index_t}) {
    // TODO: Specify me.
}

inst ldp__r__r__t_2_r_n_post(arg0: reg_index_t, arg1: reg_index_t, arg2: {reg_index_t, word_t}) {
    // TODO: Specify me.
}

inst cbz__r__n(arg0: reg_index_t, arg1: word_t) {
    // TODO: Specify me.
}

inst ldrb__r__t_2_r_r_sxtw_post(arg0: reg_index_t, arg1: {reg_index_t, reg_index_t}) {
    // TODO: Specify me.
}

inst bl__n(arg0: word_t) {
    // TODO: Specify me.
}

inst lsl__r__r__n(arg0: reg_index_t, arg1: reg_index_t, arg2: word_t) {
    // TODO: Specify me.
}

inst eor__r__r__n(arg0: reg_index_t, arg1: reg_index_t, arg2: word_t) {
    // TODO: Specify me.
}

inst ldrb__r__t_2_r_r_post(arg0: reg_index_t, arg1: {reg_index_t, reg_index_t}) {
    // TODO: Specify me.
}

inst blr__r(arg0: reg_index_t) {
    // TODO: Specify me.
}

inst subs__r__r__n(arg0: reg_index_t, arg1: reg_index_t, arg2: word_t) {
    // TODO: Specify me.
}

inst mul__r__r__r(arg0: reg_index_t, arg1: reg_index_t, arg2: reg_index_t) {
    // TODO: Specify me.
}

inst ldrb__r__t_2_r_n_post(arg0: reg_index_t, arg1: {reg_index_t, word_t}) {
    // TODO: Specify me.
}

inst strb__r__t_2_r_n_post(arg0: reg_index_t, arg1: {reg_index_t, word_t}) {
    // TODO: Specify me.
}

inst tbnz__r__n__n(arg0: reg_index_t, arg1: word_t, arg2: word_t) {
    // TODO: Specify me.
}

inst stp__r__r__t_2_r_n_post(arg0: reg_index_t, arg1: reg_index_t, arg2: {reg_index_t, word_t}) {
    // TODO: Specify me.
}

inst cmp__r__n(arg0: reg_index_t, arg1: word_t) {
    // TODO: Specify me.
}

inst b__n(arg0: word_t) {
    // TODO: Specify me.
}

inst add__r__r__n(arg0: reg_index_t, arg1: reg_index_t, arg2: word_t) {
    // TODO: Specify me.
}

inst mov__r__r(arg0: reg_index_t, arg1: reg_index_t) {
    // TODO: Specify me.
}

inst b_hs__n(arg0: word_t) {
    // TODO: Specify me.
}

inst ldr__r__t_2_r_n_post(arg0: reg_index_t, arg1: {reg_index_t, word_t}) {
    // TODO: Specify me.
}

inst ret() {
    // TODO: Specify me.
}

inst and__r__r__r(arg0: reg_index_t, arg1: reg_index_t, arg2: reg_index_t) {
    // TODO: Specify me.
}

inst b_ne__n(arg0: word_t) {
    // TODO: Specify me.
}

inst adrp__r__n(arg0: reg_index_t, arg1: word_t) {
    // TODO: Specify me.
}

inst sxtw__r__r(arg0: reg_index_t, arg1: reg_index_t) {
    // TODO: Specify me.
}

inst ldr__r__t_1_r_post(arg0: reg_index_t, arg1: {reg_index_t}) {
    // TODO: Specify me.
}