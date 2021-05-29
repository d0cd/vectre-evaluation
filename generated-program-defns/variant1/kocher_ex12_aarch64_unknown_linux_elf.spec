prog _generated-binaries_variant1_kocher_ex12_aarch64_unknown_linux_elf {
ENTRY_4194304:
    4194304:	sub	sp, sp, #0x10;
    4194308:	adrp	x8, #0x500000;
    4194312:	add	x8, x8, #0;
    4194316c:	str	x0, [sp, #8];
    4194320:	str	x1, [sp];
    4194324:	ldr	x9, [sp, #8];
    4194328:	ldr	x10, [sp];
    4194332c:	add	x9, x9, x10;
    4194336:	ldr	x8, [x8];
    4194340:	cmp	x9, x8;
    4194344:	b.hs	#0x40006c;
ENTRY_4194412:
    4194412c:	add	sp, sp, #0x10;
    4194416:	ret;
ENTRY_4194348:
    4194348c:	ldr	x8, [sp, #8];
    4194352:	ldr	x9, [sp];
    4194356:	add	x8, x8, x9;
    4194360:	adrp	x9, #0x500000;
    4194364c:	add	x9, x9, #8;
    4194368:	ldrb	w10, [x9, x8];
    4194372:	movz	w11, #0x200;
    4194376:	mul	w10, w10, w11;
    4194380c:	adrp	x8, #0x500000;
    4194384:	add	x8, x8, #0x10;
    4194388:	ldrb	w10, [x8, w10, sxtw];
    4194392:	adrp	x8, #0x500000;
    4194396c:	add	x8, x8, #0x18;
    4194400:	ldrb	w11, [x8];
    4194404:	and	w10, w11, w10;
    4194408:	strb	w10, [x8];
    4194412c:	add	sp, sp, #0x10;
    4194416:	ret;
}
