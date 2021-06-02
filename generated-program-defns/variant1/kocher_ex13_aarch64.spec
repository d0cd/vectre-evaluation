prog _generated-binaries_variant1_kocher_ex13_aarch64 {
ENTRY_4194304:
    4194304:	sub	sp, sp, #0x20;
    4194308:	stp	x29, x30, [sp, #0x10];
    4194312:	add	x29, sp, #0x10;
    4194316c:	str	x0, [sp, #8];
    4194320:	ldr	x0, [sp, #8];
    4194324:	bl	#0x500000;
ENTRY_5242880:

ENTRY_4194328:
    4194328:	cbz	w0, #0x400054;
ENTRY_4194388:
    4194388:	ldp	x29, x30, [sp, #0x10];
    4194392:	add	sp, sp, #0x20;
    4194396c:	ret;
ENTRY_4194332:
    4194332c:	ldr	x8, [sp, #8];
    4194336:	adrp	x9, #0x500000;
    4194340:	add	x9, x9, #8;
    4194344:	ldrb	w10, [x9, x8];
    4194348c:	movz	w11, #0x200;
    4194352:	mul	w10, w10, w11;
    4194356:	adrp	x8, #0x500000;
    4194360:	add	x8, x8, #0x10;
    4194364c:	ldrb	w10, [x8, w10, sxtw];
    4194368:	adrp	x8, #0x500000;
    4194372:	add	x8, x8, #0x18;
    4194376:	ldrb	w11, [x8];
    4194380c:	and	w10, w11, w10;
    4194384:	strb	w10, [x8];
    4194388:	ldp	x29, x30, [sp, #0x10];
    4194392:	add	sp, sp, #0x20;
    4194396c:	ret;
}
