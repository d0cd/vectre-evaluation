prog _generated_binaries_variant1_kocher_ex10_aarch64 {
ENTRY_4194304:
    0x400000bv64: sub__r__r__n sp, sp, 0x10bv64;
    0x400004bv64: adrp__r__n x8, 0x500000bv64;
    0x400008bv64: add__r__r__n x8, x8, 0;
    0x40000cbv64: str__r__t_2_r_n_post x0, (sp, 8);
    0x400010bv64: strb__r__t_2_r_n_post w1, (sp, 7);
    0x400014bv64: ldr__r__t_2_r_n_post x9, (sp, 8);
    0x400018bv64: ldr__r__t_1_r_post x8, (x8);
    0x40001cbv64: cmp__r__r x9, x8;
    0x400020bv64: b.hs__n 0x400060bv64;
ENTRY_4194400:
    0x400060bv64: add__r__r__n sp, sp, 0x10bv64;
    0x400064bv64: ret;
ENTRY_4194340:
    0x400024bv64: ldr__r__t_2_r_n_post x8, (sp, 8);
    0x400028bv64: adrp__r__n x9, 0x500000bv64;
    0x40002cbv64: add__r__r__n x9, x9, 8;
    0x400030bv64: ldrb__r__t_2_r_r_post w10, (x9, x8);
    0x400034bv64: ldrb__r__t_2_r_n_post w11, (sp, 7);
    0x400038bv64: cmp__r__r w10, w11;
    0x40003cbv64: b.ne__n 0x400060bv64;
ENTRY_4194368:
    0x400040bv64: adrp__r__n x8, 0x500000bv64;
    0x400044bv64: add__r__r__n x8, x8, 0x10bv64;
    0x400048bv64: ldrb__r__t_1_r_post w9, (x8);
    0x40004cbv64: adrp__r__n x8, 0x500000bv64;
    0x400050bv64: add__r__r__n x8, x8, 0x18bv64;
    0x400054bv64: ldrb__r__t_1_r_post w10, (x8);
    0x400058bv64: and__r__r__r w9, w10, w9;
    0x40005cbv64: strb__r__t_1_r_post w9, (x8);
    0x400060bv64: add__r__r__n sp, sp, 0x10bv64;
    0x400064bv64: ret;
}
