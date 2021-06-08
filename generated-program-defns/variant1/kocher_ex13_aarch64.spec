prog _generated_binaries_variant1_kocher_ex13_aarch64 {
ENTRY_4194304:
    0x400000bv64: sub__r__r__n sp, sp, 0x20bv64;
    0x400004bv64: stp__r__r__t_2_r_n_post x29, x30, (sp, 0x10bv64);
    0x400008bv64: add__r__r__n x29, sp, 0x10bv64;
    0x40000cbv64: str__r__t_2_r_n_post x0, (sp, 8);
    0x400010bv64: ldr__r__t_2_r_n_post x0, (sp, 8);
    0x400014bv64: bl__n 0x500000bv64;
ENTRY_5242880:

ENTRY_4194328:
    0x400018bv64: cbz__r__n w0, 0x400054bv64;
ENTRY_4194388:
    0x400054bv64: ldp__r__r__t_2_r_n_post x29, x30, (sp, 0x10bv64);
    0x400058bv64: add__r__r__n sp, sp, 0x20bv64;
    0x40005cbv64: ret;
ENTRY_4194332:
    0x40001cbv64: ldr__r__t_2_r_n_post x8, (sp, 8);
    0x400020bv64: adrp__r__n x9, 0x500000bv64;
    0x400024bv64: add__r__r__n x9, x9, 8;
    0x400028bv64: ldrb__r__t_2_r_r_post w10, (x9, x8);
    0x40002cbv64: movz__r__n w11, 0x200bv64;
    0x400030bv64: mul__r__r__r w10, w10, w11;
    0x400034bv64: adrp__r__n x8, 0x500000bv64;
    0x400038bv64: add__r__r__n x8, x8, 0x10bv64;
    0x40003cbv64: ldrb__r__t_2_r_r_sxtw_post w10, (x8, w10);
    0x400040bv64: adrp__r__n x8, 0x500000bv64;
    0x400044bv64: add__r__r__n x8, x8, 0x18bv64;
    0x400048bv64: ldrb__r__t_1_r_post w11, (x8);
    0x40004cbv64: and__r__r__r w10, w11, w10;
    0x400050bv64: strb__r__t_1_r_post w10, (x8);
    0x400054bv64: ldp__r__r__t_2_r_n_post x29, x30, (sp, 0x10bv64);
    0x400058bv64: add__r__r__n sp, sp, 0x20bv64;
    0x40005cbv64: ret;
}
