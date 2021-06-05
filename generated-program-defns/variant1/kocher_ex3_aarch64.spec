prog _generated_binaries_variant1_kocher_ex3_aarch64 {
ENTRY_4194304:
    0x400000: sub__r__r__n sp, sp, 0x10;
    0x400004: movz__r__n w8, 0x200;
    0x400008: adrp__r__n x9, 0x400000;
    0x40000c: add__r__r__n x9, x9, 1;
    0x400010: adrp__r__n x10, 0x400000;
    0x400014: add__r__r__n x10, x10, 1;
    0x400018: strb__r__t2_post w0, (sp, 0xf);
    0x40001c: ldrb__r__t2_post w11, (sp, 0xf);
    0x400020: mul__r__r__r w8, w11, w8;
    0x400024: ldrb__r__t2_sxtw_post w8, (x9, w8);
    0x400028: ldrb__r__t1_post w11, (x10);
    0x40002c: and__r__r__r w8, w11, w8;
    0x400030: strb__r__t1_post w8, (x10);
    0x400034: add__r__r__n sp, sp, 0x10;
    0x400038: ret;
ENTRY_4194364:
    0x40003c: sub__r__r__n sp, sp, 0x20;
    0x400040: stp__r__r__t2_post x29, x30, (sp, 0x10);
    0x400044: add__r__r__n x29, sp, 0x10;
    0x400048: adrp__r__n x8, 0x400000;
    0x40004c: add__r__r__n x8, x8, 8;
    0x400050: str__r__t2_post x0, (sp, 8);
    0x400054: ldr__r__t2_post x9, (sp, 8);
    0x400058: ldr__r__t1_post x8, (x8);
    0x40005c: cmp__r__r x9, x8;
    0x400060: b.hs__n 0x400078;
ENTRY_4194424:
    0x400078: ldp__r__r__t2_post x29, x30, (sp, 0x10);
    0x40007c: add__r__r__n sp, sp, 0x20;
    0x400080: ret;
ENTRY_4194404:
    0x400064: ldr__r__t2_post x8, (sp, 8);
    0x400068: adrp__r__n x9, 0x400000;
    0x40006c: add__r__r__n x9, x9, 1;
    0x400070: ldrb__r__t2_post w0, (x9, x8);
    0x400074: bl__n 0x400000;
}
