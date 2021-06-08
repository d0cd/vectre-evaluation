prog _generated_binaries_variant1_kocher_ex9_aarch64 {
ENTRY_4194304:
    0x400000: sub__r__r__n sp, sp, 0x10bv64;
    0x400004: str__r__t_2_r_n_post x0, (sp, 8);
    0x400008: str__r__t_1_r_post x1, (sp);
    0x40000c: ldr__r__t_1_r_post x8, (sp);
    0x400010: ldr__r__t_1_r_post w9, (x8);
    0x400014: cbz__r__n w9, 0x400050bv64;
ENTRY_4194384:
    0x400050: add__r__r__n sp, sp, 0x10bv64;
    0x400054: ret;
ENTRY_4194328:
    0x400018: ldr__r__t_2_r_n_post x8, (sp, 8);
    0x40001c: adrp__r__n x9, 0x500000bv64;
    0x400020: add__r__r__n x9, x9, 0;
    0x400024: ldrb__r__t_2_r_r_post w10, (x9, x8);
    0x400028: movz__r__n w11, 0x200bv64;
    0x40002c: mul__r__r__r w10, w10, w11;
    0x400030: adrp__r__n x8, 0x500000bv64;
    0x400034: add__r__r__n x8, x8, 8;
    0x400038: ldrb__r__t_2_r_r_sxtw_post w10, (x8, w10);
    0x40003c: adrp__r__n x8, 0x500000bv64;
    0x400040: add__r__r__n x8, x8, 0x10bv64;
    0x400044: ldrb__r__t_1_r_post w11, (x8);
    0x400048: and__r__r__r w10, w11, w10;
    0x40004c: strb__r__t_1_r_post w10, (x8);
    0x400050: add__r__r__n sp, sp, 0x10bv64;
    0x400054: ret;
}
