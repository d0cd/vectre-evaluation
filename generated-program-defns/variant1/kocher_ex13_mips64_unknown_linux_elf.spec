prog _generated-binaries_variant1_kocher_ex13_mips64_unknown_linux_elf {
ENTRY_4194304:
    4194304:	daddiu	$sp, $sp, -0x30;
    4194308:	sd	$ra, 0x28($sp);
    4194312:	sd	$fp, 0x20($sp);
    4194316c:	sd	$gp, 0x18($sp);
    4194320:	move	$fp, $sp;
    4194324:	lui	$at, 0;
    4194328:	daddu	$at, $at, $t9;
    4194332c:	daddiu	$at, $at, 0;
    4194336:	sd	$a0, 0x10($fp);
    4194340:	ld	$a0, 0x10($fp);
    4194344:	ld	$t9, ($at);
    4194348c:	move	$gp, $at;
    4194352:	sd	$at, 8($fp);
    4194356:	jalr	$t9;
    4194360:	nop;
ENTRY_5242968:

ENTRY_4194364:
    4194364c:	beqz	$v0, 0x400088;
    4194368:	nop;
ENTRY_4194440:
    4194440:	move	$sp, $fp;
    4194444c:	ld	$gp, 0x18($sp);
    4194448:	ld	$fp, 0x20($sp);
    4194452:	ld	$ra, 0x28($sp);
    4194456:	daddiu	$sp, $sp, 0x30;
    4194460c:	jr	$ra;
    4194464a0:	nop;
ENTRY_4194372:
    4194372:	b	0x40004c;
    4194376:	nop;
ENTRY_4194380:
    4194380c:	ld	$at, 0x10($fp);
    4194384:	ld	$v0, 8($fp);
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
