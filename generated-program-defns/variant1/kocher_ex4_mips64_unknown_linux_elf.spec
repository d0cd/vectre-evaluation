prog _generated-binaries_variant1_kocher_ex4_mips64_unknown_linux_elf {
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
    4194348c:	sltu	$a1, $v0, $v1;
    4194352:	sd	$at, ($fp);
    4194356:	beqz	$a1, 0x400084;
    4194360:	nop;
ENTRY_4194436:
    4194436:	move	$sp, $fp;
    4194440:	ld	$fp, 0x10($sp);
    4194444c:	ld	$ra, 0x18($sp);
    4194448:	daddiu	$sp, $sp, 0x20;
    4194452:	jr	$ra;
    4194456:	nop;
ENTRY_4194364:
    4194364c:	b	0x400044;
    4194368:	nop;
ENTRY_4194372:
    4194372:	ld	$at, 8($fp);
    4194376:	dsll	$at, $at, 1;
    4194380c:	ld	$v0, ($fp);
    4194384:	ld	$v1, ($v0);
    4194388:	daddu	$at, $v1, $at;
    4194392:	lbu	$at, ($at);
    4194396c:	dsll	$at, $at, 9;
    4194400:	ld	$v1, ($v0);
    4194404:	daddu	$at, $v1, $at;
    4194408:	lbu	$a0, ($at);
    4194412c:	ld	$at, ($v0);
    4194416:	lbu	$a1, ($at);
    4194420:	and	$a0, $a1, $a0;
    4194424:	sb	$a0, ($at);
    4194428c:	b	0x400084;
    4194432:	nop;
}
