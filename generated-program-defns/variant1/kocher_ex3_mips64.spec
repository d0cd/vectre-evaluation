prog _generated-binaries_variant1_kocher_ex3_mips64 {
ENTRY_4194304:
    4194304:	daddiu	$sp, $sp, -0x20;
    4194308:	sd	$ra, 0x18($sp);
    4194312:	sd	$fp, 0x10($sp);
    4194316c:	move	$fp, $sp;
    4194320:	lui	$at, 0;
    4194324:	daddu	$at, $at, $t9;
    4194328:	daddiu	$at, $at, 0;
    4194332c:	sb	$a0, 0xc($fp);
    4194336:	lbu	$v0, 0xc($fp);
    4194340:	dsll	$v0, $v0, 9;
    4194344:	ld	$v1, ($at);
    4194348c:	daddu	$v0, $v1, $v0;
    4194352:	lbu	$a0, ($v0);
    4194356:	ld	$at, ($at);
    4194360:	lbu	$a1, ($at);
    4194364c:	and	$a0, $a1, $a0;
    4194368:	sb	$a0, ($at);
    4194372:	move	$sp, $fp;
    4194376:	ld	$fp, 0x10($sp);
    4194380c:	ld	$ra, 0x18($sp);
    4194384:	daddiu	$sp, $sp, 0x20;
    4194388:	jr	$ra;
    4194392:	nop;
ENTRY_4194400:
    4194400:	daddiu	$sp, $sp, -0x30;
    4194404:	sd	$ra, 0x28($sp);
    4194408:	sd	$fp, 0x20($sp);
    4194412c:	sd	$gp, 0x18($sp);
    4194416:	move	$fp, $sp;
    4194420:	lui	$at, 0;
    4194424:	daddu	$at, $at, $t9;
    4194428c:	daddiu	$at, $at, 0;
    4194432:	sd	$a0, 0x10($fp);
    4194436:	ld	$v0, 0x10($fp);
    4194440:	ld	$v1, ($at);
    4194444c:	ld	$v1, ($v1);
    4194448:	sltu	$a1, $v0, $v1;
    4194452:	sd	$at, 8($fp);
    4194456:	beqz	$a1, 0x4000d4;
    4194460c:	nop;
ENTRY_4194516:
    4194516d4:	move	$sp, $fp;
    4194520d8:	ld	$gp, 0x18($sp);
    4194524dc:	ld	$fp, 0x20($sp);
    4194528e0:	ld	$ra, 0x28($sp);
    4194532e4:	daddiu	$sp, $sp, 0x30;
    4194536e8:	jr	$ra;
    4194540ec:	nop;
ENTRY_4194464:
    4194464a0:	b	0x4000a8;
    4194468a4:	nop;
ENTRY_4194472:
    4194472a8:	ld	$at, 0x10($fp);
    4194476ac:	ld	$v0, 8($fp);
    4194480b0:	ld	$v1, ($v0);
    4194484b4:	daddu	$at, $v1, $at;
    4194488b8:	lbu	$a0, ($at);
    4194492bc:	ld	$t9, ($v0);
    4194496c0:	move	$gp, $v0;
    4194500c4:	jalr	$t9;
    4194504c8:	nop;
ENTRY_5242968:

ENTRY_4194508:
    4194508cc:	b	0x4000d4;
    4194512d0:	nop;
}
