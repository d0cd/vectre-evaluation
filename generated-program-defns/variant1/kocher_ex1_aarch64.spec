prog _generated-binaries_variant1_kocher_ex1_aarch64 {
ENTRY_4194304:
    4194304:	sub	sp, sp, #0x10;
    4194308:	adrp	x8, #0x400000;
    4194312:	add	x8, x8, #8;
    4194316c:	str	x0, [sp, #8];
    4194320:	ldr	x9, [sp, #8];
    4194324:	ldr	x8, [x8];
    4194328:	cmp	x9, x8;
    4194332c:	b.hs	#0x400058;
ENTRY_4194400:
    4194400:	ret;
ENTRY_4194392:
    4194392:	add	sp, sp, #0x10;
    4194396c:	ret;
ENTRY_4194336:
    4194336:	ldr	x8, [sp, #8];
    4194340:	adrp	x9, #0x400000;
    4194344:	add	x9, x9, #1;
    4194348c:	ldrb	w10, [x9, x8];
    4194352:	movz	w11, #0x200;
    4194356:	mul	w10, w10, w11;
    4194360:	adrp	x8, #0x400000;
    4194364c:	add	x8, x8, #1;
    4194368:	ldrb	w10, [x8, w10, sxtw];
    4194372:	adrp	x8, #0x400000;
    4194376:	add	x8, x8, #1;
    4194380c:	ldrb	w11, [x8];
    4194384:	and	w10, w11, w10;
    4194388:	strb	w10, [x8];
    4194392:	add	sp, sp, #0x10;
    4194396c:	ret;
}