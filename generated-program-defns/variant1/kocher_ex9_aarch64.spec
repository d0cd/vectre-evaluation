prog _generated_binaries_variant1_kocher_ex9_aarch64 {
ENTRY_4194304:
    0x400000: sub__r64__r64__n sp, sp, 0x10bv64;
    0x400004: str__r64__t_2_r64_n gpr_0, (sp, 8);
    0x400008: str__r64__t_1_r64 gpr_1, (sp);
    0x40000c: ldr__r64__t_1_r64 gpr_8, (sp);
    0x400010: ldr__r32__t_1_r64 gpr_9, (gpr_8);
    0x400014: cbz__r32__n gpr_9, 0x400050bv64;
ENTRY_4194384:
    0x400050: add__r64__r64__n sp, sp, 0x10bv64;
    0x400054: ret;
ENTRY_4194328:
    0x400018: ldr__r64__t_2_r64_n gpr_8, (sp, 8);
    0x40001c: adrp__r64__n gpr_9, 0x500000bv64;
    0x400020: add__r64__r64__n gpr_9, gpr_9, 0;
    0x400024: ldrb__r32__t_2_r64_r64 gpr_10, (gpr_9, gpr_8);
    0x400028: movz__r32__n gpr_11, 0x200bv64;
    0x40002c: mul__r32__r32__r32 gpr_10, gpr_10, gpr_11;
    0x400030: adrp__r64__n gpr_8, 0x500000bv64;
    0x400034: add__r64__r64__n gpr_8, gpr_8, 8;
    0x400038: ldrb__r32__t_2_r64_r32_sxtw gpr_10, (gpr_8, gpr_10);
    0x40003c: adrp__r64__n gpr_8, 0x500000bv64;
    0x400040: add__r64__r64__n gpr_8, gpr_8, 0x10bv64;
    0x400044: ldrb__r32__t_1_r64 gpr_11, (gpr_8);
    0x400048: and__r32__r32__r32 gpr_10, gpr_11, gpr_10;
    0x40004c: strb__r32__t_1_r64 gpr_10, (gpr_8);
    0x400050: add__r64__r64__n sp, sp, 0x10bv64;
    0x400054: ret;
}
