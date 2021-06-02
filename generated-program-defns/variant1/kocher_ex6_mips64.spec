prog _generated-binaries_variant1_kocher_ex6_mips64 {
ENTRY_4194304:
    4194304:	daddiu	$sp, $sp, -0x20;
    4194308:	sd	$ra, 0x18($sp);
    4194312:	sd	$fp, 0x10($sp);
    4194316c:	move	$fp, $sp;
    4194320:	lui	$at, 0;
    4194324:	daddu	$at, $at, $t9;
    4194328:	daddiu	$at, $at, 0;
    4194332c:	sd	$a0, 8($fp);
    4194336:	ld	$v0, 8($fp);
    4194340:	ld	$v1, ($at);
    4194344:	ld	$v1, ($v1);
    4194348c:	and	$v1, $v0, $v1;
    4194352:	sd	$at, ($fp);
    4194356:	bne	$v1, $v0, 0x400080;
    4194360:	nop;
ENTRY_4194432:
    4194432:	move	$sp, $fp;
    4194436:	ld	$fp, 0x10($sp);
    4194440:	ld	$ra, 0x18($sp);
    4194444c:	daddiu	$sp, $sp, 0x20;
    4194448:	jr	$ra;
    4194452:	nop;
ENTRY_4194364:
    4194364c:	b	0x400044;
    4194368:	nop;
ENTRY_4194372:
    4194372:	ld	$at, 8($fp);
    4194376:	ld	$v0, ($fp);
    4194380c:	ld	$v1, ($v0);
    4194384:	daddu	$at, $v1, $at;
    4194388:	lbu	$at, ($at);
    4194392:	dsll	$at, $at, 9;
    4194396c:	ld	$v1, ($v0);
    4194400:	daddu	$at, $v1, $at;
    4194404:	lbu	$a0, ($at);
    4194408:	ld	$at, ($v0);
    4194412c:	lbu	$a1, ($at);
    4194416:	and	$a0, $a1, $a0;
    4194420:	sb	$a0, ($at);
    4194424:	b	0x400080;
    4194428c:	nop;
}
