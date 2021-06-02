prog _generated-binaries_variant1_kocher_ex5_mips64 {
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
    4194352:	sd	$at, 8($fp);
    4194356:	beqz	$a1, 0x4000c8;
    4194360:	nop;
ENTRY_4194504:
    4194504c8:	move	$sp, $fp;
    4194508cc:	ld	$fp, 0x20($sp);
    4194512d0:	ld	$ra, 0x28($sp);
    4194516d4:	daddiu	$sp, $sp, 0x30;
    4194520d8:	jr	$ra;
    4194524dc:	nop;
ENTRY_4194364:
    4194364c:	b	0x400044;
    4194368:	nop;
ENTRY_4194372:
    4194372:	ld	$at, 0x18($fp);
    4194376:	daddiu	$at, $at, -1;
    4194380c:	sd	$at, 0x10($fp);
    4194384:	b	0x400058;
    4194388:	nop;
ENTRY_4194392:
    4194392:	addiu	$at, $zero, 0;
    4194396c:	sw	$at, 4($fp);
    4194400:	bnez	$zero, 0x4000c0;
    4194404:	nop;
ENTRY_4194408:
    4194408:	b	0x400070;
    4194412c:	nop;
ENTRY_4194416:
    4194416:	ld	$at, 0x10($fp);
    4194420:	ld	$v0, 8($fp);
    4194424:	ld	$v1, ($v0);
    4194428c:	daddu	$at, $v1, $at;
    4194432:	lbu	$at, ($at);
    4194436:	dsll	$at, $at, 9;
    4194440:	ld	$v1, ($v0);
    4194444c:	daddu	$at, $v1, $at;
    4194448:	lbu	$a0, ($at);
    4194452:	ld	$at, ($v0);
    4194456:	lbu	$a1, ($at);
    4194460c:	and	$a0, $a1, $a0;
    4194464a0:	sb	$a0, ($at);
    4194468a4:	b	0x4000ac;
    4194472a8:	nop;
ENTRY_4194476:
    4194476ac:	ld	$at, 0x10($fp);
    4194480b0:	daddiu	$at, $at, -1;
    4194484b4:	sd	$at, 0x10($fp);
    4194488b8:	b	0x400058;
    4194492bc:	nop;
ENTRY_4194496:
    4194496c0:	b	0x4000c8;
    4194500c4:	nop;
}
