prog _generated_binaries_variant1_kocher_ex10_aarch64 {
ENTRY_4194304:
    0x400000: sub__r64__r64__n sp, sp, 0x10bv64;
    0x400004: adrp__r64__n gpr_8, 0x500000bv64;
    0x400008: add__r64__r64__n gpr_8, gpr_8, 0;
    0x40000c: str__r64__t_2_r64_n gpr_0, (sp, 8);
    0x400010: strb__r32__t_2_r64_n gpr_1, (sp, 7);
    0x400014: ldr__r64__t_2_r64_n gpr_9, (sp, 8);
    0x400018: ldr__r64__t_1_r64 gpr_8, (gpr_8);
    0x40001c: cmp__r64__r64 gpr_9, gpr_8;
    0x400020: b_hs__n 0x400060bv64;
ENTRY_4194400:
    0x400060: add__r64__r64__n sp, sp, 0x10bv64;
    0x400064: ret;
ENTRY_4194340:
    0x400024: ldr__r64__t_2_r64_n gpr_8, (sp, 8);
    0x400028: adrp__r64__n gpr_9, 0x500000bv64;
    0x40002c: add__r64__r64__n gpr_9, gpr_9, 8;
    0x400030: ldrb__r32__t_2_r64_r64 gpr_10, (gpr_9, gpr_8);
    0x400034: ldrb__r32__t_2_r64_n gpr_11, (sp, 7);
    0x400038: cmp__r32__r32 gpr_10, gpr_11;
    0x40003c: b_ne__n 0x400060bv64;
ENTRY_4194368:
    0x400040: adrp__r64__n gpr_8, 0x500000bv64;
    0x400044: add__r64__r64__n gpr_8, gpr_8, 0x10bv64;
    0x400048: ldrb__r32__t_1_r64 gpr_9, (gpr_8);
    0x40004c: adrp__r64__n gpr_8, 0x500000bv64;
    0x400050: add__r64__r64__n gpr_8, gpr_8, 0x18bv64;
    0x400054: ldrb__r32__t_1_r64 gpr_10, (gpr_8);
    0x400058: and__r32__r32__r32 gpr_9, gpr_10, gpr_9;
    0x40005c: strb__r32__t_1_r64 gpr_9, (gpr_8);
    0x400060: add__r64__r64__n sp, sp, 0x10bv64;
    0x400064: ret;
}
