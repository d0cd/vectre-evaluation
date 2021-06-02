prog _generated-binaries_variant1_kocher_ex9_aarch64 {
ENTRY_4194304:
    4194304:	sub	sp, sp, #0x10;
    4194308:	str	x0, [sp, #8];
    4194312:	str	x1, [sp];
    4194316c:	ldr	x8, [sp];
    4194320:	ldr	w9, [x8];
    4194324:	cbz	w9, #0x400050;
ENTRY_4194384:
    4194384:	add	sp, sp, #0x10;
    4194388:	ret;
ENTRY_4194328:
    4194328:	ldr	x8, [sp, #8];
    4194332c:	adrp	x9, #0x500000;
    4194336:	add	x9, x9, #0;
    4194340:	ldrb	w10, [x9, x8];
    4194344:	movz	w11, #0x200;
    4194348c:	mul	w10, w10, w11;
    4194352:	adrp	x8, #0x500000;
    4194356:	add	x8, x8, #8;
    4194360:	ldrb	w10, [x8, w10, sxtw];
    4194364c:	adrp	x8, #0x500000;
    4194368:	add	x8, x8, #0x10;
    4194372:	ldrb	w11, [x8];
    4194376:	and	w10, w11, w10;
    4194380c:	strb	w10, [x8];
    4194384:	add	sp, sp, #0x10;
    4194388:	ret;
}
