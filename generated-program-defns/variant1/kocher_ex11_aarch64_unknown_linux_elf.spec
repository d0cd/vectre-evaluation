prog _generated-binaries_variant1_kocher_ex11_aarch64_unknown_linux_elf {
ENTRY_4194304:
    4194304:	sub	sp, sp, #0x20;
    4194308:	stp	x29, x30, [sp, #0x10];
    4194312:	add	x29, sp, #0x10;
    4194316c:	adrp	x8, #0x500000;
    4194320:	add	x8, x8, #0;
    4194324:	str	x0, [sp, #8];
    4194328:	ldr	x9, [sp, #8];
    4194332c:	ldr	x8, [x8];
    4194336:	cmp	x9, x8;
    4194340:	b.hs	#0x400074;
ENTRY_4194420:
    4194420:	ldp	x29, x30, [sp, #0x10];
    4194424:	add	sp, sp, #0x20;
    4194428c:	ret;
ENTRY_4194344:
    4194344:	ldr	x8, [sp, #8];
    4194348c:	adrp	x9, #0x500000;
    4194352:	add	x9, x9, #8;
    4194356:	ldrb	w10, [x9, x8];
    4194360:	movz	w11, #0x200;
    4194364c:	mul	w10, w10, w11;
    4194368:	mov	w0, w10;
    4194372:	sxtw	x8, w0;
    4194376:	adrp	x9, #0x500000;
    4194380c:	add	x9, x9, #0x10;
    4194384:	add	x1, x9, x8;
    4194388:	adrp	x8, #0x500000;
    4194392:	add	x8, x8, #0x18;
    4194396c:	mov	x0, x8;
    4194400:	movz	x2, #0x1;
    4194404:	str	x8, [sp];
    4194408:	bl	#0x500020;
ENTRY_5242912:

ENTRY_4194412:
    4194412c:	ldr	x8, [sp];
    4194416:	strb	w0, [x8];
    4194420:	ldp	x29, x30, [sp, #0x10];
    4194424:	add	sp, sp, #0x20;
    4194428c:	ret;
}
