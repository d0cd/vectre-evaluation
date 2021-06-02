prog _generated-binaries_variant1_kocher_ex11_mips64 {
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
    4194340:	ld	$v0, 0x10($fp);
    4194344:	ld	$v1, ($at);
    4194348c:	ld	$v1, ($v1);
    4194352:	sltu	$a1, $v0, $v1;
    4194356:	sd	$at, 8($fp);
    4194360:	beqz	$a1, 0x400098;
    4194364c:	nop;
ENTRY_4194456:
    4194456:	move	$sp, $fp;
    4194460c:	ld	$gp, 0x18($sp);
    4194464a0:	ld	$fp, 0x20($sp);
    4194468a4:	ld	$ra, 0x28($sp);
    4194472a8:	daddiu	$sp, $sp, 0x30;
    4194476ac:	jr	$ra;
    4194480b0:	nop;
ENTRY_4194368:
    4194368:	b	0x400048;
    4194372:	nop;
ENTRY_4194376:
    4194376:	ld	$at, 0x10($fp);
    4194380c:	ld	$v0, 8($fp);
    4194384:	ld	$v1, ($v0);
    4194388:	daddu	$at, $v1, $at;
    4194392:	lbu	$at, ($at);
    4194396c:	dsll	$at, $at, 9;
    4194400:	ld	$v1, ($v0);
    4194404:	daddu	$a1, $v1, $at;
    4194408:	ld	$at, ($v0);
    4194412c:	ld	$t9, ($v0);
    4194416:	daddiu	$a2, $zero, 1;
    4194420:	move	$a0, $at;
    4194424:	move	$gp, $v0;
    4194428c:	sd	$at, ($fp);
    4194432:	jalr	$t9;
    4194436:	nop;
ENTRY_5242968:

ENTRY_4194440:
    4194440:	ld	$at, ($fp);
    4194444c:	sb	$v0, ($at);
    4194448:	b	0x400098;
    4194452:	nop;
}
