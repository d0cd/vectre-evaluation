prog _generated-binaries_variant1_kocher_ex3_aarch64_unknown_linux_elf {
ENTRY_4194304:
    4194304:	sub	sp, sp, #0x10;
    4194308:	movz	w8, #0x200;
    4194312:	adrp	x9, #0x400000;
    4194316c:	add	x9, x9, #1;
    4194320:	adrp	x10, #0x400000;
    4194324:	add	x10, x10, #1;
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
    4194376:	adrp	x8, #0x400000;
    4194380c:	add	x8, x8, #8;
    4194384:	str	x0, [sp, #8];
    4194388:	ldr	x9, [sp, #8];
    4194392:	ldr	x8, [x8];
    4194396c:	cmp	x9, x8;
    4194400:	b.hs	#0x400078;
ENTRY_4194424:
    4194424:	ldp	x29, x30, [sp, #0x10];
    4194428c:	add	sp, sp, #0x20;
    4194432:	ret;
ENTRY_4194404:
    4194404:	ldr	x8, [sp, #8];
    4194408:	adrp	x9, #0x400000;
    4194412c:	add	x9, x9, #1;
    4194416:	ldrb	w0, [x9, x8];
    4194420:	bl	#0x400000;
}
