prog _generated_binaries_variant1_kocher_ex13_aarch64 {
ENTRY_4194304:
    0x400000: sub__r__r__n sp, sp, 0x20bv64;
    0x400004: stp__r__r__t_2_r_n_post x29, x30, (sp, 0x10bv64);
    0x400008: add__r__r__n x29, sp, 0x10bv64;
    0x40000c: str__r__t_2_r_n_post x0, (sp, 8);
    0x400010: ldr__r__t_2_r_n_post x0, (sp, 8);
    0x400014: bl__n 0x500000bv64;
ENTRY_5242880:

ENTRY_4194328:
    0x400018: cbz__r__n w0, 0x400054bv64;
ENTRY_4194388:
    0x400054: ldp__r__r__t_2_r_n_post x29, x30, (sp, 0x10bv64);
    0x400058: add__r__r__n sp, sp, 0x20bv64;
    0x40005c: ret;
ENTRY_4194332:
    0x40001c: ldr__r__t_2_r_n_post x8, (sp, 8);
    0x400020: adrp__r__n x9, 0x500000bv64;
    0x400024: add__r__r__n x9, x9, 8;
    0x400028: ldrb__r__t_2_r_r_post w10, (x9, x8);
    0x40002c: movz__r__n w11, 0x200bv64;
    0x400030: mul__r__r__r w10, w10, w11;
    0x400034: adrp__r__n x8, 0x500000bv64;
    0x400038: add__r__r__n x8, x8, 0x10bv64;
    0x40003c: ldrb__r__t_2_r_r_sxtw_post w10, (x8, w10);
    0x400040: adrp__r__n x8, 0x500000bv64;
    0x400044: add__r__r__n x8, x8, 0x18bv64;
    0x400048: ldrb__r__t_1_r_post w11, (x8);
    0x40004c: and__r__r__r w10, w11, w10;
    0x400050: strb__r__t_1_r_post w10, (x8);
    0x400054: ldp__r__r__t_2_r_n_post x29, x30, (sp, 0x10bv64);
    0x400058: add__r__r__n sp, sp, 0x20bv64;
    0x40005c: ret;
}
