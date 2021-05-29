prog _generated-binaries_variant1_kocher_ex15_mips64_unknown_linux_elf {
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
    4194340:	ld	$v0, ($v0);
    4194344:	ld	$v1, ($at);
    4194348c:	ld	$v1, ($v1);
    4194352:	sltu	$a1, $v0, $v1;
    4194356:	sd	$at, ($fp);
    4194360:	beqz	$a1, 0x400088;
    4194364c:	nop;
ENTRY_4194440:
    4194440:	move	$sp, $fp;
    4194444c:	ld	$fp, 0x10($sp);
    4194448:	ld	$ra, 0x18($sp);
    4194452:	daddiu	$sp, $sp, 0x20;
    4194456:	jr	$ra;
    4194460c:	nop;
ENTRY_4194368:
    4194368:	b	0x400048;
    4194372:	nop;
ENTRY_4194376:
    4194376:	ld	$at, 8($fp);
    4194380c:	ld	$at, ($at);
    4194384:	ld	$v0, ($fp);
    4194388:	ld	$v1, ($v0);
    4194392:	daddu	$at, $v1, $at;
    4194396c:	lbu	$at, ($at);
    4194400:	dsll	$at, $at, 9;
    4194404:	ld	$v1, ($v0);
    4194408:	daddu	$at, $v1, $at;
    4194412c:	lbu	$a0, ($at);
    4194416:	ld	$at, ($v0);
    4194420:	lbu	$a1, ($at);
    4194424:	and	$a0, $a1, $a0;
    4194428c:	sb	$a0, ($at);
    4194432:	b	0x400088;
    4194436:	nop;
}
