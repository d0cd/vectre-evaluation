prog _generated_binaries_variant1_kocher_ex14_aarch64 {
ENTRY_4194304:
    0x400000: sub__r__r__n sp, sp, 0x10bv64;
    0x400004: adrp__r__n x8, 0x500000bv64;
    0x400008: add__r__r__n x8, x8, 0;
    0x40000c: str__r__t_2_r_n_post x0, (sp, 8);
    0x400010: ldr__r__t_2_r_n_post x9, (sp, 8);
    0x400014: ldr__r__t_1_r_post x8, (x8);
    0x400018: cmp__r__r x9, x8;
    0x40001c: b_hs__n 0x40005cbv64;
ENTRY_4194396:
    0x40005c: add__r__r__n sp, sp, 0x10bv64;
    0x400060: ret;
ENTRY_4194336:
    0x400020: ldr__r__t_2_r_n_post x8, (sp, 8);
    0x400024: eor__r__r__n x8, x8, 0xffbv64;
    0x400028: adrp__r__n x9, 0x500000bv64;
    0x40002c: add__r__r__n x9, x9, 8;
    0x400030: ldrb__r__t_2_r_r_post w10, (x9, x8);
    0x400034: movz__r__n w11, 0x200bv64;
    0x400038: mul__r__r__r w10, w10, w11;
    0x40003c: adrp__r__n x8, 0x500000bv64;
    0x400040: add__r__r__n x8, x8, 0x10bv64;
    0x400044: ldrb__r__t_2_r_r_sxtw_post w10, (x8, w10);
    0x400048: adrp__r__n x8, 0x500000bv64;
    0x40004c: add__r__r__n x8, x8, 0x18bv64;
    0x400050: ldrb__r__t_1_r_post w11, (x8);
    0x400054: and__r__r__r w10, w11, w10;
    0x400058: strb__r__t_1_r_post w10, (x8);
    0x40005c: add__r__r__n sp, sp, 0x10bv64;
    0x400060: ret;
}
