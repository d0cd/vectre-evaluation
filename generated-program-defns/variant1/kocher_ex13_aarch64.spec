prog _generated_binaries_variant1_kocher_ex13_aarch64 {
ENTRY_4194304:
    0x400000: sub__r64__r64__n sp, sp, 0x20bv64;
    0x400004: stp__r64__r64__t_2_r_n gpr_29, gpr_30, (sp, 0x10bv64);
    0x400008: add__r64__r64__n gpr_29, sp, 0x10bv64;
    0x40000c: str__r64__t_2_r_n gpr_0, (sp, 8);
    0x400010: ldr__r64__t_2_r_n gpr_0, (sp, 8);
    0x400014: bl__n 0x500000bv64;

ENTRY_4194328:
    0x400018: cbz__r32__n gpr_0, 0x400054bv64;
ENTRY_4194388:
    0x400054: ldp__r64__r64__t_2_r_n gpr_29, gpr_30, (sp, 0x10bv64);
    0x400058: add__r64__r64__n sp, sp, 0x20bv64;
    0x40005c: ret;
ENTRY_4194332:
    0x40001c: ldr__r64__t_2_r_n gpr_8, (sp, 8);
    0x400020: adrp__r64__n gpr_9, 0x500000bv64;
    0x400024: add__r64__r64__n gpr_9, gpr_9, 8;
    0x400028: ldrb__r32__t_2_r_r gpr_10, (x9, x8);
    0x40002c: movz__r32__n gpr_11, 0x200bv64;
    0x400030: mul__r32__r32__r32 gpr_10, gpr_10, gpr_11;
    0x400034: adrp__r64__n gpr_8, 0x500000bv64;
    0x400038: add__r64__r64__n gpr_8, gpr_8, 0x10bv64;
    0x40003c: ldrb__r32__t_2_r_r_sxtw gpr_10, (x8, w10);
    0x400040: adrp__r64__n gpr_8, 0x500000bv64;
    0x400044: add__r64__r64__n gpr_8, gpr_8, 0x18bv64;
    0x400048: ldrb__r32__t_1_r gpr_11, (x8);
    0x40004c: and__r32__r32__r32 gpr_10, gpr_11, gpr_10;
    0x400050: strb__r32__t_1_r gpr_10, (x8);
    0x400054: ldp__r64__r64__t_2_r_n gpr_29, gpr_30, (sp, 0x10bv64);
    0x400058: add__r64__r64__n sp, sp, 0x20bv64;
    0x40005c: ret;
}
