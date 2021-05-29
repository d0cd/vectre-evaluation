prog _generated-binaries_variant1_kocher_ex10_mips64_unknown_linux_elf {
ENTRY_4194304:
    4194304:	daddiu	$sp, $sp, -0x30;
    4194308:	sd	$ra, 0x28($sp);
    4194312:	sd	$fp, 0x20($sp);
    4194316c:	move	$fp, $sp;
    4194320:	lui	$at, 0;
    4194324:	daddu	$at, $at, $t9;
    4194328:	daddiu	$at, $at, 0;
    4194332c:	sd	$a0, 0x18($fp);
    4194336:	sb	$a1, 0x14($fp);
    4194340:	ld	$v0, 0x18($fp);
    4194344:	ld	$v1, ($at);
    4194348c:	ld	$v1, ($v1);
    4194352:	sltu	$a1, $v0, $v1;
    4194356:	sd	$at, 8($fp);
    4194360:	beqz	$a1, 0x40009c;
    4194364c:	nop;
ENTRY_4194460:
    4194460c:	move	$sp, $fp;
    4194464a0:	ld	$fp, 0x20($sp);
    4194468a4:	ld	$ra, 0x28($sp);
    4194472a8:	daddiu	$sp, $sp, 0x30;
    4194476ac:	jr	$ra;
    4194480b0:	nop;
ENTRY_4194368:
    4194368:	b	0x400048;
    4194372:	nop;
ENTRY_4194376:
    4194376:	ld	$at, 0x18($fp);
    4194380c:	ld	$v0, 8($fp);
    4194384:	ld	$v1, ($v0);
    4194388:	daddu	$at, $v1, $at;
    4194392:	lbu	$a0, ($at);
    4194396c:	lbu	$a1, 0x14($fp);
    4194400:	bne	$a0, $a1, 0x400094;
    4194404:	nop;
ENTRY_4194452:
    4194452:	b	0x40009c;
    4194456:	nop;
ENTRY_4194408:
    4194408:	b	0x400070;
    4194412c:	nop;
ENTRY_4194416:
    4194416:	ld	$at, 8($fp);
    4194420:	ld	$v0, ($at);
    4194424:	lbu	$v1, ($v0);
    4194428c:	ld	$v0, ($at);
    4194432:	lbu	$a0, ($v0);
    4194436:	and	$v1, $a0, $v1;
    4194440:	sb	$v1, ($v0);
    4194444c:	b	0x400094;
    4194448:	nop;
}
