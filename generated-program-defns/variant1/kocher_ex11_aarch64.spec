prog _generated_binaries_variant1_kocher_ex11_aarch64 {
ENTRY_4194304:
    0x400000: sub__r__r__n sp, sp, 0x20;
    0x400004: stp__r__r__t2_post x29, x30, (sp, 0x10);
    0x400008: add__r__r__n x29, sp, 0x10;
    0x40000c: adrp__r__n x8, 0x500000;
    0x400010: add__r__r__n x8, x8, 0;
    0x400014: str__r__t2_post x0, (sp, 8);
    0x400018: ldr__r__t2_post x9, (sp, 8);
    0x40001c: ldr__r__t1_post x8, (x8);
    0x400020: cmp__r__r x9, x8;
    0x400024: b.hs__n 0x400074;
ENTRY_4194420:
    0x400074: ldp__r__r__t2_post x29, x30, (sp, 0x10);
    0x400078: add__r__r__n sp, sp, 0x20;
    0x40007c: ret;
ENTRY_4194344:
    0x400028: ldr__r__t2_post x8, (sp, 8);
    0x40002c: adrp__r__n x9, 0x500000;
    0x400030: add__r__r__n x9, x9, 8;
    0x400034: ldrb__r__t2_post w10, (x9, x8);
    0x400038: movz__r__n w11, 0x200;
    0x40003c: mul__r__r__r w10, w10, w11;
    0x400040: mov__r__r w0, w10;
    0x400044: sxtw__r__r x8, w0;
    0x400048: adrp__r__n x9, 0x500000;
    0x40004c: add__r__r__n x9, x9, 0x10;
    0x400050: add__r__r__r x1, x9, x8;
    0x400054: adrp__r__n x8, 0x500000;
    0x400058: add__r__r__n x8, x8, 0x18;
    0x40005c: mov__r__r x0, x8;
    0x400060: movz__r__n x2, 0x1;
    0x400064: str__r__t1_post x8, (sp);
    0x400068: bl__n 0x500020;
ENTRY_5242912:

ENTRY_4194412:
    0x40006c: ldr__r__t1_post x8, (sp);
    0x400070: strb__r__t1_post w0, (x8);
    0x400074: ldp__r__r__t2_post x29, x30, (sp, 0x10);
    0x400078: add__r__r__n sp, sp, 0x20;
    0x40007c: ret;
}
