prog _generated_binaries_variant1_kocher_ex2_aarch64 {
ENTRY_4194304:
    0x400000: sub__r64__r64__n sp, sp, 0x10bv64;
    0x400004: movz__r32__n gpr_8, 0x200bv64;
    0x400008: adrp__r64__n gpr_9, 0x500000bv64;
    0x40000c: add__r64__r64__n gpr_9, gpr_9, 0;
    0x400010: adrp__r64__n gpr_10, 0x500000bv64;
    0x400014: add__r64__r64__n gpr_10, gpr_10, 8;
    0x400018: strb__r32__t_2_r64_n gpr_0, (sp, 0xfbv64);
    0x40001c: ldrb__r32__t_2_r64_n gpr_11, (sp, 0xfbv64);
    0x400020: mul__r32__r32__r32 gpr_8, gpr_11, gpr_8;
    0x400024: ldrb__r32__t_2_r64_r32_sxtw gpr_8, (gpr_9, gpr_8);
    0x400028: ldrb__r32__t_1_r64 gpr_11, (gpr_10);
    0x40002c: and__r32__r32__r32 gpr_8, gpr_11, gpr_8;
    0x400030: strb__r32__t_1_r64 gpr_8, (gpr_10);
    0x400034: add__r64__r64__n sp, sp, 0x10bv64;
    0x400038: ret;
ENTRY_4194364:
    0x40003c: sub__r64__r64__n sp, sp, 0x20bv64;
    0x400040: stp__r64__r64__t_2_r64_n gpr_29, gpr_30, (sp, 0x10bv64);
    0x400044: add__r64__r64__n gpr_29, sp, 0x10bv64;
    0x400048: adrp__r64__n gpr_8, 0x500000bv64;
    0x40004c: add__r64__r64__n gpr_8, gpr_8, 0x10bv64;
    0x400050: adrp__r64__n gpr_9, 0x500000bv64;
    0x400054: add__r64__r64__n gpr_9, gpr_9, 0x18bv64;
    0x400058: str__r64__t_2_r64_n gpr_0, (sp, 8);
    0x40005c: ldr__r64__t_2_r64_n gpr_10, (sp, 8);
    0x400060: ldr__r64__t_1_r64 gpr_8, (gpr_8);
    0x400064: cmp__r64__r64 gpr_10, gpr_8;
    0x400068: str__r64__t_1_r64 gpr_9, (sp);
    0x40006c: b_hs__n 0x400088bv64;
ENTRY_4194440:
    0x400088: ldp__r64__r64__t_2_r64_n gpr_29, gpr_30, (sp, 0x10bv64);
    0x40008c: add__r64__r64__n sp, sp, 0x20bv64;
    0x400090: ret;
ENTRY_4194416:
    0x400070: ldr__r64__t_2_r64_n gpr_8, (sp, 8);
    0x400074: adrp__r64__n gpr_9, 0x500000bv64;
    0x400078: add__r64__r64__n gpr_9, gpr_9, 0x20bv64;
    0x40007c: ldrb__r32__t_2_r64_r64 gpr_0, (gpr_9, gpr_8);
    0x400080: ldr__r64__t_1_r64 gpr_8, (sp);
    0x400084: blr__r64 gpr_8;

}
