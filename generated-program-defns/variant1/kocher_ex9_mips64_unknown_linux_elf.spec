prog _generated-binaries_variant1_kocher_ex9_mips64_unknown_linux_elf {
ENTRY_4194304:
    4194304:	daddiu	$sp, $sp, -0x30;
    4194308:	sd	$ra, 0x28($sp);
    4194312:	sd	$fp, 0x20($sp);
    4194316c:	move	$fp, $sp;
    4194320:	lui	$at, 0;
    4194324:	daddu	$at, $at, $t9;
    4194328:	daddiu	$at, $at, 0;
    4194332c:	sd	$a0, 0x18($fp);
    4194336:	sd	$a1, 0x10($fp);
    4194340:	ld	$v0, 0x10($fp);
    4194344:	lw	$v1, ($v0);
    4194348c:	sd	$at, 8($fp);
    4194352:	beqz	$v1, 0x40007c;
    4194356:	nop;
ENTRY_4194428:
    4194428c:	move	$sp, $fp;
    4194432:	ld	$fp, 0x20($sp);
    4194436:	ld	$ra, 0x28($sp);
    4194440:	daddiu	$sp, $sp, 0x30;
    4194444c:	jr	$ra;
    4194448:	nop;
ENTRY_4194360:
    4194360:	b	0x400040;
    4194364c:	nop;
ENTRY_4194368:
    4194368:	ld	$at, 0x18($fp);
    4194372:	ld	$v0, 8($fp);
    4194376:	ld	$v1, ($v0);
    4194380c:	daddu	$at, $v1, $at;
    4194384:	lbu	$at, ($at);
    4194388:	dsll	$at, $at, 9;
    4194392:	ld	$v1, ($v0);
    4194396c:	daddu	$at, $v1, $at;
    4194400:	lbu	$a0, ($at);
    4194404:	ld	$at, ($v0);
    4194408:	lbu	$a1, ($at);
    4194412c:	and	$a0, $a1, $a0;
    4194416:	sb	$a0, ($at);
    4194420:	b	0x40007c;
    4194424:	nop;
}
