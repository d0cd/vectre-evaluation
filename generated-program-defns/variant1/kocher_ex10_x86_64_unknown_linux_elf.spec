prog _generated-binaries_variant1_kocher_ex10_x86_64_unknown_linux_elf {
ENTRY_4194304:
    4194304:	push	rbp;
    4194305:	mov	rbp, rsp;
    4194308:	mov	qword ptr [rbp - 8], rdi;
    4194312:	mov	byte ptr [rbp - 9], sil;
    4194316c:	mov	rax, qword ptr [rbp - 8];
    4194320:	cmp	rax, qword ptr [0x500000];
    4194328:	jae	0x400054;
ENTRY_4194334:
    4194334e:	mov	rax, qword ptr [rbp - 8];
    4194338:	movzx	ecx, byte ptr [rax + 0x500008];
    4194346a:	movzx	edx, byte ptr [rbp - 9];
    4194350e:	cmp	ecx, edx;
    4194352:	jne	0x40004f;
ENTRY_4194388:
    4194388:	pop	rbp;
    4194389:	ret;
ENTRY_4194358:
    4194358:	movzx	eax, byte ptr [0x500010];
    4194366e:	movzx	ecx, byte ptr [0x500018];
    4194374:	and	ecx, eax;
    4194376:	mov	byte ptr [0x500018], cl;
    4194383f:	jmp	0x400054;
ENTRY_4194383:
    4194383f:	jmp	0x400054;
}
