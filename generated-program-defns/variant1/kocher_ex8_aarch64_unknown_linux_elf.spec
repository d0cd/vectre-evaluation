prog _generated-binaries_variant1_kocher_ex8_aarch64_unknown_linux_elf {
ENTRY_4194304:
    4194304:	sub	sp, sp, #0x10;
    4194308:	adrp	x8, #0x500000;
    4194312:	add	x8, x8, #0;
    4194316c:	str	x0, [sp, #8];
    4194320:	ldr	x9, [sp, #8];
    4194324:	ldr	x8, [x8];
    4194328:	cmp	x9, x8;
    4194332c:	b.hs	#0x400030;
ENTRY_4194352:
    4194352:	mov	x8, xzr;
    4194356:	str	x8, [sp];
    4194360:	ldr	x8, [sp];
    4194364c:	adrp	x9, #0x500000;
    4194368:	add	x9, x9, #8;
    4194372:	ldrb	w10, [x9, x8];
    4194376:	movz	w11, #0x200;
    4194380c:	mul	w10, w10, w11;
    4194384:	adrp	x8, #0x500000;
    4194388:	add	x8, x8, #0x10;
    4194392:	ldrb	w10, [x8, w10, sxtw];
    4194396c:	adrp	x8, #0x500000;
    4194400:	add	x8, x8, #0x18;
    4194404:	ldrb	w11, [x8];
    4194408:	and	w10, w11, w10;
    4194412c:	strb	w10, [x8];
    4194416:	add	sp, sp, #0x10;
    4194420:	ret;
ENTRY_4194336:
    4194336:	ldr	x8, [sp, #8];
    4194340:	add	x8, x8, #1;
    4194344:	str	x8, [sp];
    4194348c:	b	#0x400038;
ENTRY_4194360:
    4194360:	ldr	x8, [sp];
    4194364c:	adrp	x9, #0x500000;
    4194368:	add	x9, x9, #8;
    4194372:	ldrb	w10, [x9, x8];
    4194376:	movz	w11, #0x200;
    4194380c:	mul	w10, w10, w11;
    4194384:	adrp	x8, #0x500000;
    4194388:	add	x8, x8, #0x10;
    4194392:	ldrb	w10, [x8, w10, sxtw];
    4194396c:	adrp	x8, #0x500000;
    4194400:	add	x8, x8, #0x18;
    4194404:	ldrb	w11, [x8];
    4194408:	and	w10, w11, w10;
    4194412c:	strb	w10, [x8];
    4194416:	add	sp, sp, #0x10;
    4194420:	ret;
}
