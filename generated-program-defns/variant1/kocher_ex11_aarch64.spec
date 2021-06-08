prog _generated_binaries_variant1_kocher_ex11_aarch64 {
ENTRY_4194304:
    0x400000bv64: sub__r__r__n sp, sp, 0x20bv64;
    0x400004bv64: stp__r__r__t_2_r_n_post x29, x30, (sp, 0x10bv64);
    0x400008bv64: add__r__r__n x29, sp, 0x10bv64;
    0x40000cbv64: adrp__r__n x8, 0x500000bv64;
    0x400010bv64: add__r__r__n x8, x8, 0;
    0x400014bv64: str__r__t_2_r_n_post x0, (sp, 8);
    0x400018bv64: ldr__r__t_2_r_n_post x9, (sp, 8);
    0x40001cbv64: ldr__r__t_1_r_post x8, (x8);
    0x400020bv64: cmp__r__r x9, x8;
    0x400024bv64: b_hs__n 0x400074bv64;
ENTRY_4194420:
    0x400074bv64: ldp__r__r__t_2_r_n_post x29, x30, (sp, 0x10bv64);
    0x400078bv64: add__r__r__n sp, sp, 0x20bv64;
    0x40007cbv64: ret;
ENTRY_4194344:
    0x400028bv64: ldr__r__t_2_r_n_post x8, (sp, 8);
    0x40002cbv64: adrp__r__n x9, 0x500000bv64;
    0x400030bv64: add__r__r__n x9, x9, 8;
    0x400034bv64: ldrb__r__t_2_r_r_post w10, (x9, x8);
    0x400038bv64: movz__r__n w11, 0x200bv64;
    0x40003cbv64: mul__r__r__r w10, w10, w11;
    0x400040bv64: mov__r__r w0, w10;
    0x400044bv64: sxtw__r__r x8, w0;
    0x400048bv64: adrp__r__n x9, 0x500000bv64;
    0x40004cbv64: add__r__r__n x9, x9, 0x10bv64;
    0x400050bv64: add__r__r__r x1, x9, x8;
    0x400054bv64: adrp__r__n x8, 0x500000bv64;
    0x400058bv64: add__r__r__n x8, x8, 0x18bv64;
    0x40005cbv64: mov__r__r x0, x8;
    0x400060bv64: movz__r__n x2, 0x1bv64;
    0x400064bv64: str__r__t_1_r_post x8, (sp);
    0x400068bv64: bl__n 0x500020bv64;
ENTRY_5242912:

ENTRY_4194412:
    0x40006cbv64: ldr__r__t_1_r_post x8, (sp);
    0x400070bv64: strb__r__t_1_r_post w0, (x8);
    0x400074bv64: ldp__r__r__t_2_r_n_post x29, x30, (sp, 0x10bv64);
    0x400078bv64: add__r__r__n sp, sp, 0x20bv64;
    0x40007cbv64: ret;
}
