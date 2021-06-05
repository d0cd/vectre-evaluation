prog _generated_binaries_variant1_kocher_ex8_aarch64 {
ENTRY_4194304:
    0x400000: sub__r__r__n sp, sp, 0x10;
    0x400004: adrp__r__n x8, 0x500000;
    0x400008: add__r__r__n x8, x8, 0;
    0x40000c: str__r__t2_post x0, (sp, 8);
    0x400010: ldr__r__t2_post x9, (sp, 8);
    0x400014: ldr__r__t1_post x8, (x8);
    0x400018: cmp__r__r x9, x8;
    0x40001c: b.hs__n 0x400030;
ENTRY_4194352:
    0x400030: mov__r__r x8, xzr;
    0x400034: str__r__t1_post x8, (sp);
    0x400038: ldr__r__t1_post x8, (sp);
    0x40003c: adrp__r__n x9, 0x500000;
    0x400040: add__r__r__n x9, x9, 8;
    0x400044: ldrb__r__t2_post w10, (x9, x8);
    0x400048: movz__r__n w11, 0x200;
    0x40004c: mul__r__r__r w10, w10, w11;
    0x400050: adrp__r__n x8, 0x500000;
    0x400054: add__r__r__n x8, x8, 0x10;
    0x400058: ldrb__r__t2_sxtw_post w10, (x8, w10);
    0x40005c: adrp__r__n x8, 0x500000;
    0x400060: add__r__r__n x8, x8, 0x18;
    0x400064: ldrb__r__t1_post w11, (x8);
    0x400068: and__r__r__r w10, w11, w10;
    0x40006c: strb__r__t1_post w10, (x8);
    0x400070: add__r__r__n sp, sp, 0x10;
    0x400074: ret;
ENTRY_4194336:
    0x400020: ldr__r__t2_post x8, (sp, 8);
    0x400024: add__r__r__n x8, x8, 1;
    0x400028: str__r__t1_post x8, (sp);
    0x40002c: b__n 0x400038;
ENTRY_4194360:
    0x400038: ldr__r__t1_post x8, (sp);
    0x40003c: adrp__r__n x9, 0x500000;
    0x400040: add__r__r__n x9, x9, 8;
    0x400044: ldrb__r__t2_post w10, (x9, x8);
    0x400048: movz__r__n w11, 0x200;
    0x40004c: mul__r__r__r w10, w10, w11;
    0x400050: adrp__r__n x8, 0x500000;
    0x400054: add__r__r__n x8, x8, 0x10;
    0x400058: ldrb__r__t2_sxtw_post w10, (x8, w10);
    0x40005c: adrp__r__n x8, 0x500000;
    0x400060: add__r__r__n x8, x8, 0x18;
    0x400064: ldrb__r__t1_post w11, (x8);
    0x400068: and__r__r__r w10, w11, w10;
    0x40006c: strb__r__t1_post w10, (x8);
    0x400070: add__r__r__n sp, sp, 0x10;
    0x400074: ret;
}
