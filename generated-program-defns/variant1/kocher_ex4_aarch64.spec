prog _generated_binaries_variant1_kocher_ex4_aarch64 {
ENTRY_4194304:
    0x400000: sub__r64__r64__n sp, sp, 0x10bv64;
    0x400004: adrp__r64__n gpr_8, 0x500000bv64;
    0x400008: add__r64__r64__n gpr_8, gpr_8, 0;
    0x40000c: str__r64__t_2_r64_n gpr_0, (sp, 8);
    0x400010: ldr__r64__t_2_r64_n gpr_9, (sp, 8);
    0x400014: ldr__r64__t_1_r64 gpr_8, (gpr_8);
    0x400018: cmp__r64__r64 gpr_9, gpr_8;
    0x40001c: b_hs__n 0x40005cbv64;
ENTRY_4194396:
    0x40005c: add__r64__r64__n sp, sp, 0x10bv64;
    0x400060: ret;
ENTRY_4194336:
    0x400020: ldr__r64__t_2_r64_n gpr_8, (sp, 8);
    0x400024: lsl__r64__r64__n gpr_8, gpr_8, 1;
    0x400028: adrp__r64__n gpr_9, 0x500000bv64;
    0x40002c: add__r64__r64__n gpr_9, gpr_9, 8;
    0x400030: ldrb__r32__t_2_r64_r64 gpr_10, (gpr_9, gpr_8);
    0x400034: movz__r32__n gpr_11, 0x200bv64;
    0x400038: mul__r32__r32__r32 gpr_10, gpr_10, gpr_11;
    0x40003c: adrp__r64__n gpr_8, 0x500000bv64;
    0x400040: add__r64__r64__n gpr_8, gpr_8, 0x10bv64;
    0x400044: ldrb__r32__t_2_r64_r32_sxtw gpr_10, (gpr_8, gpr_10);
    0x400048: adrp__r64__n gpr_8, 0x500000bv64;
    0x40004c: add__r64__r64__n gpr_8, gpr_8, 0x18bv64;
    0x400050: ldrb__r32__t_1_r64 gpr_11, (gpr_8);
    0x400054: and__r32__r32__r32 gpr_10, gpr_11, gpr_10;
    0x400058: strb__r32__t_1_r64 gpr_10, (gpr_8);
    0x40005c: add__r64__r64__n sp, sp, 0x10bv64;
    0x400060: ret;
}
