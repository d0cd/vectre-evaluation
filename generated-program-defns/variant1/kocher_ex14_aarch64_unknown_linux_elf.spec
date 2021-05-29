prog _generated-binaries_variant1_kocher_ex14_aarch64_unknown_linux_elf {
ENTRY_4194304:
    4194304:	sub	sp, sp, #0x10;
    4194308:	adrp	x8, #0x500000;
    4194312:	add	x8, x8, #0;
    4194316c:	str	x0, [sp, #8];
    4194320:	ldr	x9, [sp, #8];
    4194324:	ldr	x8, [x8];
    4194328:	cmp	x9, x8;
    4194332c:	b.hs	#0x40005c;
ENTRY_4194396:
    4194396c:	add	sp, sp, #0x10;
    4194400:	ret;
ENTRY_4194336:
    4194336:	ldr	x8, [sp, #8];
    4194340:	eor	x8, x8, #0xff;
    4194344:	adrp	x9, #0x500000;
    4194348c:	add	x9, x9, #8;
    4194352:	ldrb	w10, [x9, x8];
    4194356:	movz	w11, #0x200;
    4194360:	mul	w10, w10, w11;
    4194364c:	adrp	x8, #0x500000;
    4194368:	add	x8, x8, #0x10;
    4194372:	ldrb	w10, [x8, w10, sxtw];
    4194376:	adrp	x8, #0x500000;
    4194380c:	add	x8, x8, #0x18;
    4194384:	ldrb	w11, [x8];
    4194388:	and	w10, w11, w10;
    4194392:	strb	w10, [x8];
    4194396c:	add	sp, sp, #0x10;
    4194400:	ret;
}
