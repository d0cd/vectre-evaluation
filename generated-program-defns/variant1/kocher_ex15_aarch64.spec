prog _generated-binaries_variant1_kocher_ex15_aarch64 {
ENTRY_4194304:
    4194304:	sub	sp, sp, #0x10;
    4194308:	adrp	x8, #0x500000;
    4194312:	add	x8, x8, #0;
    4194316c:	str	x0, [sp, #8];
    4194320:	ldr	x9, [sp, #8];
    4194324:	ldr	x9, [x9];
    4194328:	ldr	x8, [x8];
    4194332c:	cmp	x9, x8;
    4194336:	b.hs	#0x400060;
ENTRY_4194400:
    4194400:	add	sp, sp, #0x10;
    4194404:	ret;
ENTRY_4194340:
    4194340:	ldr	x8, [sp, #8];
    4194344:	ldr	x8, [x8];
    4194348c:	adrp	x9, #0x500000;
    4194352:	add	x9, x9, #8;
    4194356:	ldrb	w10, [x9, x8];
    4194360:	movz	w11, #0x200;
    4194364c:	mul	w10, w10, w11;
    4194368:	adrp	x8, #0x500000;
    4194372:	add	x8, x8, #0x10;
    4194376:	ldrb	w10, [x8, w10, sxtw];
    4194380c:	adrp	x8, #0x500000;
    4194384:	add	x8, x8, #0x18;
    4194388:	ldrb	w11, [x8];
    4194392:	and	w10, w11, w10;
    4194396c:	strb	w10, [x8];
    4194400:	add	sp, sp, #0x10;
    4194404:	ret;
}
