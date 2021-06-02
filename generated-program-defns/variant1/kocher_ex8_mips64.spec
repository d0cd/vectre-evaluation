prog _generated-binaries_variant1_kocher_ex8_mips64 {
ENTRY_4194304:
    4194304:	daddiu	$sp, $sp, -0x30;
    4194308:	sd	$ra, 0x28($sp);
    4194312:	sd	$fp, 0x20($sp);
    4194316c:	move	$fp, $sp;
    4194320:	lui	$at, 0;
    4194324:	daddu	$at, $at, $t9;
    4194328:	daddiu	$at, $at, 0;
    4194332c:	sd	$a0, 0x18($fp);
    4194336:	ld	$v0, 0x18($fp);
    4194340:	ld	$v1, ($at);
    4194344:	ld	$v1, ($v1);
    4194348c:	sltu	$a1, $v0, $v1;
    4194352:	sd	$at, 0x10($fp);
    4194356:	beqz	$a1, 0x400058;
    4194360:	nop;
ENTRY_4194392:
    4194392:	daddiu	$at, $zero, 0;
    4194396c:	sd	$at, 8($fp);
    4194400:	b	0x400068;
    4194404:	nop;
ENTRY_4194364:
    4194364c:	b	0x400044;
    4194368:	nop;
ENTRY_4194408:
    4194408:	ld	$at, 8($fp);
    4194412c:	ld	$v0, 0x10($fp);
    4194416:	ld	$v1, ($v0);
    4194420:	daddu	$at, $v1, $at;
    4194424:	lbu	$at, ($at);
    4194428c:	dsll	$at, $at, 9;
    4194432:	ld	$v1, ($v0);
    4194436:	daddu	$at, $v1, $at;
    4194440:	lbu	$a0, ($at);
    4194444c:	ld	$at, ($v0);
    4194448:	lbu	$a1, ($at);
    4194452:	and	$a0, $a1, $a0;
    4194456:	sb	$a0, ($at);
    4194460c:	move	$sp, $fp;
    4194464a0:	ld	$fp, 0x20($sp);
    4194468a4:	ld	$ra, 0x28($sp);
    4194472a8:	daddiu	$sp, $sp, 0x30;
    4194476ac:	jr	$ra;
    4194480b0:	nop;
ENTRY_4194372:
    4194372:	ld	$at, 0x18($fp);
    4194376:	daddiu	$at, $at, 1;
    4194380c:	sd	$at, 8($fp);
    4194384:	b	0x400068;
    4194388:	nop;
}
