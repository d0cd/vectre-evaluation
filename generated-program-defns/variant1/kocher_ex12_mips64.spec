prog _generated-binaries_variant1_kocher_ex12_mips64 {
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
    4194340:	ld	$v0, 0x18($fp);
    4194344:	ld	$v1, 0x10($fp);
    4194348c:	daddu	$v0, $v0, $v1;
    4194352:	ld	$v1, ($at);
    4194356:	ld	$v1, ($v1);
    4194360:	sltu	$a2, $v0, $v1;
    4194364c:	sd	$at, 8($fp);
    4194368:	beqz	$a2, 0x400094;
    4194372:	nop;
ENTRY_4194452:
    4194452:	move	$sp, $fp;
    4194456:	ld	$fp, 0x20($sp);
    4194460c:	ld	$ra, 0x28($sp);
    4194464a0:	daddiu	$sp, $sp, 0x30;
    4194468a4:	jr	$ra;
    4194472a8:	nop;
ENTRY_4194376:
    4194376:	b	0x400050;
    4194380c:	nop;
ENTRY_4194384:
    4194384:	ld	$at, 0x18($fp);
    4194388:	ld	$v0, 0x10($fp);
    4194392:	daddu	$at, $at, $v0;
    4194396c:	ld	$v0, 8($fp);
    4194400:	ld	$v1, ($v0);
    4194404:	daddu	$at, $v1, $at;
    4194408:	lbu	$at, ($at);
    4194412c:	dsll	$at, $at, 9;
    4194416:	ld	$v1, ($v0);
    4194420:	daddu	$at, $v1, $at;
    4194424:	lbu	$a0, ($at);
    4194428c:	ld	$at, ($v0);
    4194432:	lbu	$a1, ($at);
    4194436:	and	$a0, $a1, $a0;
    4194440:	sb	$a0, ($at);
    4194444c:	b	0x400094;
    4194448:	nop;
}
