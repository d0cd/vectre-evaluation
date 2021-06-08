prog _generated_binaries_variant1_kocher_ex2_aarch64 {
ENTRY_4194304:
    0x400000bv64: sub__r__r__n sp, sp, 0x10bv64;
    0x400004bv64: movz__r__n w8, 0x200bv64;
    0x400008bv64: adrp__r__n x9, 0x500000bv64;
    0x40000cbv64: add__r__r__n x9, x9, 0;
    0x400010bv64: adrp__r__n x10, 0x500000bv64;
    0x400014bv64: add__r__r__n x10, x10, 8;
    0x400018bv64: strb__r__t_2_r_n_post w0, (sp, 0xfbv64);
    0x40001cbv64: ldrb__r__t_2_r_n_post w11, (sp, 0xfbv64);
    0x400020bv64: mul__r__r__r w8, w11, w8;
    0x400024bv64: ldrb__r__t_2_r_r_sxtw_post w8, (x9, w8);
    0x400028bv64: ldrb__r__t_1_r_post w11, (x10);
    0x40002cbv64: and__r__r__r w8, w11, w8;
    0x400030bv64: strb__r__t_1_r_post w8, (x10);
    0x400034bv64: add__r__r__n sp, sp, 0x10bv64;
    0x400038bv64: ret;
ENTRY_4194364:
    0x40003cbv64: sub__r__r__n sp, sp, 0x20bv64;
    0x400040bv64: stp__r__r__t_2_r_n_post x29, x30, (sp, 0x10bv64);
    0x400044bv64: add__r__r__n x29, sp, 0x10bv64;
    0x400048bv64: adrp__r__n x8, 0x500000bv64;
    0x40004cbv64: add__r__r__n x8, x8, 0x10bv64;
    0x400050bv64: adrp__r__n x9, 0x500000bv64;
    0x400054bv64: add__r__r__n x9, x9, 0x18bv64;
    0x400058bv64: str__r__t_2_r_n_post x0, (sp, 8);
    0x40005cbv64: ldr__r__t_2_r_n_post x10, (sp, 8);
    0x400060bv64: ldr__r__t_1_r_post x8, (x8);
    0x400064bv64: cmp__r__r x10, x8;
    0x400068bv64: str__r__t_1_r_post x9, (sp);
    0x40006cbv64: b_hs__n 0x400088bv64;
ENTRY_4194440:
    0x400088bv64: ldp__r__r__t_2_r_n_post x29, x30, (sp, 0x10bv64);
    0x40008cbv64: add__r__r__n sp, sp, 0x20bv64;
    0x400090bv64: ret;
ENTRY_4194416:
    0x400070bv64: ldr__r__t_2_r_n_post x8, (sp, 8);
    0x400074bv64: adrp__r__n x9, 0x500000bv64;
    0x400078bv64: add__r__r__n x9, x9, 0x20bv64;
    0x40007cbv64: ldrb__r__t_2_r_r_post w0, (x9, x8);
    0x400080bv64: ldr__r__t_1_r_post x8, (sp);
    0x400084bv64: blr__r x8;
ENTRY_6295640:

}
