prog _generated-binaries_variant1_kocher_ex7_mips64 {
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
    4194348c:	sd	$at, ($fp);
    4194352:	bne	$v0, $v1, 0x40007c;
    4194356:	nop;
ENTRY_4194428:
    4194428c:	ld	$at, 8($fp);
    4194432:	ld	$v0, ($fp);
    4194436:	ld	$v1, ($v0);
    4194440:	ld	$v1, ($v1);
    4194444c:	sltu	$a0, $at, $v1;
    4194448:	beqz	$a0, 0x4000b8;
    4194452:	nop;
ENTRY_4194360:
    4194360:	b	0x400040;
    4194364c:	nop;
ENTRY_4194488:
    4194488b8:	move	$sp, $fp;
    4194492bc:	ld	$fp, 0x10($sp);
    4194496c0:	ld	$ra, 0x18($sp);
    4194500c4:	daddiu	$sp, $sp, 0x20;
    4194504c8:	jr	$ra;
    4194508cc:	nop;
ENTRY_4194456:
    4194456:	b	0x4000a0;
    4194460c:	nop;
ENTRY_4194368:
    4194368:	ld	$at, 8($fp);
    4194372:	ld	$v0, ($fp);
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
ENTRY_4194464:
    4194464a0:	ld	$at, 8($fp);
    4194468a4:	ld	$v0, ($fp);
    4194472a8:	ld	$v1, ($v0);
    4194476ac:	sd	$at, ($v1);
    4194480b0:	b	0x4000b8;
    4194484b4:	nop;
}
