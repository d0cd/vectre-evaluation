prog _generated-binaries_variant1_kocher_ex2_aarch64_unknown_linux_elf {
ENTRY_4194304:
    4194304:	sub	sp, sp, #0x10;
    4194308:	movz	w8, #0x200;
    4194312:	adrp	x9, #0x500000;
    4194316c:	add	x9, x9, #0;
    4194320:	adrp	x10, #0x500000;
    4194324:	add	x10, x10, #8;
    4194328:	strb	w0, [sp, #0xf];
    4194332c:	ldrb	w11, [sp, #0xf];
    4194336:	mul	w8, w11, w8;
    4194340:	ldrb	w8, [x9, w8, sxtw];
    4194344:	ldrb	w11, [x10];
    4194348c:	and	w8, w11, w8;
    4194352:	strb	w8, [x10];
    4194356:	add	sp, sp, #0x10;
    4194360:	ret;
ENTRY_4194364:
    4194364c:	sub	sp, sp, #0x20;
    4194368:	stp	x29, x30, [sp, #0x10];
    4194372:	add	x29, sp, #0x10;
    4194376:	adrp	x8, #0x500000;
    4194380c:	add	x8, x8, #0x10;
    4194384:	adrp	x9, #0x500000;
    4194388:	add	x9, x9, #0x18;
    4194392:	str	x0, [sp, #8];
    4194396c:	ldr	x10, [sp, #8];
    4194400:	ldr	x8, [x8];
    4194404:	cmp	x10, x8;
    4194408:	str	x9, [sp];
    4194412c:	b.hs	#0x400088;
ENTRY_4194440:
    4194440:	ldp	x29, x30, [sp, #0x10];
    4194444c:	add	sp, sp, #0x20;
    4194448:	ret;
ENTRY_4194416:
    4194416:	ldr	x8, [sp, #8];
    4194420:	adrp	x9, #0x500000;
    4194424:	add	x9, x9, #0x20;
    4194428c:	ldrb	w0, [x9, x8];
    4194432:	ldr	x8, [sp];
    4194436:	blr	x8;
ENTRY_6295640:

}
